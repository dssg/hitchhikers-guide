
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


## Improving the performance of your queries


## How to kill hung or run-away queries


## Tips

3. If your query is running for a long time, the most likely culprit is lack of an index. Create indices often and early but be deliberate about selecting the columns that you think you'll be (or are) using frequently in *joins* or *where* clauses.

4. (Advanced Tip) Use EXPLAIN to get a query execution plan to get an idea of 1) how long the query might take to run and 2) which indices would make things faster.

5. Don't do *UPDATE* queries (on large table). UPDATEs are horribly inefficient and it's often faster to create a new table and select the data from the old table into it with the transformations you're trying to do with the update statement.

6. Set up permissions for your team (using GRANT) so you don't get them annoyed and frustrated when they can't access a table or schema you've created.


## Bonus Tips

1. The atomic swap is a good pattern for ingesting updated data: load the new data into `{table_name}_staging` and then (in a single transaction) drop (if one exists) `{table_name}_old`, rename the current table to `{table_name}_old`, and rename the staging table to `{table_name}`. This both avoids a gap in the table being available and always preserves the previous version of the table if something has gone wrong and the process needs to be rolled back.

2. Postgres has pretty extensive built-in functionality for handling JSON data, arrays, regular expressions, doing range joins, etc, as well as extensions for dealing with data that's geographic in nature. We don't have time to delve into all of this functionality here, but you can find good tutorials and documentation online for all of them.

3. Using psql and annoyed by wrapping lines creating difficult-to-read outputs? Try setting the `PAGER` environment variable, when starting `psql` (then you'll be able to use your left and right arrow keys to navigate wide outputs):
```
$ PAGER='less -S' psql -h db.dssg.io -U {andrew_id} {database_name}
```
