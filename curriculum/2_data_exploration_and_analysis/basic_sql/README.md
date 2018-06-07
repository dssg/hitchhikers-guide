# Intro to SQL

You've already used databases. Excel spreadsheets are a simple example. But those databases have many problems, such as 

* size of data you can use is limited by RAM
* cannot handle complex data (there are databases to handle more complex data types, e.g. documents)
* difficult to use data from multiple tables/sheets
* no data integrity guarantees (you can accidentally put a letter in a numeric column and the entire column will become a character column)
* it's difficult for multiple people to use the spreadsheet at the same time. If one person updates sheet A and another person updates sheet B, integrating both updates gets ugly.


Things to cover:

* `select`
* `from`
* `limit` (Postgres)
* `where`
* `group by`
* `order by`
* joins

**So, let's get into it, shall we!?**

First, we'll need to:

* ssh into the server
* Run  `psql`
* Run `SET ROLE training_write` so that we have the appropriate permissions

### Getting a sense of the tables and data:

A few things we can do to explore:

* Look at the schemas currently present; make sure yours is there: `\dn`
* List databases: `\l`
* Find the count of the list of rows:
  
  `SELECT COUNT(*) FROM mpettit_schema.mpettit_table;`
* Output the list of columns for this table:
  
  `SELECT column_name
   FROM information_schema.columns
   WHERE table_name = 'mpettit_table';`
* If you also want to look at datatype:
   
   `SELECT column_name, data_type
   FROM information_schema.columns
   WHERE table_name = 'mpettit_table';`
   
Ok, now that we've gotten a sense of the data, let's dial it back and get to the basics. :)

### Select
Now, let's look a bit more into SELECT. The SELECT statement is used to select data from a database. The data returned is stored in a result table, called the result-set.

In SQL, data is usually organized in various tables. For example, a sports team database might have the tables teams, players, and games. A wedding database might have tables guests, vendors, and music_playlist. 

First off, let's select everything from the table to see what we get:

`SELECT * FROM mpettit_schema.mpettit_table;`

There's a lot to view at once here. Let's say we're not interested in all those comments and just want to look at the columns `inspection_id`, `dba_name`, `aka_name`, `results`, and `inspection_date`. We can edit the above command to only select those columns:

`SELECT inspection_id, dba_name, aka_name, results, inspection_date FROM mpettit_schema.mpettit_table;`

### Where 

The WHERE clause is used to filter records. That is, the WHERE class extracts only those records that fulfill a specified condition.



