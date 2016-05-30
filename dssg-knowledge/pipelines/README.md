# Pipelines and Project Workflow

## Motivation
Every DSSG project uses a *data pipeline*: a set of code that makes repeating and extending your data processing and analysis steps relatively simple.

Every team will develop some sort of pipeline for their project. Less experienced teams haven’t had experience structuring their workflows, and we want them to have a decent example so they don’t waste time slowly developing a problematic pipeline. Although teams aren’t necessarily writing production code, they will need to hand over an end-to-end working product at the end of the summer. They need to document all ETL and modeling, so that someone unfamiliar with the project can *understand what they did* as well as *run their code and reproduce their results*. 




## Concepts

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


![alt text](https://www.lucidchart.com/publicSegments/view/6d86145d-48b4-44f7-bea1-e7dfbccd364f/image.png "Pipeline Diagram")


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
* [Example pipeline](https//github.com/edublancas/ds-template)
* [Data Science Toolbox](http://datasciencetoolbox.org/)



## Discussion Notes

