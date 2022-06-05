# Getting data into a database

## Why use a database compared to CVSs or Excel files

## Let's start with the raw data

### Get a CSV file

## Load it in a database

### Get database credentials

`def get_db_conn():
    """ Get an authenticated psycopg db connection"""
    
    user=os.getenv('PGUSER'),  # returns tuple
    password=os.getenv('PGPASSWORD'), #returns tuple
    host=os.getenv('PGHOST'), #returns tuple
    port=int(os.getenv('PGPORT')), #returns tuple
    database=os.getenv('PGDATABASE')
    
    engine = create_engine('postgresql://{}:{}@{}:{}/{}'.format(user[0], 
                                                                password[0], 
                                                                host[0], 
                                                                port[0], 
                                                                database))
    connection = engine.connect()`
    
    
    

### Load the csv in python

### Copy it to the database

## Check if it worked
