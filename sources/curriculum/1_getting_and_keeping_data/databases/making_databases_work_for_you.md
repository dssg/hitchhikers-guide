
# Making databases work for you

## Motivation
Databases are great for dealing with large amounts of data in an efficient manner. We'll use databases (typically postgres) all summer for almost all of our projects. While you'll find them to be your new best friend, you're likely to get frustrated and annoyed  with them (just as you would with any best friend) if you don't set things up correctly up front. Here are some things to keep in mind that you should do early on to reduce your frustration and annoyance as you get to know each other better.

**Goals for today's session:**
- Common pitfalls to avoid when constructing tables
- Getting information about tables, columns, and grants
- Dealing with permissions and roles
- Improving the performance of your queries
- How to kill hung or run-away queries

## Common Pitfalls to Avoid When Constructing Tables

**TIP #1 -- Avoid modifying your raw data in place**

Even though you might have the source data backed up somewhere, using separate `raw` and `clean` schemas as you process the data you've loaded into the database is a best practice. Most projects will require considerable effort in data cleaning: fixing up data types, resolving different values with the same semantic meaning (e.g., abbreviations, typos), removing special characters, dealing with values out of the meaningful range (e.g., future or far past dates), etc. 

However, your data cleaning code may have bugs or make bad assumptions that you may need to modify as you iterate on the project. Keeping the raw data separate will both facilitate this process as well as allow you to easily compare the data you're working with to the source data to understand the impact of your transformations.


**TIP #2 -- Stick to lowercase characters for table and column names**

Although postgres will let you use upper-case letters and special characters in your column names, doing so means you'll have to reference these names with double quotes any time you reference then, which is both easily forgotten when querying the data by hand and prone to result in bugs that are hard to track down when code that queries the database programatically is buried deep in your pipeline.

To illustrate this point, let's take a look at the `FoodFacilities` table in the `sql_tips` schema of the training database. What happens when you try querying the name, city, state, and zipcode of some sample facilities?

Next try looking at the square footage, number of seats, and status of a few facilities. How well did that work?


**TIP #3 -- Table and column names are limited to 63 characters**

You can specify a longer name in your code but it will be truncated by postgres to the 63-character limit. This can cause us some real trouble when programatically creating feature names, especially when multiple columns will get truncated to the same thing or moving back and forth from python to postgres. Let's take a look:

```sql
create table sql_tips.my_very_long_table_name_that_is_much_too_long_for_a_postgres_table_name (
	id INT,
	this_is_a_really_long_column_name_that_is_also_going_to_cause_us_trouble VARCHAR
);

insert into sql_tips.my_very_long_table_name_that_is_much_too_long_for_a_postgres_table_name values (1, 'foo bar');
```

Running that works just fine, but it gives us a warning about some identfiers getting truncated. We can use the `pg_tables` system table to get information about the table that was actually created:

```sql
select * from pg_tables where schemaname = 'sql_tips';
```

Notice that the actual table name here is `my_very_long_table_name_that_is_much_too_long_for_a_postgres_ta`

Yet, we can still select rows from it using the full name (which will also get truncated):

```sql
select * from sql_tips.my_very_long_table_name_that_is_much_too_long_for_a_postgres_table_name;
```

But also notice that the second column is now `this_is_a_really_long_column_name_that_is_also_going_to_cause_u`. If we'd been doing this from python and expecting to get the full names back, we would have run into some real trouble!


## Getting information about tables, columns, and grants

**TIP #4 -- Get to know the postgres system tables**

Postgres provides several system tables that you can query to learn about different objects in the database. These can be handy when you're querying the database directly, but become particularly powerful when you're doing work programatically through python scripts. For instance, you can query `pg_tables` to find some basic information about tables in the system:

```sql
select * from pg_tables where schemaname = 'sql_tips';
```

What if I want to know about the columns in my tables? Check out `information_schema.columns`:

```sql
select * from information_schema.columns where table_schema = 'sql_tips';
```

That's pretty handy, but note that the schema here is referred to as `table_schema` rather than `schemaname` like it is in `pg_tables` (thanks, postgres!). Speaking of, if you want to get a list of schemas check out `pg_namespace` (why is this "pg_namespace" rather than "pg_schemas"? thanks, postgres!)

Sometimes it can be helpful to know about the permissions that have been granted on different tables as well, which you can do so using `information_schema.role_table_grants`:

```sql
select * from information_schema.role_table_grants rtg  where table_schema = 'sql_tips';
```

