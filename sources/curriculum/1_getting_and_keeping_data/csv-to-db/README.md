# Getting Data into a Database

## Motivation
This summer, you will use a database to store and analyze data. Databases have several advantages over using text files such as CSVs or Excel files:

* Databases can store information about relationships between tables.
* We're collecting more and more data -- often too much to fit in memory. Most databases can handle this in a more efficient manner. 
* Databases can provide integrity checks and guarantees. If you have a column of numbers in a spreadsheet, Excel will let you change a random cell to text. In contrast, you can tell your database to only accept input that meets your conditions (e.g. type, uniqueness). This is especially important for ongoing projects, where you have new data coming in.
* Databases allow you to store data in one place. That makes updates easy and reliable. 
* Databases are more secure. You can more carefully control who has which types of access to what data better in a database than with a CSV.
* Databases can handle multiple users. Concurrent edits to a CSV can get messy. Some file systems won't even let multiple users access a CSV at the same time.
* Databases are designed to help you do analysis. SQL will probably become your best (non-human) friend this summer.

You'll likely have to load CSVs (or excel files) into your database (e.g. from the open data portal), even if your partner gave a database dump ([which is ideal](https://dsapp.uchicago.edu/home/resources/give-us-direct-access-system-database-dump/)). This session builds on what you learned last week in the [pipeline](https://github.com/dssg/hitchhikers-guide/tree/master/curriculum/0_before_you_start/pipelines-and-project-workflow) and [command line](https://github.com/dssg/hitchhikers-guide/tree/master/curriculum/1_getting_and_keeping_data/command-line-tools) sessions. We will focus on ETL. 


