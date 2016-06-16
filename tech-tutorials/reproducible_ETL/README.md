# Reproducible ETL

## Motivation
* *Understanding what you did*: Save all the steps you took so you can tell how you got here. 
* *Using what you did*: Use and re-use code for this project or for others. Fix errors easily. Import new data with confidence. GET IT IMPLEMENTED!

This session builds on what you learned last week in the [CSV to DB](https://github.com/dssg/hitchhikers-guide/tree/master/tech-tutorials/csvtodb) session.


## Potential Teachouts
* Proprietary-database transfers (e.g. SQL Server, Oracle) 
 

## Concepts
Many people associate data science with fancy machine-learning algorithms, but ETL is arguably more important.

ETL: 

1. *Extract*: Get data from the source, e.g. a CSV the partner gave you.
2. *Transform*: Get the data into the format you want/need, e.g. standardize missing values.
3. *Load*: Get the data into the database.

There are two reasons why ETL matters so much:

1. The rest of your analysis depends on your ETL. For example, [you might ignore some of the most important cases if you drop rows with missing values](http://www.stabilityjournal.org/articles/10.5334/sta.cr/). 
2. Better data tends to trump better methods.

So you should do ETL well:
* Reliably
* Understandably
* Preferably automatically

Tools:
* Code is typically better than GUIs. Code can be automated.
* All else being equal, command-line tools are good choices. They are time tested and efficient.
* make
* [drake](https://github.com/Factual/drake)
* If you can't save the code, save the notes, e.g. record how you used Pentaho to transfer an Oracle database to Postgres.


## Examples

### Hitchhiker's Guide Weather Example
Remember the weather example from last week? Let's make sure it's reproducible. I stored the code in two files:
* `jwalsh_table.sql` drops `jwalsh_schema.jwalsh_table` if it exists, creates the table using our statement from the CSV-to-DB session, then copies the data.
* `Drakefile` downloads the weather data, unzips it, then calls `jwalsh_table.sql`

To run it, make sure you specify the Postgres environment variables in `default_profile`, then type `drake` while in this directory.

I've run this code many times without error, and I feel pretty confident that it will continue to run without error for a while.

Because we've written some decent ETL code, we can borrow it for this project. Some of this code originated with the lead project.

Let's say NOAA changes the format of the weather file. This code will throw an error when we try to run it. We can simply modify `jwalsh_table.sql` to match the new format, re-run the code without error, and enjoy the up-to-date data. 


### Lead Project
Well-developed ETL in `input/`. 

### Sanergy Project
`input/Drakefile` calls an R script. The repository is [here](https://github.com/dssg/sanergy).

### What If You Have to Use Points and Clicks?
See last year's police team [Oracle directions](https://github.com/dssg/police/tree/master/input/cmpd/oracle_export_code).

## Discussion

