# Pipelines and Project Workflow

## Motivation

We've all done data analysis where we write a line of code to fit a model, look at the results, write another line of code to fit a model, look at the results, and so on. For ex    ample, we might fit three regression models to the sklearn Boston data:
![alt text](https://github.com/dssg/hitchhikers-guide/blob/master/dssg-knowledge/pipelines/no_pipeline_analysis.png "Pipeline-less Analysis")

What if we were to try more ridge hyperparameters? lasso regression? subsets of features? or even incorporating external data sources? We end up writing a fair amount of code -- three or more lines for each combination. We also struggle to keep track of the consequential choices we made along the way. The result: frustration, wasted time, and sub-optimal model performance.

In this session, we introduce the data pipeline.


## Concepts

A *data pipeline* is a set of code that handles all the computational tasks your project needs from beginning to end. Here's what a typical data pipeline looks like:
![alt text](https://www.lucidchart.com/publicSegments/view/c3e9a1ba-2d26-4407-8b8e-d3cbf88ad68f/image.png "Pipeline Diagram")

For the Boston example, 


You can think about a data pipeline as a powerful computer function: you give it inputs (data and modeling choices) and it gives you outputs (predictions and performance metrics). 


* Abstraction: Once the pipeline -- or even parts of the pipeline -- perform well, you can focus on the inputs and outputs rather than what's happening underneath. Isn't that nice?
* Reusability: Not only can you reuse code; you can also vary the pipeline inputs and see how the outputs change. 

In the Boston example, we could write a simple function that takes the classifier, its hyperparameters, and the data as inputs and produces the score as an output. Then we'd only need to write one short line of code for each combination rather than three:
![alt text](https://github.com/dssg/hitchhikers-guide/blob/master/dssg-knowledge/pipelines/fit_and_score_function.png "Pipeline Analysis")

Reusability can be within a project (e.g. last year's project tried lots of models to identify Charlotte-Mecklenburg police officers at risk of adverse incidents) or even between projects (e.g. this year's project will learn how well our CMPD pipeline and results hold for the Metropolitan Nashville Police Department). 


* You can try lots of inputs and track the outputs (e.g. how much do the results change with changes in the inputs?) (It standardizes outputs, makes them comparable. e.g. makes it easier to track whether observations get dropped and whether the comparisons are fair, e.g. without pipeline, we might run a random forest with different options than logistic regression.)
* You can modify the pipeline to try new things. For example, you can try random forest, logistic regression, SVMs, naive Bayes, and many other algorithms. You can also try many hyperparameters for each.
* Pipelines make your analysis reproducible.
 





 

Every DSSG project will use a data pipeline. The specifics may vary, but  

 

 makes repeating and extending your data processing and analysis steps relatively simple.

In this session, we introduce the concept of a data pipeline. Data pipelines are 

 
Every team will develop some sort of pipeline for their project. Less experienced teams haven’t had experience structuring their workflows, and we want them to have a decent example so they don’t waste time slowly developing a problematic pipeline. Although teams aren’t necessarily writing production code, they will need to hand over an end-to-end working product at the end of the summer. They need to document all ETL and modeling, so that someone unfamiliar with the project can *understand what they did* as well as *run their code and reproduce their results*. 



Connect this to the [summer schedule](https://drive.google.com/file/d/0B785LvQJaoZMNktzekNrT1VhY2s/view) (approximately where will you be at each week) and an example pipeline.

Two important parts to data science. Both create dependencies:
* data
* code. Numerous assumptions made along the way, often too many to track. The code captures them. For example, drop rows? Drop columns? Replace missing values? person deduplication?
We gave CMPD the code and the data in our format, and they were able to run the pipeline without problems.


Data "science" requires replication (the ability to obtain the same results using the same data and code) and reproducibility (obtaining the same results using different data). [reproducibility and replicability](http://cogprints.org/7691/7/ICMLws09.pdf). Pipelines help with both. (For the Nashville project, we're going to generalize the CMPD pipeline as much as possible. We'll probably end up with a standard set of analytics and output tools and a standard schema ("give us your data in this specific format!") but department-specific ETL tools that bring the data into a standard format for the rest of the pipeline.)


If it's not in code, it wasn't done.

Most data-science pipelines are powerful computer functions:
* It's a piece of code. You give an input and it gives an output.
* This is powerful: 
  * You can try lots of inputs and track the outputs (e.g. how much do the results change with changes in the inputs?) (It standardizes outputs, makes them comparable. e.g. makes it easier to track whether observations get dropped and whether the comparisons are fair, e.g. without pipeline, we might run a random forest with different options than logistic regression.)
  * You can modify the pipeline to try new things. For example, you can try random forest, logistic regression, SVMs, naive Bayes, and many other algorithms. You can also try many hyperparameters for each.
* Pipelines make your analysis reproducible.


![alt text](https://www.lucidchart.com/publicSegments/view/c3e9a1ba-2d26-4407-8b8e-d3cbf88ad68f/image.png "Pipeline Diagram")


Abstraction 



### Testing
* Temporal cross validation: the pipeline automates this
* Simulate data, see whether pipeline performs correctly 



### Tradeoffs
* There's no such thing as a free lunch. There are tradeoffs to every pipeline.
* Every pipeline will differ a bit. 



## A Basic Structure
* ETL: different formats (SQL, Access, Excel, CSV, etc), variable names (e.g. some police departments call it "Internal Affairs," others "Office of Professional Accountability"), variables (e.g. some departments collect compliments, departments have different definitions of "use of force")
* Analysis
* Output
*   



## Resources
* [Police Pipeline](https://github.com/dssg/police-eis)
* [Data Science Toolbox](http://datasciencetoolbox.org/)



## Discussion Notes

