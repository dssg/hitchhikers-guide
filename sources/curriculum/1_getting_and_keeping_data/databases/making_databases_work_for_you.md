
# Making databases work for you

## Motivation
Databases are great for dealing with large amounts of data in an efficient manner. We'll use databases (typically postgres) all summer for almost all of our projects. While you'll find them to be your new best friend, you're likely to get frustrated and annoyed  with them (just as you would with any best friend) if you don't set things up correctly up front. Here are some things to keep in mind that you should do early on to reduce your frustration and annoyance as you get to know each other better:

## Tips

1. Don't mix upper and lower case for table and column names. Postgres is case-sensitive and you don't want to spend time typing double quotes (or forgetting to do so) every tiome type out a table or column name. **Stick to all lowercase table and column names when you can**

2. Don't use special characters in table names or start with a digit. Same reason as #1.

3. if your query is running for a long time, the most likely culprit is lack of an index. Create indices often and early but be deliberate about selecting the columns that you think you'll be (or are) using frequently in *joins* or *where* clauses.

4. (Advanced Tip) Use EXPLAIN to get a query execution plan to get an idea of 1) how long the query might take to run and 2) which indices would make things faster.

5. Don't do *UPDATE* queries (on large table). UPDATEs are horribly inefficient and it's often faster to create a new table and select the data from the old table into it with the transformations you're trying to do with the update statement.

6. Set up permissions for your team (using GRANT) so you don't get them annoyed and frustrated when they can't access a table or schema you've created.


## Bonus Tips


