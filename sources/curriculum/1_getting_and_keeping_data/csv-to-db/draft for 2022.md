# Getting data into a database

## Why use a database compared to CVSs or Excel files

## Let's start with the raw data

### Get a CSV file

Donorschoose project data is in /mnt/data/projects/food-inspections/data/projects.csv

### Load the csv in python

```
df=pd_read_csv('path to file')
```

## Load it in a database

### Get database credentials

```
engine = create_engine("postgresql://")  

```

### Copy it to the database
 
Let's explore a few different ways of getting this CSV in our database

1.

2. 

3. 


## Check to see if worked

## Workflow tips for loading project data
 
