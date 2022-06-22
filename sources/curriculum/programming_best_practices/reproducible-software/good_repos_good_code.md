# Good Repos, good code

## Goals of the session

+ Elements of a good repo
+ Elements of good coding

At the end of this session you should know:

+ What to have on your `README.md`
+ Why you need a `requirements.txt`
+ "What not to" on your repo
+ "What not to" on your code

## Repos

### Reproducible work

A reproducible work/project:

- Works for someone other than the original team
- Can be **easily** installed on another computer
- Has documentation that describes any dependencies and how to install them
- Comes with enough tests to indicate the software is running properly

### `README.md`

All projects should have a README that communicates the following:

1. What the project is about
   - A short description of the project (i.e. the problem you are trying to solve).

2. The required dependencies to run the software
   - Can be in the form of a *requirements.txt* file for Python that lists
   the dependencies and version numbers.
   - The system-level dependencies.

3. Installation instructions
   - How to install your software and associated binaries. This can be in the form of
     instructions on how to use *pip*, *apt*, *yum*, or some other binary package
     manager.

4. Example usage
   - The inputs and outputs of your software (i.e. how to use it) with code examples.

5. Attribution/Licensing
   - Who did what and how others can use your software.

### `requirements.txt`

Specify the libraries that we are using on our project and the specific versions. (`pip freeze > requirements.txt`)

### `.gitignore`

What are the files or type of files that shouldn't be part of the repo.

Don't upload data files:

+ `csv`
+ `xlsx, xlsx`
+ `zip`

### Folder structure

Keep your directory structure intuitive, interpretable and easy to understand.
[Example](https://github.com/dssg/hitchhikers-guide/tree/master/sources/curriculum/programming_best_practices/reproducible-software#good-directory-organization
).

Structure can change depending on your context.

  + `src`
  + `documents`
  + `notebooks`

### Examples

  + https://github.com/dssg/cfa-getcalfresh
  + https://github.com/dssg/el-salvador-mined-public
  + https://github.com/dssg/state-leg-tracker
  + https://github.com/dssg/hitchhikers-guide/tree/master/sources/curriculum/programming_best_practices/reproducible-software


## Good Code

Think about reproducibility and that others will build upong your project.

### Hard coded files and paths

`load_shapefile_hardpath_v1.sh`

```python
# Data downloaded from this website: http://mrdata.usgs.gov/geology/state/state.php?state=NY
shp2pgsql -d -s 4267:2261 -d /mnt/data/syracuse/NY_geol_dd soil.geology | psql
```

Instead send parameters

`load_shapefile_hardpath_v2.sh`

```python
#!/bin/bash
# Data downloaded from this website: http://mrdata.usgs.gov/geology/state/state.php?state=NY
original_projection=4267
new_projection=2261 #projection of Upstate NY
schema='soil'
table='geology'
shapefile='/mnt/data/syracuse/NY_geol_dd/nygeol_poly_dd.shp'

#create table and schema
psql -c "drop table if exists ${schema}.${table}"
psql -c "create schema if not exists ${schema}"
#import the data
shp2pgsql -d -s ${original_projection}:${new_projection} -d ${shapefile} ${schema}.${table} | psql
```

Or

`process_data.py`

```python
data = '/mnt/data/projects/pakistan-ihhn/data/'
```

`constants.py`

```
PROJECT_SERVER_DATA_PATH = '/mnt/data/projects/pakistan-ihhn/data/'
```

And then on `process_data.py`

```
data = constants.PROJECT_SERVER_DATA_PATH
```


### Documentation

Document your functions so that your future you and others can understand what you are doing on this chunk of code. Use docstrings (your IDE will add the shallow structure).

+ Explicitly document the inputs `:param name: description` (you can add the type)
+ Explicitly document the outputs `:returns:`

