## Data Exploration and Analysis
Once you've got some data, you're going to be eager to dig into it! Our tool of choice for data analysis is Python. Start off
with [Intro to Git and Python](https://github.com/dssg/hitchhikers-guide/blob/master/sources/curriculum/2_data_exploration_and_analysis/intro-to-git-and-python/introduction-to-git-and-python.ipynb), then move onto [Data Exploration in Python](data-exploration-in-python/).
If you're combining data from multiple sources, you'll have to do [record linkage](record-linkage/) to match entities across datasets. Depending on your particular project, you may need special methods and tools; at this time, we have resources
for working with [text data](text-analysis/), [spatial data](gis_analysis/postgis-workshop/tutorial.html) and [network data](network-analysis/).

### Data Exploration Tips
Here are some things you want to do during data exploration:

- distributions of different variables - historgrams, boxplots
- distinct values for a categorical variable
- correlations between variables - you can do a correlation matrix and turn it into a heatmap
- changes and trends over time - how does the data and the entities in the data change over time. Distributions over time.
- missing values: are there lots of missing values? is there any pattern there?
- looking at outliers - this can be done using clustering but also using other methods by plotting distributions.
- cross-tabs (if you're looking at multiple classes/labels), describing how the positive and negative classes are different without doing any machine learning.