??? info "Shortcuts when using psql"

	`psql` has several shortcuts that you can use to help you quickly explore the database and learn about objects. Here are a couple quick pointers:
	
	- `\dn` will list the schemas in the database you're connected to
	- `\dt {schema_name}.*` will list the tables in schema `{schema_name}`
	- `\d {schema_name}.{table_name}` will list the columns of table `{schema_name}.{table_name}`
	- `\x` can be used to enter "extended display mode" to view results in a tall, key-value format
	- `\?` will show help about psql meta-commands
	- `\q` will exit


## Dealing with permissions and roles

**TIP #5 -- Don't forget to grant permissions to your teammates...**

A very common source of friction between teams collaborating in a database is forgetting to ensure that your teammates can see and use the table that you create. By default, new tables are both owned and only accessible by the user who created them. Try selecting from this table I created before the session:

```sql
SELECT * FROM sql_tips.can_you_see_me;
```

Oops! I forgot to grant permissions for the rest of you to access the table...

Fortunately, postgres allows for different users to share roles, and there's a common `food-inspections-role` that we all have access to, so I can grant permissions to everyone at once:

```sql
GRANT ALL ON sql_tips.can_you_see_me TO "food-inspections-role";
```

Note the double-quotes around the role since we used a hyphen in the role name (sorry!). Your groups all have similar shared roles (e.g., the database name with `-role` at the end).

Try to select from the table again. Does that work now? What happens if you try dropping the table?

Even though I gave you "ALL" permissions on the table, dropping it didn't work because only the role that owns the table can drop it. If you're not sure who owns a table, note that you can find out via `pg_tables`:

```sql
select * from pg_tables where schemaname = 'sql_tips' and tablename = 'can_you_see_me';
```

If I wanted to make sure you were able to drop the table as well, I might have been better off transferring ownership of the table to the shared role:

```sql
ALTER TABLE sql_tips.can_you_see_me OWNER TO "food-inspections-role";
```

Now we can check `pg_tables` again to confirm that the shared role owns the table. What happens if you try dropping it now?


**TIP #6 -- ...Or, use your group's role directly**

Another option for solving this problem is to run your queries as the shared role directly using the `SET ROLE` statement. Let's see what happens when I try this:

```sql
SET ROLE "food-inspections-role";
CREATE TABLE sql_tips.can_you_see_me as select * from raw.inspections limit 10;
```

Now check the ownership via `pg_tables` -- what do you see? What happens if you try querying from the table now?

Want to check what role you're currently using? Try `SELECT CURRENT_ROLE;`

Want to revert to your default role after setting a different one? Use `RESET ROLE;`


??? info "Setting default permissions"

	Postgres also provides an option setting default permissions that will be applied to various objects you create in the database (or a given schema) so you don't have to remember to either run grants or switch into the group role whenever you create new tables. Check out the syntax for the [ALTER DEFAULT PRIVILEGES statement](https://www.postgresql.org/docs/13/sql-alterdefaultprivileges.html) if you'd like to learn more. Sadly, postgres doesn't provide a means for transferring ownership of new objects created by default to another role (of course, it's an open source project, so feel free to open a pull request...)


## Improving the performance of your queries

**TIP #7 -- Avoid UPDATE statements, especially on large tables**

Although the SQL standard provides a mechanism for modifying the data in a table in place using the `UPDATE` statement, the implementation of these queries is terribly inefficient and you'll find that it is often much faster in practice to create a new table and select the data from the old table into it with the transformations you're trying to do (then you can swap the new table in for the old by changing the names of both using `ALTER TABLE` statements).


**TIP #8 -- Use EXPLAIN to understand query plans**

You can get some insight into how the query optimizer is going to run your query by adding `EXPLAIN` to the front of the statement. Rather than actually running the query, this will return some (somewhat inscrutible) information about the query plan that can give you an idea of 1) how long the query might take to run and 2) which indices would make things faster. Give this a try:

```sql
EXPLAIN SELECT * FROM clean.inspections WHERE encounter = '201410290023';
```

Notice that picking out a specific inspection record from the clean table is making use of an index via `Index Scan` that lets it very quickly find rows associated with a specific value. By contrast, try running:

```sql
EXPLAIN SELECT * FROM sql_tips.violations_big WHERE encounter = '201410290023';
```

Here, `Seq Scan` tells us that postgres has to scan the entire table to find the right records, which can be very expensive (especially with joins!). Also note how much higher the overall estimated cost is for this query in the first row here than for the query above.

Likewise, running `EXPLAIN` for joins can give you information about the type of join that will be used and how (or if) your tables' indices in running the query. Try running:

```sql
EXPLAIN SELECT * FROM sql_tips.inspections LEFT JOIN sql_tips.violations_big USING(encounter);
```

