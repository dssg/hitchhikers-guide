# Pipelining frameworks and Workflow management

When working on a machine learning problem, often a lot of time is invested in basic steps
like loading and saving data, keeping track of parameters, and organising the code
to run the steps in the right order.
Machine learning pipelines can become complex as time goes on and are often used by multiple people.

Workflow management tools are made to help reduce the effort required for these steps.

The most commonly used pipelining frameworks are

- [Airflow](https://airflow.apache.org/) - developed by AirBnB. Open-sourced in 2015.
- [Luigi](https://github.com/spotify/luigi) - developed by Spotify. Open-sourced in 2011

QuantumBlack recently open-sourced their framework called [Kedro](https://pypi.org/project/kedro/).

## Workflows are DAGs

Tasks performed in a machine learning project are depended on each other, but should not be circular.
In other words, they form a directed acyclic graph - a DAG.
Worflow management systems (WMS) take advantage of this fact and optimise the execution of each step in the graph.

For example,
Airflow interprets each task as a node in a graph and the dependency between tasks as edges.

Tasks could be
- Transformations / operations on data sets
- Sensors that check for the state of a process or a data structure

Luigi and Kedro see nodes as data sets and edges are the functions that transform parent 
data sets into a child data set.
Luigi calls them Tasks and Targets.

## Code example

To see in in action, we'll look at a simple code example on 
[Towards Data Science](https://towardsdatascience.com/data-pipelines-luigi-airflow-everything-you-need-to-know-18dc741449b7).


## Visualisations

Airflow offers a powerful UI where the user can monitor DAGs and task execution and can 
directly interact with them through the web UI.

Luigi and Kedro offer a very minimal UI. There is no user interaction with running processes.

## References

Most of the content here is taken from 
[Towards Data Science](https://towardsdatascience.com/data-pipelines-luigi-airflow-everything-you-need-to-know-18dc741449b7).

