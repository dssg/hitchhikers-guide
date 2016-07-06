# __Skills You Need to do Data Science for Social Good__
The following skill levels can help you gauge where you stand and what things would be useful to brush up on or seek out:   
*   [What you should know before coming to the fellowship](../prerequisites/) and [what you should know after orientation.](https://github.com/dssg/hitchhikers-guide/tree/master/tech-tutorials/)
*   [Cool Kid](#cool-kid): what you should know at the end of the fellowship. 
*   [Data Scientist for Social Good](#data-scientist-for-social-good): what you should know to practice in this field.
*   [Data Witch](#data-witch): skills that are nice to have if you get the chance to pick them up.


##*Cool Kid* 
###Programming and tools

**Best practices**

*   Use `logging`, `print` is evil, here are some [good practices for logging in Python](http://victorlin.me/posts/2012/08/26/good-logging-practice-in-python)
*   Docstrings
    *   [From the Python docs](https://www.python.org/dev/peps/pep-0257/)
    *   [Numpy style doctrings](https://github.com/numpy/numpy/blob/master/doc/HOWTO_DOCUMENT.rst.txt) - widely used in the scientific Python community
*   Writing documentation

**Data visualization**

*   [matplotlib](https://github.com/matplotlib/matplotlib) - De facto standard in Python, most visualization tools are built on top of matplotlib (it has a low-level API)
*   [seaborn](https://github.com/mwaskom/seaborn) - statistical data visualization. A nice option for doing statistical plots, provides a much higher level API than matplotlib
*   [folium](https://github.com/python-visualization/folium) - this is probably the best option available for plotting maps in Python
*   [bokeh](https://github.com/bokeh/bokeh) - interactive plots in Python

**Databases**

*   SQL vs NoSQL - tl; dr; use SQL for analytics
*   Connecting to a database from Python
    *   PostgreSQL - psycopg2

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

**Git and github**

*   Markdown for documenting your repos
*   `.gitignore`
*   Github: Issues and pull requests

**Hadoop and Spark**

*   What they are and when to use them (and when not to)

**Making your models train faster**

*   Concurrent Python - The basics
*   using D3
*   using APIs to get data
*   Scraping
*   R
*   Parallelization
*   parallel for loops
*   SQL DBs: types of DBs - postgres, mysql, sqllite, ms sql server, oracle
*   Types - pros and cons

###Computer Science
*   Algorithmic complexity


###Machine Learning

*   Supervised vs Unsupervised learning
*   Cross-validation
    *   [Cross-validation in scikit-learn](http://scikit-learn.org/stable/modules/cross_validation.html)
*   Bias-variance tradeoff
*   Feature preprocessing
    *   [Feature preprocessing in scikit-learn](http://scikit-learn.org/stable/modules/preprocessing.html)
*   Feature generation
*   Feature selection
    *   [Feature selection in scikit-learn](http://scikit-learn.org/stable/modules/feature_selection.html)
*   Ranking
*   Model evaluation
    *   Grid search
        *   Grid search in [scikit-learn](http://scikit-learn.org/stable/modules/grid_search.html)
    *   Metrics
        *   [Metrics in scikit-learn](http://scikit-learn.org/stable/modules/classes.html#module-sklearn.metrics)
    *   Plots
        *   Classification: Confusion Matrix, Precision-Recall, ROC

###Social Science
*   data bias
*   econ macro/micro
*   experiments
*   A/B
*   MAB


##*Data Scientist for Social Good*


###Programming and tools

**Python**

*   PEP8 - Style guide for Python
    *   [From the official Python documentation](https://www.python.org/dev/peps/pep-0008/)
    *   [PEP8 for humans](http://pep8.org/)
*   Python packaging
    *   [How To Package Your Python Code](https://python-packaging.readthedocs.io/en/latest/) - Extensive guide on Python packaging
*   [Structuring your project](http://docs.python-guide.org/en/latest/writing/structure/)

**Git**

*   [Branching](https://git-scm.com/book/en/v2/Git-Branching-Branching-Workflows)

**Software testing**

*   py.test - The best tool for testing in Python
*   Continous integration with Travis

**Documenting your projects**

*   Sphinx
*   Read the docs

**Workflow management**

*   Open source tools for workflow management
    *   [drake](https://github.com/Factual/drake) - "make for data" - Simplest of all the tools shown
    *   [Airflow](https://github.com/apache/incubator-airflow)
    *   [Luigi](https://github.com/spotify/luigi)
    *   [Pinball](https://github.com/pinterest/pinball)
    *   [Azkaban](https://github.com/azkaban/azkaban)

###Computer Science

*   Distributed systems
*   Algorithmic complexity
*   Data structures: lists/hashes


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
*   Deep Learning
    *   What it is and when to use use it




##*Data Witch*

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
    *   Flask
*   front-end frameworks
*   JS frameworks
*   css

###Computer Science

**Concurrency**

*   [Seven Concurrency Models in Seven Weeks](https://pragprog.com/book/pb7con/seven-concurrency-models-in-seven-weeks) - Practical book on concurrency, covering modern approaches to it

###Math and Stats

*   Linear algebra
*   Simulation
*   Optimization
*   Proofs/formal logic


###Social Science
*   natural experiments
*   diff in diff
*   causal inference with observational data methods
*   regression discontinuity
*   matching
*   instrumental variables

# Conceptual and Unleveled Skills
The following skills haven't been assigned to a level or don't fit in to one. 

###Programming
*   Complexity and Time/Space Constraints: BigO, relational vs non-relational DBs
*   Parallelization: mapreduce, spark, parallel for-loops
*   Cleaning
*   Integration
*   Record linkage (rule based and ml based)

###Scoping and Management
*   Project scoping
*   Agility in dealing with expectations, partners, ect.
*   Managing expectations with partners - how to ensure organizational support and how not to overpromise and underdeliver 

###Privacy, Ethics, and Security 
*   Impact of data bias
*   Prediction bias
*   Common terms:
    * HIPPA
    * Ferpa
    * Privacy-utility tradeoff
    * k anonymity
    * l diversity
*   Differential privacy


###Communications
*   Model Interpretation and Transparency
*   How to interpret different types of models
*   Feature importances
*   Case based explanations
*   Communicating the possibilities/vision
*   Communicating data
*   Communicating models
*   Communicating results
*   Communicating the impact of the work

###Social Issues
Poverty,
Racism,
Equity,
Education,
Health,
Environment,
Politics,
Government,
Crime,
Transportation,
Jobs / economic development,
International development

###Math and Stats
*   Time series analysis 
*   Linear/logistic regression
*   Hypothesis testing
*   Probability (basic theory and distributions)
*   Markov chains/stochastic processes 
*   Maximum likelihood estimation
*   Consistent/efficient estimators 
*   Correlation/causation
*   Experimental design: randomization/replication/blocking
*   Nonparametric statistics, density estimation

###Machine Learning

*   probability estimates
*   Semi-supervised
*   Methodology
*   Out of sample
*   Temporal cross validation

*   precision @ k

*   Field Trial design

*   Model updates and maintenance
*   Different types of data
    * Text analysis
    * Search/indexing
    * Information extraction
    * Images
    * Sound
    * Video
    * Network/graphs
