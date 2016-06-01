#Skills You Need
The following five skill levels can help you gauge where you stand and what things would be useful to brush up on or seek out:   
*   [Level 0 - Fellow](#fellow): what you should know before coming to the fellowship.
*   [Level 1 - Rookie](#rookie): what you should know after orientation.
*   [Level 2 - Cool Kid](#cool-kid): what you should know at the end of the fellowship. 
*   [Level 3 - Data Scientist for Social Good](#data-scientist-for-social-good): what you should know to practice in this field.
*   [Level 4 - Data Witch](#data-witch): skills that are nice to have if you get the chance to pick them up.

##Fellow   
  Check out the [prerequisites](prerequisites/). 

##Rookie
###Programming
-   Python: [An Informal Introduction to Python](https://docs.python.org/2/tutorial/introduction.html)
    - Ipython notebooks, pandas, numpy, scipy, sklearn, matplotlib
-   Git
    -   [Try Git](http://try.github.com/)
    -   [Github basics](https://guides.github.com/activities/hello-world/)
-   UNIX Command Line: [A Command Line Primer for Beginners](http://lifehacker.com/5633909/who-needs-a-mouse-learn-to-use-the-command-line-for-almost-anything)
-   Introduction to databases
    - creating schemas/dbs, getting data in (copy command), getting data out (command line, python, R), SQL GUIs (dbeaver, dbvisualizer) 
-   AWS/Cloud
    - ec2, rds, s3, Redshift

###Computer Science

###Math and Stats



##Cool Kid 
###Programming and tools

**Best practices**

*   Use `logging`, `print` is evil, here are some [good practices for logging in Python](http://victorlin.me/posts/2012/08/26/good-logging-practice-in-python)
*   Docstrings
*   Writing documentation

**Data visualization**

*   [matplotlib](https://github.com/matplotlib/matplotlib) - De facto standard in Python, most visualization tools are built on top of matplotlib (it has a low-level API)
*   [seaborn](https://github.com/mwaskom/seaborn) - statistical data visualization. A nice option for doing statistical plots, provides a much higher level API than matplotlib
*   [folium](https://github.com/python-visualization/folium) - this is probably the best option available for plotting maps in Python
*   [bokeh](https://github.com/bokeh/bokeh) - interactive plots in Python

**Databases**

*   SQL vs NoSQL

**Command line**

*   [The Linux Command Line](http://www.amazon.com/Linux-Command-Line-Complete-Introduction/dp/1593273894?ie=UTF8&keywords=The%20Linux%20Command%20Line&qid=1464744173&ref_=sr_1_1&sr=8-1) - An excellent introductory text to get to use the linux command line
*   Package management

**Environment management**

*   miniconda (recommended)
*   anaconda
*   virtualenv

**Asking for help**

*   StackOverflow
*   Github issues



using D3

using APIs to get data
Scraping
R
Parallelization
parallel for loops
mapreduce
spark
SQL DBs: types of DBs - postgres, mysql, sqllite, ms sql server, oracle
NoSQ	 DBs	
Types - pros and cons
Using one of them from python

###Computer Science
Algorithmic complexity

###Math and Stats

###Machine Learning

*   Supervised vs Unsupervised learning
*   Bias-variance tradeoff
*   Feature generation
*   Feature selection
    *   [Feature selection in scikit-learn](http://scikit-learn.org/stable/modules/feature_selection.html)
*   Ranking
*   Model evaluation
    *   Selecting proper metrics
    *   Plots

###Social Science
data bias
econ macro/micro
experiments
A/B
MAB


##Data Scientist for Social Good


###Programming and tools

**Python**

*   PEP8 - Style guide for Python
    *   [From the official Python documentation](https://www.python.org/dev/peps/pep-0008/)
    *   [PEP8 for humans](http://pep8.org/)
*   Python packaging
    *   [How To Package Your Python Code](https://python-packaging.readthedocs.io/en/latest/) - Extensive guide on Python packaging

**Git**

*   [Branching](https://git-scm.com/book/en/v2/Git-Branching-Branching-Workflows)

**Software testing**

**Documenting your projects**

*   Sphinx

**Job schedulers**

###Computer Science

*   Distributed systems

Algorithmic complexity
Data structures: lists/hashes

Algorithms

###Math and Stats
###Machine Learning

*   Out of core learning - When your data does not fit into memory and [Hadoop is still an overkill](http://research.microsoft.com/apps/pubs/default.aspx?id=163083)
    *   [Out of core learning in scikit-learn](http://scikit-learn.org/stable/modules/scaling_strategies.html)
*   Hyper-parameter optimization
    *   [Practical Bayesian Optimization of Machine Learning Algorithms](https://arxiv.org/pdf/1206.2944.pdf)
    *   Python libraries (highly experimental and unstable)
        *   [Hyperopt](http://hyperopt.github.io/hyperopt/) - Implements TPE
        *   [Optunity](http://pythonhosted.org/Optunity/)
        *   [Spearmint](https://github.com/HIPS/Spearmint)
        *   [auto-sklearn](http://automl.github.io/auto-sklearn/stable/)
        *   [SMAC](http://www.cs.ubc.ca/labs/beta/Projects/SMAC/)
        *   [HPOlib](https://github.com/automl/hpolib)
*   Serving Machine Learning models
    *   [Using scikit-learn pickle](http://scikit-learn.org/stable/modules/model_persistence.html) (not recommended in production)
    *   PMML
        *   [sklearn2pmml](https://github.com/jpmml/sklearn2pmml)

###Social Science






##Data Witch

###Programming and tools
**Becoming a Python ninja**

-   [Fluent Python](http://www.amazon.com/Fluent-Python-Luciano-Ramalho/dp/1491946008?ie=UTF8&keywords=fluent%20python&qid=1464742151&ref_=sr_1_1&sr=8-1) - This is a must read to become a Pythonista. This book should be called *Poetry for Python Programmers*.
-   [numba](http://numba.pydata.org/) - Acceleratnig your scientific Python code
-   [High Performance Pandas](https://www.youtube.com/watch?v=2RW9zSQF1Sk)
-   [Advanced scikit-learn](https://www.youtube.com/watch?v=ZL77pbWBZQA)

**Reproducible Data Science Pipelines**

*   [Docker for Data Science by Michelangelo D'Agostino](https://www.youtube.com/watch?v=GOW6yQpxOIg)
*   Experiment logging

**Data Products**

*   Web development

front-end frameworks
JS frameworks
css

###Computer Science

**Concurrency**

*   [Seven Concurrency Models in Seven Weeks](https://pragprog.com/book/pb7con/seven-concurrency-models-in-seven-weeks) - Practical book on concurrency, covering modern approaches to it

###Math and Stats

Linear algebra
Simulation
Optimization
Proofs/formal logic

###Machine Learning
###Social Science
natural experiments
diff in diff
causal inference with observational data methods
regression discontinuity
matching
instrumental variables

##Conceptual and Unleveled Skills
The following skills haven't been assigned to a level or don't fit in to one. 

###Programming

Complexity and Time/Space Constraints: BigO, relational vs non-relational DBs

parallelization: mapreduce, spark, parallel for-loops
Cleaning
Integration
record linkage (rule based and ml based)


###Scoping and Management

Project scoping
Agile 
Managing expectations with partners - how to ensure organizational support and how not to overpromise and underdeliver 
Agile

###Privacy, Ethics, and Security 
impact of data bias
prediction bias
prediction error bias
common terms
hippa
Ferpa
privacy utility tradeoff
privacy measures
k anonymity
l diversity
differential privacy


###Communications
Model Interpretation and Transparency
how to interpret different types of models
feature importances
case based explanations
communicating the possibilities/vision
communicating data
communicating models
communicating results
communicating the impact of the work

###Social Issues
Poverty
Racism
Equity
Education
Health
Environment
Politics
Government
Crime
Transportation
Jobs / economic development
International development

###Math and Stats
Time series analysis 
Linear/logistic regression
Hypothesis testing
Probability (basic theory and distributions)
Markov chains/stochastic processes 
Maximum likelihood estimation
Consistent/efficient estimators 
Correlation/causation
Experimental design: randomization/replication/blocking
Nonparametric statistics, density estimation

###Machine Learning

probability estimates
Semi-supervised
For loops
Evaluation
methodology
out of sample
Cross validation
temporal cross validation
metrics
accuracy, precision, recall, auc
precision @ k
Field Trial design
Model updates and maintenance
Different types of data
text analysis
search/indexing
classification
clustering
information extraction
images
sound
video
network/graphs