## Tools
* psql (command line)
* [dBeaver](https://dbeaver.io/)
* [csvkit](https://github.com/wireservice/csvkit)
* [ohio](https://github.com/dssg/ohio)

Notice that we're not using pandas. DO NOT COPY DATA INTO THE DATABASE USING PANDAS. We strongly recommend using `psql`, which is orders of magnitude faster.


## Basic Database Lingo
* *Database server or host*: the computer on which the database is running. We will use Amazon RDS.
* *Database*: a self-contained set of tables and schema. A server can run many databases. This summer, we will operate databases for almost all projects from the same Amazon server.
* *Schema*: similar to a folder. A database can contain many schema, each containing many tables.
* *Tables*: tables are like spreadsheets. They have rows and columns and values in each cell.
* *Views*: views are virtual tables created by a query but only instantiated when the query is run. They can be used as tables but are generated "on-demand" when they're used. An advantage is that they always contain the most current data but take time to compute.
* *Queries*: Queries are analysis that you run on a database, often in SQL.


## Let's Rock Some Data!

### Connecting to the database
Some unique aspects of the setup at DSSG: You cannot access the database server directly; you have to connect to the University's secure network and tunnel go through one of the EC2 instances. The data are far safer that way: you have to access the University's secure network, then one of our EC2s, and then the database. 

There are two ways to connect to the database (once you're on the University network):

1. *Connect from your laptop*: Use an SSH tunnel to pass data between your laptop and the database. You have a database program running locally. If you're using dBeaver, you're connecting from your laptop.
![Connect from your laptop](https://www.lucidchart.com/publicSegments/view/0a5f49d0-d66c-4ef3-90eb-f7e037d20ec3/image.png)
2. *Connect from the EC2*: SSH into the EC2 and run everything from there. Your laptop only sends your commands to the EC2; the EC2 does the work. You don't use an SSH tunnel because everything stays on the EC2.
![Connect from the EC2](https://www.lucidchart.com/publicSegments/view/9ca0e0f9-da92-468a-935c-b1fc1d3d467a/image.png)

You can use option 1 (especially dBeaver) to explore the data, but you should use option 2 to load the data. First, downloading the datasets to your laptop may violate our contracts. Second, the internet connections will be better. The connections within Amazon are pretty fast; the connections from our office to Amazon might not be. Option 2 keeps the heavy transfers on Amazon's infrastructure. 

### Getting data into a Database
There are three steps to get a CSV into an existing database:
1. **Create table**: This involves figuring out the structure of the table (how many fields, what should they be called, and what data types they are). Once you figure out the structure, you can create a sql "CREATE TABLE" statement and run that to generate an *empty* table*
2. **Copy CSV to the table**: Every database has a "bulk" copy command that is **much** more efficient than using pandas. Please do not use pandas to copy large csvs to a database. Postgres has a COPY command that can now copy your csv to the table you just created. 
3. **Check if it copied successfully**: You want to check if your table now has the same number of rows and columns as the CSV (as well as other consistency checks). If it did not copy successfully, you may need to modify the table structure, clean the csv to remove characters, replace nulls, and try steps 1 and 2 again.

### Step 1: Let's get the structure of the data

In this session, we will put the City of Chicago's food-inspection data into the DSSG training database.

Start by SSHing into the training server:
`ssh your_username@the_training_EC2_address`

Create a folder for yourself in the EC2 training directory and download the data:

1. `cd /mnt/data/projects/training/`
2. `mkdir jwalsh`
3. `cd jwalsh`
4. `wget -O inspections.csv https://data.cityofchicago.org/api/views/4ijn-s7e5/rows.csv?accessType=DOWNLOAD`

This gives you a file called `inspections.csv`. You can explore the data using `head`, `tail`, `csvlook`, and other command-line tools you've learned in previous sessions.

Here's the output from `csvlook`:
![alt text](https://raw.githubusercontent.com/dssg/hitchhikers-guide/master/curriculum/1_getting_and_keeping_data/csv-to-db/inspections_data_csvlook.png "inspections data")

`csvsql` generates `create table` statements for you. Because it uses Python, it will load all the data and then do its thing. That can be really inefficient for large datasets: you have to wait to read the entire dataset, and you need lots of memory to do it. To limit the resources csvsql needs, I'll only use the first 1000 rows. We're using a PostgreSQL ("Postgres") database:

`
head -n1000 inspections.csv | csvsql -i postgresql
`

Here's the output:

```
CREATE TABLE stdin (
	"Inspection ID" DECIMAL NOT NULL, 
	"DBA Name" VARCHAR NOT NULL, 
	"AKA Name" VARCHAR, 
	"License #" DECIMAL NOT NULL, 
	"Facility Type" VARCHAR, 
	"Risk" VARCHAR, 
	"Address" VARCHAR NOT NULL, 
	"City" VARCHAR NOT NULL, 
	"State" VARCHAR, 
	"Zip" DECIMAL NOT NULL, 
	"Inspection Date" DATE NOT NULL, 
	"Inspection Type" VARCHAR NOT NULL, 
	"Results" VARCHAR NOT NULL, 
	"Violations" VARCHAR, 
	"Latitude" DECIMAL, 
	"Longitude" DECIMAL, 
	"Location" VARCHAR
);
```

A few things to note:
* Inspection ID, DBA Name, AKA Name, etc. are column names.
* VARCHAR and INTEGER are column types. VARCHAR(11) means variable character length column up to 11 characters. If you try to give a character column a number, an integer column a decimal, and so on, Postgres will prevent the entire transfer. 
* NOT NULL means you have to provide a value for that column.
* Postgres hates uppercase and spaces in column names. If you have either, you need to wrap the column name in quotation marks. Yuck.
* We need to replace `stdin` with the table name (`jwalsh.jwalsh`). 

Let's give it another shot:

`
head -n 1000 inspections.csv | tr [:upper:] [:lower:] | tr ' ' '_' | sed 's/#/num/' | csvsql -i postgresql --db-schema jwalsh --tables jwalsh
`

* `tr [:upper:] [:lower:]` converts all uppercase to all lowercase. 
* `tr ' ' '_'` converts all spaces to underscores.
* `sed 's/#/num/'` replaces the pound sign with "num".
* `csvsql -i postgresql --db-schema jwalsh --tables jwalsh` generates the postgres `create table` statement.

Here's the output:

```
CREATE TABLE jwalsh.jwalsh (
	inspection_id DECIMAL NOT NULL, 
	dba_name VARCHAR NOT NULL, 
	aka_name VARCHAR, 
	license_num DECIMAL NOT NULL, 
	facility_type VARCHAR, 
	risk VARCHAR, 
	address VARCHAR NOT NULL, 
	city VARCHAR NOT NULL, 
	state VARCHAR, 
	zip DECIMAL NOT NULL, 
	inspection_date DATE NOT NULL, 
	inspection_type VARCHAR NOT NULL, 
	results VARCHAR NOT NULL, 
	violations VARCHAR, 
	latitude DECIMAL, 
	longitude DECIMAL, 
	location VARCHAR
);
```

`csvsql` ain't perfect. We could still make changes if we wanted, e.g. changing the `license_num` column type. But DECIMAL is good enough for this exercise. 

### Let's create the schema and table
Remember, the schema is like a folder. You can use schema to categorize your tables. Let's use a script, which I'll call `inspections.sql`, to create the schema and table. Here's what it looks like:

```
SET ROLE training_write;

CREATE SCHEMA IF NOT EXISTS jwalsh;

CREATE TABLE IF NOT EXISTS jwalsh.jwalsh (
	inspection_id DECIMAL NOT NULL, 
	dba_name VARCHAR NOT NULL, 
	aka_name VARCHAR, 
	license_num DECIMAL NOT NULL, 
	facility_type VARCHAR, 
	risk VARCHAR, 
	address VARCHAR NOT NULL, 
	city VARCHAR NOT NULL, 
	state VARCHAR, 
	zip DECIMAL NOT NULL, 
	inspection_date DATE NOT NULL, 
	inspection_type VARCHAR NOT NULL, 
	results VARCHAR NOT NULL, 
	violations VARCHAR, 
	latitude DECIMAL, 
	longitude DECIMAL, 
	location VARCHAR
);
```

A few things to note:
* The first row sets the role. You need to assume a role that has write permissions to create schemas and tables and to copy data.
* I added `IF NOT EXISTS` conditions for `create schema` and `create table`. You don't need those if you run the script once, but if you run the script multiple times, you'll get errors if those already exist.
* The `create table` statement is from above.


### Step 2: Let's copy the data

All you've given the database to this point is a schema and an empty table. Use psql's `\copy` command to get data into the table: `\copy [db table] from '[source CSV]' with csv header`. I'll add it to the `inspections.sql` script:
```
SET ROLE training_write;

CREATE SCHEMA IF NOT EXISTS jwalsh_schema;

CREATE TABLE jwalsh_schema.jwalsh_table (
        inspection_id DECIMAL NOT NULL,
        dba_name VARCHAR NOT NULL,
        aka_name VARCHAR,
        license_num DECIMAL NOT NULL,
        facility_type VARCHAR,
        risk VARCHAR, 
        address VARCHAR NOT NULL,
        city VARCHAR NOT NULL,
        state VARCHAR,  
        zip DECIMAL NOT NULL,
        inspection_date DATE NOT NULL,
        inspection_type VARCHAR NOT NULL,
        results VARCHAR NOT NULL,
        violations VARCHAR,
        latitude DECIMAL,
        longitude DECIMAL,
        location VARCHAR
);

\COPY jwalsh_schema.jwalsh_table from 'inspections.csv' WITH CSV HEADER;
```

To run the script securely, follow these [data security guidelines](https://github.com/dssg/hitchhikers-guide/tree/master/curriculum/1_getting_and_keeping_data/data-security-primer) by storing the database credentials in a file. Postgres looks for four environment variables: PGHOST, PGUSER, PGPASSWORD, and PGDATABASE. To set the environment variables using default_profile (copy and modify from `default_profile.example`):

`
eval $(cat default_profile)
`

Then
`
psql -f inspections.sql
`

Uh oh, we got an error:
```
Password for user jwalsh: 
SET
psql:copy_example.sql:2: ERROR:  null value in column "city" violates not-null constraint
DETAIL:  Failing row contains (2145008, INTERURBAN, INTERURBAN, 2492070, Restaurant, Risk 1 (High), 1438 W CORTLAND ST , null, null, 60642, 2018-02-15, License, Pass, null, 41.916996072966775, -87.6645967198223, (41.916996072966775, -87.6645967198223)).
CONTEXT:  COPY jwalsh_table, line 7960: "2145008,INTERURBAN,INTERURBAN,2492070,Restaurant,Risk 1 (High),1438 W CORTLAND ST ,,,60642,02/15/201..."
```

With Postgres `copy`, either the entire copy is successful or none of it is. Check your table: nothing is there. I'll modify `inspections.sql` to allow missing values and try again:
```
SET ROLE training_write;

CREATE SCHEMA IF NOT EXISTS jwalsh_schema;

DROP TABLE IF EXISTS jwalsh_schema.jwalsh_table;

CREATE TABLE jwalsh_schema.jwalsh_table (
        inspection_id DECIMAL,
        dba_name VARCHAR,
        aka_name VARCHAR,
        license_num DECIMAL,
        facility_type VARCHAR,
        risk VARCHAR,
        address VARCHAR,
        city VARCHAR,
        state VARCHAR,
        zip DECIMAL,
        inspection_date DATE,
        inspection_type VARCHAR,
        results VARCHAR,
        violations VARCHAR,
        latitude DECIMAL,
        longitude DECIMAL,
        location VARCHAR
);

\COPY jwalsh_schema.jwalsh_table from 'inspections.csv' WITH CSV HEADER;
```

Run the script:
`
psql -f inspections.sql
`


### Step 3: Let's look at the data and make sure everything is there
Check if the data are there. Here's what it looks like in dBeaver:

![alt text](https://raw.githubusercontent.com/dssg/hitchhikers-guide/master/curriculum/1_getting_and_keeping_data/csv-to-db/data_inserted_into_table.png "data inserted")


## Further Resources
* Software Carpentry: [Databases and SQL](http://swcarpentry.github.io/sql-novice-survey/)



## Discussion Notes


