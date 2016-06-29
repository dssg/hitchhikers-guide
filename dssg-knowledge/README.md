## ML: Machine Learning and Practical Validity (due week 4)
#### Motivation: 
By definition this work involves abstracting or disguising the human element by turning a social problem into an optimization problem. It is important to think carefully about how we do that, implicit and explicit assumptions, and common pitfalls.
#### Concepts: 
Mapping a social science problem to ML problem - defining an objective function, ethical questions, potential for misuse, evaluation and validation (just because you’re modeling something well doesn’t mean it’s what you think you’re modeling, or that the application will be effective). Social implications (and potential biases) should be worked out; contextualizing project from a data-driven, practical perspective. ref future ML talks

## ML: Predictive Modeling (due week 4)
#### Motivation: 
People coming from social science or stats background are usually familiar with modeling for interpretation so it is a leap for them to go to throwing as many models and features as possible at a problem.
#### Concepts: 
Prediction vs. interpretation- what this means for feature generation and model evaluation (you include all information even if it might not be useful), collinearity is not as concerning, feature selection/regularization 

## ML: Model Evaluation (due week 4)
#### Motivation:
You build a lot of models. You have to choose between them. How?
#### Concepts:
Constructing a training/test split, AUC/precision/recall, deciding on a metric based on the context of the problem (ranked list/precision at top K), generalizability (EPA test set bias)


## ML: Temporal Cross Validation
#### Motivation:
Most projects will aim to predict some outcome before it happens, need to build models that don’t leak information so you estimate performance as accurately as possible 
#### Concepts:
How to choose granularity/observation level (predicting in the next day/week/year), how to set up training and test sets (both conceptually and technically), difference between training window (observations) and aggregation windows (features), how to not cross contaminate, how does model update when more data is added
Resources: 

## Databases (due week 2)
#### Motivation:
Fellows have already learned how to do basic input/output in Postgres. This talk will provide more depth about how databases work, what types are out there, and which to use for which purpose.
####Concepts:
####Resources:

## Software Development in Python (due week 3)

#### Motivation:
Some people who are proficient in R haven’t done any other software development; use Python to introduce more of that.

#### Concepts:
Modules, debugging, Packaging code, setup.py, docker, drake.

#### Tools:
Python syntax and patterns

#### Resources:
How to Develop Quality Python Code (District Data Labs) 

## Remotes, AWS & Pimp my Dotfiles (due week 3)

#### Motivation:
Working remotely (e.g. AWS) and/or on multiple projects. How do you comfortably work on a remote? How do you configure your command line tools for your daily tasks?

#### Tools:
.bashrc, aliases, ssh, shfs, tmux, virtualenv, conda, PYTHONPATH, *.pth, relative imports

## Cloud Computing (due week 6)
#### Motivation:
Most pipelines and data products run on cloud resources. What are they and how do you use them?


## Debugging in R & Python
#### Motivation:
#### Concepts:
#### Tools:
#### Resources:

## Test, Test, Test
#### Motivation:
#### Concepts:
#### Tools:
unittest, mock, nose, travis
#### Resources:

## Working in SQL
#### Motivation:
As you generate features, you need to make more complicated joins/queries to aggregate spatially and temporally.
#### Concepts:
Generating features before/after generating training and test sets, long vs wide formats, GIS ...
#### Tools:
#### Resources:


## Data Viz: Interactive Data Exploration
#### Motivation:
#### Concepts:
#### Tools:
#### Resources:

## Data Viz: Communication of Results
#### Motivation:
#### Concepts:
#### Tools:
#### Resources:

## Web Apps
#### Motivation:
Many projects include a web app as a deliverable 

#### Concepts:
Visualizing model results for your own use and for partner use; showing “feature importance”/why an example is flagged in an honest, straightforward way when the model is not as interpretable (e.g. either labeled positive examples with similar features or distribution of features on training set)
#### Tools:
#### Resources:
Using APIs for Data Science

# Social Science Concepts 
Very short introduction to formalism, and its application
- What is it? Theory (or intuition), algorithm
- How to do it? Tools
- What is it useful for? (application examples, insightful studies)


## Intro to Quantitative Social Science (due week 2)
#### Motivation:
You’re doing causal inference, you might have observational data. Learn vocabulary, learn motivation. 
If we don’t get to the rest of them, you need to at least be familiar.


#### Concepts:
Short overview of everything in the other 4 sessions

## Causal Inference with Experimental Data I
#### Motivation:

#### Concepts:
Experimental design, hypothesis testing, multiple hypothesis testing

#### Tools:
Power calculator, single-tailed tests 

#### Resources:

## Causal Inference with Experimental Data II
#### Motivation:

#### Concepts:
RCT, multi-armed bandits (adaptive experiments), experimental design

#### Resources:

## Causal Inference with Observational Data  I

#### Motivation:
duh

#### Concepts:
Instrumental variables, natural experiments, regression discontinuity

#### Resources:

## Causal Inference with Observational Data  II
#### Motivation:
Computer scientists use regressions to make predictions, but don’t care what the coefficients are. Social scientists want to have meaningful and interpretable coefficients.  

#### Concepts:
Regression, matching, propensity score matching, regression discontinuity

#### Resources:

# Social Issues and Implications 

### Social Issues

### Poverty

### Racism 

### Equity

###Education

### Healthcare
### Jobs
* Economic health and development and employment, what are people doing in different cities/countries

### Respectful Conversations (due week 3) 

### Open Source, Open Data, and Transparency 
###	Social Services 
* Criminal Justice