```python
def group_process(cleaned_text, model, vocabulary, function_groups_names, root_form, model_embedding):
    """
    Description of what this function is doing

    :param cleaned_text: Description of this parameter
    :param model: Description of this parameter
    :param vocabulary: Description of this parameter
    :param function_groups_names: Description of this parameter
    :param root_form: Description of this parameter
    :model_embedding: Description of this parameter
    :return: Description of the output
    """
```

### Variable names

+ Names should have meaning to the intended readers
+ Using `i,j,k` is ok for iterators and nothing more
+ If you have long names use snake case instead of camel case: `some_name`

### Functions

Use functions to isolate parts of code. One function should have just one
specific task -> unit tests.

### Logging

Instead of having `print` everywhere, use the `logging` package to have a formal log of your process.

Example:

`candidate_assignmente.py`

```
TODAY = date.today()
logging.basicConfig(format= '%(asctime)s %(levelname)-8s %(message)s',
                    filename='candidate_assignment_by_endpoint_' + str(TODAY) + '.log',
                    level=logging.INFO, datefmt='%Y-%m-%d %H:%M:%S')

  def persist_offers(rows):
      """
      Persists offers - candidates - groups on DB on _copy table and on treemap
      :param rows: Data to persist in DB
      :return:
      """
      logging.info("registro en bd")

      ...

      try:
          cursor = db_conn.cursor()
          logging.info('insert into stps _copy candidate')
          try:
              extras.execute_batch(cursor, q, rows)
              db_conn.commit()
          except (Exception, psycopg2.IntegrityError) as error:
              logging.info("duplicate key: " + rows)
              logging.error(error)
              db_conn.rollback()
          else:
              db_conn.commit()
      except (Exception, psycopg2.DatabaseError) as error:
          logging.error(error)
```


### Tests

You should be writing unit tests for your code, that's how you "make sure" your code does what it is supposed to do. 

## What to do 

- Use [virtual environments](#virtual-environments).
- Keep your directory structure [intuitive, interpretable and easy to understand](#good-directory-organization).
- Keep your database free of "junk tables." Keep only what you need and what's current.
  - Junk tables will only confuse your future-self or others that come fresh to the project.
- Merge all branches into master/dev.
  - Branches are for adding features or patches. When you have added said feature or patch
    and you know you won't break the master branch, merge into master and delete the branch.
- Write commit messages in such a way that your log is helpful (see [Git and Github tutorial](https://github.com/dssg/hitchhikers-guide/tree/master/tech-tutorials/git-and-github).)
- [Periodically make database backups](#backup-your-database).
- Document all of your functions with docstrings. (See [legible, good code tutorial](https://github.com/dssg/hitchhikers-guide/tree/master/tech-tutorials/legible-good-code).)
- Write your python code following the PEP8 standard. (See [legible, good code tutorial](https://github.com/dssg/hitchhikers-guide/tree/master/tech-tutorials/legible-good-code).)
- Write unit tests and use continuous integration so you can catch bugs quickly, particularly when you are merging
  new features into master.\*


## What not to do

- Use [hard-coded paths](#hard-coded-paths).
- Require sudo/root privileges to install your project.
  - You can't anticipate whether or not someone will have root access to the machine
    they are installing your project on, so don't count on it. Additionally, you shouldn't
    require users to create separate user names for your project.
- Have a [messy repo with random files everywhere](#bad-directory-organization).
  - This is confusing, irritating and cancerous to productive enterprise.
- Commit data or sensitive information like database passcodes to the GitHub repo.
  - Your repository is for your codebase, not the data. Furthermore, your data may be sensitive
    and need to be protected.
  - Always assume that your repo will be public someday if you are hosting on GitHub (for your DSSG project it will be).
    Sensitive information also includes architecture decisions about your database. After sensitive
    information is pushed to GitHub, you cannot remove it completely from the repository.
- Have code that needs to be operationalized in Jupyter Notebooks.
  - Jupyter notebooks are wonderful for containing your analysis, code and figures in a single document,
    particularly for doing exploratory analysis. They are not good for keeping the code you will need for
    your pipeline or code that you will eventually want to turn into a library.
