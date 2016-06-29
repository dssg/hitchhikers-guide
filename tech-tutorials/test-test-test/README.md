# Software testing

![tests meme](http://s2.quickmeme.com/img/bf/bf321947675de864ac980948a6c835a82768a0eb48091d32e432fabcf4165666.jpg)

You've finished your wonderful web protytpe for the Data Fest, your model is awesome and that visualizaiton is going to blow everyone's minds... You get on stage for a live demo and open the webapp just to see that nothing works. Spooky.

To prevent that from happening, it's important to write tests. Think about it, when you write a function, when do you know *it works*™? You probably test it against some inputs and if you get the proper result you move on. Maybe your function indeed works but imagine what would happen if in the following weeks you decide to modify the function to make it faster, you change a few lines, but you don't want to spend time testing again cause *it works*™, maybe you just introduced a bug and didn't notice.

For that reason, it's important to write automated tests to check your code and make sure that *at least works as it used to* and that you didn't introduced any bugs with recent changes.

## I didn't chose the test life, the test life chose me

![darth tester](http://s2.quickmeme.com/img/03/0347c3efdc17cc1959d089f60b8b2fc267d9093caa8e8cb483bf476b58e63e45.jpg)



This tutorial is divided in three parts, the first one is about *unit testing*, which is the simplest (but powerful) form of testing. The second part is devoted specifically to testing Data Science pipelines.

The last section covers *Continuous Integration* (or CI). This technique is language agnostic but we'll cover some specific things for Python, CI is a technique to automatically run all your tests every time you push to Github.

*   **Part 1:** [Unit testing with Python](python_testing.md)
*   **Part 2:** [Testing Python Data Science pipelines](ds_testing.md)
*   **Part 3:** [Continuous Integration](ci.md)

## External resources

*   [Software Testing - Udacity course](https://www.udacity.com/course/software-testing--cs258)

    ​