In general, merge joins will be faster than hash joins which will be faster than nested loop joins ([see the docs](https://www.postgresql.org/docs/current/planner-optimizer.html) for much more detail). The `EXPLAIN` output gives a ton of information and don't worry about understanding all of it -- generally focusing on the relative "cost" values, the types of joins, and types of scans can give you plenty of help in understanding why your query is slow.


**TIP #9 -- Optimize your queries with indices**

We briefly mentioned indices above, but let's take a closer look at what they are, how they can improve your queries, and how to use them. In simple terms, you can think of an index as a big, sorted lookup table that lets the database map from given values for a column (or set of columns) to the rows that contain those values. In doing so, the can make retrieving specific records or joining on those values much, much more efficient. However, the trade-off you make with creating indices is that they can greatly increase the storage space for your tables (as well as the time required when inserting new data, which also need to be added to the indices), so you do need to be somewhat deliberate about the indices you create.

*In general, if your query is running for a long time, the most likely culprit is lack of an index. Create indices often and early but be deliberate about selecting the columns that you think you'll be (or are) using frequently in joins or where clauses.*

Let's look at an example. Remember how running `EXPLAIN` on the `SELECT` statement from `sql_tips.violations_big` told us it was going to use a `Seq Scan` to pick out the record. Let's actually try running that query:

```sql
SELECT * FROM sql_tips.violations_big WHERE encounter = '201410290023';
```

That probably took a few seconds -- not terrible, but can certainly add up if we're running that query over and over again or doing a big join on the `encounter` column. Let's see what happens if we add an index:

```sql
CREATE INDEX ON sql_tips.violations_big(encounter);
```

Now try running your `EXPLAIN` again:

```sql
EXPLAIN SELECT * FROM sql_tips.violations_big WHERE encounter = '201410290023';
```

Note that the query planner now realizes there's an index it can use to find the records you want much more quickly. Try actually running the select again -- how long does it take now?

In the special case that you know records in your table will always be uniquely identified by certain value, you can set a *primary key*, which acts like an index but also tells the database it can stop looking for records after it finds a single value on the key (making things even a bit faster). We know this is true for the `encounter` field on the `sql_tips.inspections` table, so let's add one there:

```sql
ALTER TABLE sql_tips.inspections ADD PRIMARY KEY (encounter);
```


## How to kill hung or run-away queries

**TIP #10 -- Kill your run-away queries to free up resources**

Even if your tables are well-indexed, you may still end up with queries that run longer than you'd like or bugs that unintentionally create massive joins. If you think one of your queries has hung (or is taking far longer or many more resources than it should), you can run the following query to confirm that it is still running:
```sql
SELECT * FROM pg_stat_activity;
```

If you need to kill your query, you can note down the PID from that result and then use the following query to kill it:
```sql
SELECT pg_cancel_backend({PID});
```
After running that, it's a good idea to check `pg_stat_activity` again to ensure it's been killed. Sometimes that may not work, and you need to use the more aggressive command:
```sql
SELECT pg_terminate_backend({PID});
```

!!! important "Canceling execution in your SQL GUI doesn't do this for you!"

	Note that hitting the "Stop" or "Cancel" button in your GUI SQL interpreter (e.g., dbeaver, datagrip, or dbvisualizer) generally won't actually cancel the query execution on the database server itself. If you try to cancel a long-running query on your front-end, be sure to check `pg_stat_activity` to confirm it's actually been killed and use one of the commands above to stop the execution on the server if neccessary.


## Bonus Tips

1. The atomic swap is a good pattern for ingesting updated data: load the new data into `{table_name}_staging` and then (in a single transaction) drop (if one exists) `{table_name}_old`, rename the current table to `{table_name}_old`, and rename the staging table to `{table_name}`. This both avoids a gap in the table being available and always preserves the previous version of the table if something has gone wrong and the process needs to be rolled back.

2. Postgres has pretty extensive built-in functionality for handling JSON data, arrays, regular expressions, doing range joins, etc, as well as extensions for dealing with data that's geographic in nature. We don't have time to delve into all of this functionality here, but you can find good tutorials and documentation online for all of them.

3. Subqueries will generally be pretty inefficient. If you're building up a complex query, you'll usually be better off either with [CTEs](http://www.craigkerstiens.com/2013/11/18/best-postgres-feature-youre-not-using/) or building up pieces with temporary tables (which, in turn, can be indexed as well).

4. Using psql and annoyed by wrapping lines creating difficult-to-read outputs? Try setting the `PAGER` environment variable, when starting `psql` (then you'll be able to use your left and right arrow keys to navigate wide outputs):
```
$ PAGER='less -S' psql -h db.dssg.io -U {andrew_id} {database_name}
```
