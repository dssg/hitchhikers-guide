# Software testing

[Slides from 2016 DSSG](https://github.com/redshiftzero/testing-tutorial)

![tests meme](http://s2.quickmeme.com/img/bf/bf321947675de864ac980948a6c835a82768a0eb48091d32e432fabcf4165666.jpg)

You've finished your wonderful web prototpe for the Data Fest, your
model is awesome and that visualizaiton is going to blow everyone's
minds... You get on stage for a live demo and open the webapp only to
find that nothing works. Spooky.

To prevent that from happening, it's important to write tests. Think
about it, when you write a function, when do you know *it works*™? You
probably test it against some ad hoc inputs and, if you get the proper
result, you move on. Maybe your function *does* indeed work today, but
what if in the following weeks you change a few lines of the function
to make it faster, but you don't want to spend time testing again (*it
works*™)? Maybe you just introduced a bug and didn't notice.

For that reason, it's important to write automated tests to check your code and make sure that everything
*works consistently*, and that you can identify bugs introduced by
future changes.

## I didn't choose the test life, the test life chose me

![darth
tester](http://s2.quickmeme.com/img/03/0347c3efdc17cc1959d089f60b8b2fc267d9093caa8e8cb483bf476b58e63e45.jpg)

This tutorial is divided in three parts. The first one addresses *unit testing*, which is a simple
(but powerful) form of testing. The second part is devoted
specifically to testing Data Science pipelines.

The last section covers *Continuous Integration* (or CI). CI is a technique to automatically run all of
your tests every time you push new code to Github. CI is language-agnostic, but our tutorial specifically
addresses Python, because it is the language we use the most.

*   **Part 1:** [Unit Testing with Python](python_testing.md) (interactive tutorial), [How I Learned to Stop Worrying and Love Unit Testing](unit_testing.pdf) (teachout slides - [Kat Rasch](https://github.com/krasch))
*   **Part 2:** [Testing Python Data Science Pipelines](ds_testing.md)
*   **Part 3:** [Continuous Integration](ci.md)

## External Resources

- [Unit testing for Data Science - slides from Hanna (2016 DSSG fellow)](https://github.com/htorrence/pytest_examples/blob/master/unit_testing_for_data_science_talk/pydata_NYC_2018_unit_test_talk.pdf?fbclid=IwAR04pGF0sxJJgrZZjBy-1VDLY4ly3gX7eD4PuMtR9lO9ZH8MVl5Np8COU8Y)

- [Unit testing and logging for Data Science - Ori Cohen](https://towardsdatascience.com/unit-testing-and-logging-for-data-science-d7fb8fd5d217)

- [Best Testing Practices for Data Science - Eric J. Ma](https://www.youtube.com/watch?v=yACtdj1_IxE)

- [Database(Data) Testing Tutorial with Sample TestCases](https://www.guru99.com/data-testing.html)
