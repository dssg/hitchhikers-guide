# CSVs to the Database

## Motivation
This summer, you will use a database to hold, manipulate, and analyze data. Databases have several advantages over using source files such as CSVs:

* We're collecting more and more data -- often too much to fit in memory. Most databases can handle this. 
* We're collecting more complex data. For example, there are databases that efficiently store and manipulate text and causal relationships. 
* Databases can provide integrity checks and guarantees. If you have a column of numbers in a spreadsheet, Excel will let you change a random cell to text. In contrast, you can tell your database to only accept input that meets your conditions (e.g. type, uniqueness). This is especially important for ongoing projects, where you have new data coming in.
* Databases allow you to store data in one place. That makes updates easy and reliable. 
* Databases are more secure. You can more carefully control who has which types of access to what data better in a database than with a CSV.
* Databases can handle multiple users. Concurrent edits to a CSV can get messy. Some file systems won't even let multiple users access a CSV at the same time.

This session builds on what you learned last week in the [pipeline](https://github.com/dssg/hitchhikers-guide/tree/master/curriculum/pipelines-and-project-workflow) and [command line](https://github.com/dssg/hitchhikers-guide/tree/master/curriculum/command-line-tools) sessions. We will focus on ETL. 


## Potential Teachouts
* Other types of databases (e.g. NoSQL, graph)


## Tools
* psql (command line)
* dBeaver
* csvkit


## Basic Database Lingo
* *Database server*: the computer on which the database is running. We use Amazon RDS as our server.
* *Database*: a self-contained set of tables and schema. A server can run many databases. This summer, we will operate databases for almost all projects from the same Amazon server.
* *Schema*: similar to a folder. A database can contain many schema, each containing many tables.
* *Tables*: tables are like spreadsheets. They have rows and columns and values.



## Let's Rock Some Data!

### Two ways to connect to the database
You cannot access the database server directly; you have to go through one of our EC2s. The data are far safer that way: you have to use your private key (better than a password) to access the EC2 and then a password to access the database. 

There are two ways to connect to the database:

1. *Connect from your laptop*: You use an SSH tunnel to pass data between your laptop and the database. You have a database program running locally. If you're using dBeaver, you're connecting from your laptop.
![Connect from your laptop](https://www.lucidchart.com/publicSegments/view/0a5f49d0-d66c-4ef3-90eb-f7e037d20ec3/image.png)
2. *Connect from the EC2*: You SSH into the EC2 and run everything from there. Your laptop only sends your commands to the EC2; the EC2 does the work. You don't use an SSH tunnel because everything stays on the EC2.
![Connect from the EC2](https://www.lucidchart.com/publicSegments/view/9ca0e0f9-da92-468a-935c-b1fc1d3d467a/image.png)

You can use option 1 (especially dBeaver) to explore the data, but you should use option 2 to load the data. First, downloading the datasets to your laptop may violate our contracts. Second, the internet connections will be better. The connections within Amazon are pretty fast; the connections from our office to Amazon might not be. Option 2 keeps the heavy transfers on Amazon's systems. 


### Let's get the structure of the data

In this session, we will put the weather data from last week's command-line session into the DSSG training database.

Start by SSHing into the training server:
`ssh -i ~/.ssh/your_private_key your_username@the_training_EC2_address`

If you haven't already, download Matt's weather data to your training folder directory on the training server and unzip, e.g.:

1. `cd /mnt/data/training/jwalsh/`
2. `curl -O ftp://ftp.ncdc.noaa.gov/pub/data/ghcn/daily/by_year/2016.csv.gz`
3. `gunzip 2016.csv.gz`

This gives you a file called `2016.csv`. You can explore the data using `head`, `tail`, `csvlook`, and other tools that Matt taught you.

Here's the output from `csvlook`:
![alt text](https://github.com/dssg/hitchhikers-guide/blob/master/curriculum/csv-to-db/weather_data_csvlook_output.png "weather data")

The first weird thing I see when I look at the data: no headers. `csvlook -H` makes it easier to read:
![alt text](https://github.com/dssg/hitchhikers-guide/blob/master/curriculum/csv-to-db/weather_data_csvlook_noheader_output.png "weather data") 

The README tells us that 
* Column 1 is the station identifier
* Column 2 is the date (yyyymmdd)
* Column 3 is the value type (e.g. "PRCP" is precipitation)
* Column 4 is the value
* Column 5 is the "character Measurement Flag," whatever that means
* Column 6 is the "1 character Quality Flag," whatever that means
* Column 7 is the "1 character Source Flag," whatever that means
* Column 8 is the time (hhmm)

Most of the files you work with have a header, so I'll add one here:

`
Station,Date,Value Type,Value,Measurement Flag,Quality Flag,Source Flag,Time
`


Here's the new `csvlook`:
![alt text](https://github.com/dssg/hitchhikers-guide/blob/master/curriculum/csv-to-db/weather_data_csvlook_header_output.png "weather data") 

`csvsql` generates `create table` statements for you. Because it uses Python, it will load all the data and then do its thing. To limit the resources it needs, I'll only use the first 1000 rows. We're using a PostgreSQL ("Postgres") database:

`
head -n 1000 2016.csv | csvsql -i postgresql
`

Here's the output:

```
CREATE TABLE stdin (
    "Station" VARCHAR(11) NOT NULL, 
    "Date" INTEGER NOT NULL, 
    "Value Type" VARCHAR(4) NOT NULL, 
    "Value" INTEGER NOT NULL, 
    "Measurement Flag" VARCHAR(4), 
    "Quality Flag" VARCHAR(4), 
    "Source Flag" VARCHAR(1) NOT NULL, 
    "Time" VARCHAR(4)
);
```

A few things to note:
* Station, Date, etc. are column names.
* VARCHAR and INTEGER are column types. VARCHAR(11) means variable character length column up to 11 characters. If you try to give a character column a number, an integer column a decimal, and so on, Postgres will prevent the entire transfer. 
* NOT NULL means you have to provide a value for that column.
* Postgres hates uppercase and spaces in column names. If you have either, you need to wrap the column name in quotation marks. Yuck.
* We need to replace `stdin` with the table name (`jwalsh_schema.jwalsh_table`). 
* A common problem: funky (non-unicode) characters often appear in the source files. While that's not true here, you can fix many of them using `iconv`.

Let's give it another shot:

`
head -n 1000 2016.csv | iconv -t ascii | tr [:upper:] [:lower:] | tr ' ' '_' | csvsql -i postgresql
`

* `iconv -t ascii` attempts to output ascii. It can also help to use the `-f` option, which gives `iconv` the format of the input.
* `tr [:upper:] [:lower:]` converts all uppercase to all lowercase. 
* `tr ' ' '_'` converts all spaces to underscores.
* `csvsql -i postgresql` generates the postgres `create table` statement.

Here's the output:

```
CREATE TABLE stdin (
    station VARCHAR(11) NOT NULL, 
    date INTEGER NOT NULL, 
    value_type VARCHAR(4) NOT NULL, 
    value INTEGER NOT NULL, 
    measurement_flag VARCHAR(4), 
    quality_flag VARCHAR(4), 
    source_flag VARCHAR(1) NOT NULL, 
    time VARCHAR(4)
);
```

`csvsql` ain't perfect. We still need to make some changes:
* Replace `stdin` with the table name: `jwalsh_schema.jwalsh_table`.
* `date` is listed as an integer. It should be `date`.



### Let's create the schema and table
Remember, the schema is like a folder. You can use schema to categorize your tables. In dBeaver:

```
CREATE SCHEMA jwalsh_schema;

CREATE TABLE jwalsh_schema.jwalsh_table (
    station VARCHAR(11) NOT NULL, 
    date DATE NOT NULL, 
    value_type VARCHAR(4) NOT NULL, 
    value INTEGER NOT NULL, 
    measurement_flag VARCHAR(4), 
    quality_flag VARCHAR(4), 
    source_flag VARCHAR(1) NOT NULL, 
    time VARCHAR(4)
);
```

### Let's copy the data
We are ready to copy the data! We strongly recommend using `psql`. You can do it through Python scripts and other methods, but `psql` is optimized for this task. It will likely save you a lot of time.

We should follow [Jen's guidelines](https://github.com/dssg/hitchhikers-guide/tree/master/curriculum/1_getting_and_keeping_data/data-security-primer) by storing the database credentials in a file. Postgres looks for four environment variables: PGHOST, PGUSER, PGPASSWORD, and PGDATABASE. To set the environment variables using `default_profile.example`:

`
eval $(cat default_profile.example)
`

`
cat 2016.csv | psql -c "\copy jwalsh_schema.jwalsh_table from stdin with csv header;"
`

Note: You want to pipe the data from `cat` to `psql`. You'll get a permissions error if you don't.


### Let's look at the data
Use dBeaver!

```
select * from jwalsh_schema.jwalsh_table limit 25;
select count(*) from jwalsh_schema.jwalsh_table;
select * from jwalsh_schema.jwalsh_table where station = 'USW00094846';
select * from jwalsh_schema.jwalsh_table where station = 'USW00094846' and value_type = 'PRCP';
```


## Further Resources
* Software Carpentry: [Databases and SQL](http://swcarpentry.github.io/sql-novice-survey/)
* [Computation for Public Policy, Harris School of Public Policy](https://computationforpolicy.github.io/slides/08.pdf)



## Discussion Notes


