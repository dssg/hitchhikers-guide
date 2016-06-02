# Testing Python Data Science pipelines

Testing Data Pipelines is **hard**. By definition you do not expect them to produce the same output over and over again. Currently there isn't a standard way of doing it (or at least I don't know it), but here you'll find some tips to test your pipeline to some extent.

## Tips and tricks to test your pipeline

### Separate the logic/math to a modules and put your pipeline steps in a different one



### Make the assumptions in your data explicit

### Test your code with a fake database



## Tools for testing

-   [hypothesis](https://github.com/HypothesisWorks/hypothesis-python) - Python library to look for edge cases without explicitly coding them
-   [engarde](https://github.com/TomAugspurger/engarde) - Use Python decorators to test a function outcome (this project had good potential but it's dead now)
-   [feature forge](https://github.com/machinalis/featureforge) - Testing features for ML models (also seems dead)



## External resources

*    [Testing for Data Scientists by Trey Causey](https://www.youtube.com/watch?v=GEqM9uJi64Q)