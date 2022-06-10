# Data Exploration and Analysis
Once you've got some data, you're going to be eager to dig into it! Our tool of choice for data analysis is a comnbination of Python and SQL. Start off
with [Intro to Git and Python](https://github.com/dssg/hitchhikers-guide/blob/master/sources/curriculum/2_data_exploration_and_analysis/intro-to-git-and-python/introduction-to-git-and-python.ipynb), then move onto [Data Exploration in Python](data-exploration-in-python/).
If you're combining data from multiple sources, you'll have to do [record linkage](record-linkage/) to match entities across datasets. Depending on your particular project, you may need special methods and tools; at this time, we have resources
for working with [text data](text-analysis/), [spatial data](gis_analysis/postgis-workshop/tutorial.html) and [network data](network-analysis/).
 
## Why is data exploration important

- Sanity Check the data you were given
- Understanding the problem and domain 
- Problem Formulation 
- Debugging 
- Feature Generation/Selection 
- Interpretation of results 

## How to start doing data exploration 
**Tables**: identify the database tables that are most relevant to your problem
**Entities**: How can you identify the primary entities from your project? What are some basic/relevant characteristics about them? How have those changed over time?
**Fields**: Most projects have a lot of different data fields, but don’t feel like your initial exploration needs to understand everything
**Label**: Think ahead about how you might define your label? It's bit early to know what your label/outcome of interest may be exactly but it's worth having some hypothesis about it so you can do more targeted data exploration. What can you say about its distribution and how it’s changed over time?
Based on what you know of the context, what information would you expect to be important in modeling? Is this available? How well does it correlate with your label?

## Data Exploration Tips
Here are some things you want to do during data exploration:

- distributions of different variables - historgrams, boxplots
- distinct values for a categorical variable
- correlations between variables - you can do a correlation matrix and turn it into a heatmap
- changes and trends over time - how does the data and the entities in the data change over time. Distributions over time.
- missing values: are there lots of missing values? is there any pattern there?
- looking at outliers - this can be done using clustering but also using other methods by plotting distributions.
- cross-tabs (if you're looking at multiple classes/labels), describing how the positive and negative classes are different without doing any machine learning.

## Tools to consider

- SQL (directly and through python – psycopg2)
- Python (matplotlib, seaborn, altair,...)
- Pandas(if you have to)
- Tableau (use an ssh tunnel)

## A simple goal to work towards

1. Write a SQL query that takes a “person id” (e.g., student, voter, facility, entity, etc) and gives you everything you know about that person across all the tables you have. 
2. Add a date parameter to it to give you everything about that entity up to that date 
