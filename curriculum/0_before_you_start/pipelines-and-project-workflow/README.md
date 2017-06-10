# Pipelines and Project Workflow

## Motivation

Most data-science projects have the same set of tasks:

1. ETL: extracting data from its source, transforming it, then loading it into a database.
2. Pre-process data: This might include imputing missing values and choosing the training and testing sets.
3. Train the model(s): You can try different algorithms, features, and so on. 
4. Assess performance on the test set: Using an appropriate accuracy metric (e.g. AUC), examine the performance of your model "out of sample." 
5. Think of new things to try. Repeat steps 1 through 4 as appropriate. 

Often, by the time you build a couple dozen models, you're struggling to remember the details of each. What features did you use for each? What training and testing split?  What hyperparameters?

Your code might be getting messy too. Did you overwrite the code for the previous model? Maybe you copied, pasted, and edited code from an earlier model. Can you still read what's there? It can quickly become a hodgepodge that requires heroics to decipher.

In this session, we will introduce the data pipeline, an approach that helps you simplify the modeling process.



## Concepts

A *data pipeline* is a set of code that handles all the computational tasks your project needs from beginning to end. The typical data pipeline is a set of functions strung together. Here's a simple example using scikit-learn's boston dataset:

![alt text](https://github.com/dssg/hitchhikers-guide/blob/master/curriculum/pipelines-and-project-workflow/boston_pipeline.png "Simple Pipeline")

This pipeline has two steps. The first, which I call "preprocessing," prepares the data for modeling by creating training and testing splits. The second, which I call "models, predictions, and metrics," uses the preprocessed data to train models, make predictions, and print r^2 on the test set. The pipeline takes inputs (e.g. data, training/testing proportions, and model types) at one end and produces outputs (accuracy) at the other end. 

Obviously, this analysis is incomplete, but the pipeline is a good start. Because we use the same code and data, we can run the pipeline from beginning to end and get the same results. And because we split the pipeline into functions, we can identify where the pipeline goes wrong and improve the pipeline one function at a time. (Each function just needs to use the same inputs and outputs as before.) 

Also note the function and loops in the second part of the pipeline. We're somewhat agnostic about the methods we use. If it works, great! This structure lets us loop through many types of models using the same preprocessed data and the same predictions and metrics. It makes adding new methods and comparing the results easier, and it helps us focus on other parts of the pipeline, such as feature generation. 

Aren't pipelines super duper?

Our projects are far more complex than this Boston example, and our pipelines reflect that. Here's what a typical DSSG pipeline looks like:
 
![alt text](https://github.com/dssg/hitchhikers-guide/blob/master/curriculum/pipelines-and-project-workflow/pipeline_diagram.png "Pipeline Diagram")

The [police pipeline](https://github.com/dssg/police-eis), started at DSSG 2015, is an example of a relatively well developed pipeline. It lets us specify the pipeline options we want in a yaml file, from preprocessing on. (The code in this repository does not include ETL.) It gives us many modeling options, and it makes comparisons easy.


## Your Pipeline and the DSSG Schedule

Much of your work will revolve around and within your pipeline, but we have identified specific aspects for you to focus on [each week](https://github.com/dssg/hitchhikers-guide/blob/master/dssg-manual/summer-overview/high-level-summer-plan.pdf):

![](summerplan.png?raw=true)

## Resources

* [Our lead pipeline](https://github.com/dssg/lead-public), started at DSSG 2014
* [Our Cincinnati pipeline](https://github.com/dssg/cincinnati), started at DSSG 2015
* [Diogenes](https://github.com/dssg/diogenes) (a generalized DSSG pipeline)
* [Data Science Toolbox](http://datasciencetoolbox.org/)



## Discussion Notes









