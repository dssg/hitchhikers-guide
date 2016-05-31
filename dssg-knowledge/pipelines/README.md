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

A *data pipeline* is a set of code that handles all the computational tasks your project needs from beginning to end. Here's what a typical data pipeline looks like:
![alt text](https://github.com/dssg/hitchhikers-guide/blob/master/dssg-knowledge/pipelines/pipeline_diagram.png "Pipeline Diagram")

Many data pipelines are powerful computer functions: you give them inputs (data and a list of model criteria) and it gives you outputs (predictions and performance metrics). For example, we can build a very, very simple pipeline for the scikit-learn Boston dataset:
 ![alt text](https://github.com/dssg/hitchhikers-guide/blob/master/dssg-knowledge/pipelines/very_very_simple_pipeline.png "Very Simple Pipeline")

Just like other computer functions, this approach gives you two important benefits:
* Reusability: 
  * We didn't need to create an object (e.g. "ridge"), fit a model (e.g. "ridge.fit"), and generate an accuracy metric (e.g. "ridge.score") for every model we tried. Instead, we re-used fit_and_score_model() again and again. 
  * We can give someone else this code and data and they can get the same results (replication).
  * We might even be able to give someone else this code and they can use it for a different problem (reproducability. e.g. scikit-learn's diabetes dataset.)
  * If there's a problem with our code, we only need to fix it in one place. 
* Abstraction: Once we're comfortable with fit_and_score_model(), we can focus on the inputs (e.g. the data and the model choices) and the outputs (the model score), rather than what's inside the function. 

It also allows us to store the inputs and outputs so we have a complete, easy-to-use history of what we did.

Isn't that super duper?

Your projects are far more complex than this Boston example, and your pipelines will reflect that. For the rest of this session, we'll go over the [police pipeline](https://github.com/dssg/police-eis) that we started developing at DSSG 2015.



## Resources
* [Our lead pipeline](https://github.com/dssg/lead-public), started at DSSG 2014
* [Our Cincinnati pipeline](https://github.com/dssg/cincinnati), started at DSSG 2015
* [Diogenes](https://github.com/dssg/diogenes) (a generalized DSSG pipeline)
* [Data Science Toolbox](http://datasciencetoolbox.org/)



## Discussion Notes

