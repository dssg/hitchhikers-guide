# Software testing

![tests meme](http://s2.quickmeme.com/img/bf/bf321947675de864ac980948a6c835a82768a0eb48091d32e432fabcf4165666.jpg)

You've finished your wonderful web protytpe for the Data Fest, your model is awesome and that visualizaiton is going to blow eveyrone's minds... You get on stage for a live demo, open the webapp just to see that nothing works. Spooky.

To prevent that from happening, it's important to write tests. Think about it, When you write a function, when do you decide 'it works'? You probable test it against some inputs and if you get the proper result then you move on. Maybe your function indeed works but imagine what would happen if in the following weeks you decide to modify the function to make it faster, you change a few lines, no big deal and you have no time to test it *again*, maybe you just added a bug and you didn't notice.

For that reason, it's important to write automated tests, to check your code and make sure that *at least works as it used to* and that you didn't introduced any bugs.

## I didn't chose the test life, the test life chose me

![darth tester](http://s2.quickmeme.com/img/03/0347c3efdc17cc1959d089f60b8b2fc267d9093caa8e8cb483bf476b58e63e45.jpg)



## Software testing in Python

To see how to test your Python projects [see this](python_testing.md).

## Testing Data Science pipelines

This is a good overview of testing for Data Science: [Testing for Data Scientists by Trey Causey](https://www.youtube.com/watch?v=GEqM9uJi64Q)

### Tools

*   [hypotehsis](https://github.com/HypothesisWorks/hypothesis-python)- Python library to look for edge cases without explicitly coding them
*   [engarde](https://github.com/TomAugspurger/engarde) - Use Python decorators to test a function outcome (this project had good potential but it's dead now)
*   [feature forge](https://github.com/machinalis/featureforge) - Testing features for ML models (also seems dead)

## Automatically testing your projects

### Continous integration



## Resources

*   [Software Testing - Udacity course](https://www.udacity.com/course/software-testing--cs258)