# Continuous integration

Tests are (ideally) cheap to run, so it makes sense to run them every time your code changes. In [Part 1](python_testing.md), we ran a test suite using `py.test`. Running our test suite locally every time your project changes is a good practice, but it's important to also test it on a completely different machine (maybe some of your tests are passing because of local configuration and you don't even know). Furthermore, when working in teams someone may forget to run the tests locally breaking the project. Continuous integration helps you identify those cases (and with proper configuration even reject commits that break the build) just after a push is made.

If you are working on an open source project, you can get Continuous Integration for free using [Travis CI](https://travis-ci.org/). In the following sections we'll see how to setup Travis to run your tests every time you push to Github.

## Using Travis CI

The first step is to [create an account](https://travis-ci.com/) and link it to your Github profile. Travis is integrated with Github and requires minimal setup,  you just need to create a `.travis.yml ` file (note the leading dot) in your root folder, then go to Travis and activate the repo. Let's see how a `.travis.yml` file looks like.

## Travis configuration file for testing scientific Python projects

The content of your configuration file completely depends on your project, but given that most DSSG (if not all) teams use Python + Numpy + Scipy, the following file will work for you with minimal changes. The contents of the file are straightforward and tell Travis how to build your project and run the test suite.

```yaml
language: python
python:
  # list the python version you want to check your tests on
  - "2.7"
  - "3.5"
sudo: required
install:
  # this are requirements to install many scentific python packages
  # such as numpy/scipy, you cannot install them with pip
  # so we need to use the system package manager
  - "sudo apt-get install gfortran python-liblas libblas-dev liblapack-dev libatlas-dev"
  # as of June 2, 2016, travis has an outdated version of pip,
  # this may cause trouble when installing some packages such as sci-kit learn
  # updating pip before using 'pip install' solves those issues
  - "pip install --upgrade pip"
  # install specific requirements your test suite uses
  # e.g. pytest, nose, mock
  # make sure you have the requirements.txt in your repo's root folder
  - "pip install -r requirements.txt"
script:
  # steps needed to run your scripts, for simple projects
  # this may be just 'py.test' or 'nosetests', depending on
  # which library you use
  - py.test
```

Once Travis is configured it will run your tests every time you push (this is the default configuration but you can change it if you want) and if your tests don't pass it will send you and e-mail (awesome!), you can also see the log to check which tests didn't pass in the Travis website.

When configuring Travis you may encounter some issues, feel free to open an issue on this repo if that happens so we can help you out.

## Project samples using Travis + Scientific Python

*   [Police project](https://github.com/dssg/police-eis)
*   [sklearn-evaluation](https://github.com/edublancas/sklearn-evaluation) - See this if you want to make tests that compare images since it requires a different setup

