# Python and SQL 

## Objectives of the session

1. Connect to the db through Python and SQLAlchemy 
2. Execute queries directly through python with SQLAlchemy (no Pandas)
3. Template SQL 
4. Upload data with psql 

Before we start you will need to: 

+ Connect into your project server

```
$ ssh -i /path/to/your/privatekey andrewid@yourprojectserver.dssg.io
```

+ On your project server, source your `.bashrc` so that python can load your
 environment
 variables 

```
$ source ~/.bashrc
```

+ On your project server, go to the `mnt` directory 

```
$ cd /mnt/data/projects/your-projectanme/andrewid/
```

+ On your project server, start your jupyter lab on your port (check
 availability with `ss -tulnp`)

```
$ jupyter lab --port 9999
```

+ On your local machine, create a port forward -tunneling- to the jupyter lab

```
$ ssh -i /path/to/your/private/key -NL localhost:9999:localhost:9999 andrewid
@yourprojectserver.dssg.io
```

+ Open a tab on your browser using the URL from the server. Remember to
 change your port with the one that you put on the first part of the port
  forwarding.

```
localhost:9999/?token=somenumbersanddigits
```

### Connect 

You can connect to a database from Python using SQLAlchemy by creating an
 engine: 
 
```python
import os

from sqlalchemy import create_engine

# get credentials from environment variables
user = os.getenv('PGUSER')
password = os.getenv('PGPASSWORD')
host = os.getenv('PGHOST')
port = os.getenv('PGPORT')
database = os.getenv('PGDATABASE')

# configure connection to postgres
engine = create_engine("postgresql://{}:{}@{}:{}/{}").format(user, 
                                                              password, 
                                                              host, 
                                                              port, 
                                                              database) 

# open a connect
db_conn = engine.connect()
```

Now that we have a connection, lets try to run some queries: 

**Select** 

```python
# execute a query with sqlalchemy
sql = """
    select 
      id, city, zip, purpose
    from 
      raw.inspections
    limit 10
"""

result_set = db_conn.execute(sql)
```

Since we are not using Pandas the outcome **is not** in a data frame, it is
 on a cursor that we need to iterate to get each row. 
 
```python
for row in result_set: 
    print(row)
```

**Create tables**

```python
schema = "andrewid"
table = "test"

sql = """
    create table if not exists {}.{} (
        id int,
        amount float, 
        description varchar
    )
""".format(schema, table)

db_conn.execute(sql)
```

It will not be enough to just execute the query, statements that modify the
 state of the database will not be physically reflected until we tell the connection to commit these changes. 
 If you went into DBeaver now, you still wouldn't see this new table! 
 
```python
db_conn.execute("COMMIT")
```

Now you can see the new table :). If you could see it before the commit, then
 your configuration is with autocommit.  


**Insert values into tables**

We would like to insert the following rows into the table we have just created:

```python
sql = """
    insert into {}.{} values(%s, %s, %s)
""".format(schema, table)

# MUST be a list of tuples!
records_to_insert = [(1, 5.50, "tunnamelt sandwich"), (2, 5.60, "hot latte with oatmilk"), 
                     (3, 4.50, "cheese sandwich")]

# insert values 
for record in records_to_insert:
    engine.execute(sql, record)

engine.execute("COMMIT")
```

**Drop tables**  

```python
sql = """
    drop table {}.{};
""".format(schema, table)

db_conn.execute(sql)

db_conn.execute("COMMIT")
```

### Template SQL

Sometimes is easier to just have a template SQL and iterate through some
 values of your interest.

```python
dates = ['2019-01-15', '2020-01-15', '2020-04-15', '2020-06-15']

results = []
for date_ in dates:
    sql = """
       select
          inspect_dt, category_cd, purpose, status
       from {}.{}
       where inspect_dt = '{}'
    """.format('raw', 'inspections', date_)
    
    result_set = db_conn.execute(sql)
    rows = [row for row in result_set]
    results.append(rows)

# you have a list of lists with tuples, you can flat that! or create a df, or read it through pandas
results_one_list = []
for element in results:
    results_one_list += element

results_one_list
``` 

You can have complex sql queries that will be better to put on a sql file with
 some parameters. 
 
Create the file  `sql_example.sql` on your project server on `/mnt/data
/projects/yourprojectsserver/`.

```postgres-sql
--sql template
select 
  inspect_dt, city, status
from 
  {schema_name}.{table_name}
where inspect_dt between '{start_date}' and '{end_date}'
and city in ({cities});
```

Now we can read the file.

```python
# read the file
with open("sql_example.sql", "r") as f:
    sql_template = f.read()

# look at the content
print(sql_template)
```

We will need to define the parameters the query requires:

```python
# parameters
schema_name = "raw"
table_name = "inspections"
start_date = '2019-01-01'
end_date = "2019-06-30"

cities = ['Verona', 'Irwin', 'Bakerstown']

sql = sql_template.format(schema_name=schema_name, table_name=table_name, start_date=start_date, 
                         end_date=end_date, cities=cities)

print(sql)
```

Python adds a square bracket to define a list so we will need to fix this or
 postgres will complain. 

```python
def list_to_string(list_elements, dtype='string'):
    # elements on a list that are strings
    if dtype=='string':
        return ','.join(["'%s'" % element for element in list_elements])
    # elements on a list that are integers
    else:
        return ','.join(["%s" % element for element in list_elements])

cities_ = list_to_string(cities)
print(cities_)
```

```python
sql = sql_template.format(schema_name=schema_name, table_name=table_name, start_date=start_date, 
                         end_date=end_date, cities=cities_)
print(sql)
```

Now we can execute the query: 

```python
df_result_set = pd.read_sql(sql, db_conn)
df_result_set.head()
```
