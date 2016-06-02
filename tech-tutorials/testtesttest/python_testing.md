# Testing your Python projects

## Your first Python test

Testing in Python is fairly easy. In a real-world example, the code to test and the actual test would be in different files but let's keep it simple for now. Let's write a simple test, to make sure our function `get_answer` returns [the answer to life, the universe and everything.](http://hitchhikers.wikia.com/wiki/42)

```python
# function to test
def get_answer():
    return 42


# actual test
def test_answer_to_file_is_42():
    assert get_answer() == 42
```

This is pretty simple, the function is just a normal Python function and the test is another function that calls `get_answer`. The interesting part here is the keyword `assert`, which evaluates a condition, if the condition evaluates to `True` we say that *the test passed* if returns `False` we say *the test failed*.

There are many types of tests, the case above is what's called a *unit test*, the names comes from the notion that we are testing a *unit of code*, we are not testing our entire project, we are just testing one single thing, the function `get_answer`.

Software testing is an entire subject on its own but keep it simple for now and follow these when writing your tests:

*   Your tests should check only for one thing (a function for example)
*   Your tests should be independent of other tests
*   Given the same input, your test should always return the same assertion (when testing the modeling step in a Data Science pipeline this gets tricky given its probabilistic nature)

## Running tests with `py.test`

One of the best tools for testing in Python is `pytest`, it provides some useful features to reduce the amount of code for your tests and also a command to find and run them.

Install it with `pip`.

```bash
pip install pytest
```

If you want to actually run the test above, you need to get a copy of this repo.

```bash
git clone https://github.com/dssg/hitchhikers-guide
cd hitchhikers-guide
```

To run your tests (note the dot in the middle):

```
py.test
```

`pytest` will look for all the tests in your project. In our case there's a copy of our test called `test_meaning.py` on this folder.

The output should look like this:

```
==================== test session starts ===========================
platform darwin -- Python 3.5.1, pytest-2.9.1, py-1.4.31, pluggy-0.3.1
rootdir: stuff/hitchhikers-guide/tech-tutorials/testtesttest, inifile:
collected 1 items

test_life.py .

==================== 1 passed in 0.01 seconds =======================
```

Now, imagine that we accidentally modify our function to:

```python
# function to test
def get_answer():
    return 41
```

If we run `py.test` again, we'll see the following:

```
======================== test session starts ====================
platform darwin -- Python 3.5.1, pytest-2.9.1, py-1.4.31, pluggy-0.3.1
rootdir: /Users/Edu/development/dsapp/hitchhikers-guide/tech-tutorials/testtesttest, inifile:
collected 1 items

test_meaning.py F

============================== FAILURES ========================
__________________ test_answer_to_file_is_42 __________________

    def test_answer_to_file_is_42():
>       assert get_answer() == 42
E       assert 41 == 42
E        +  where 41 = get_answer()

test_meaning.py:8: AssertionError
===================== 1 failed in 0.02 seconds ==================
```

We can see from the output that our test failed.

## Where to store your tests

The are no strict rules on where to store your tests. Specifically talking about a Data Science project, you are going to have a lot of folders with code for many tasks (e.g. etl, modeling). The first to take into account is to separate your scripts from your source code, simply speaking, source code are those functions and classes that you want to reuse in various steps of your pipeline (e.g. creating a database connection). Let's see an example to make this clear:

```
.
├── docs
│   └── documentation_here.txt
├── etl
│   └── code_to_load_to_db.txt
├── evaluation
│   └── code_to_evaluate_models_here.txt
├── exploration
│   └── jupyter_notebooks_with_cool_plots_here.txt
├── features
│   └── code_to_generate_features_here.txt
├── lib
│   ├── lib
│   │   ├── __init__.py
│   │   ├── db
│   │   │   ├── __init__.py
│   │   │   ├── load.py
│   │   │   └── process.py
│   │   └── util.py
│   └── tests
│       ├── test_db.py
│       └── test_util.py
└── model
    └── code_to_train_models_here.txt
```

In the diagram above, you can see the different steps in your pipeline (ETL, exploration, feature generation, modeling, model evaluation) all those folders will contain a mix of Python, shell and SQL **scripts**. Then, there's another folder called `lib`, which stores the source code for this project. Inside such folder, you'll find another two folders `lib` and `tests`, the first one stores the actual source code and the later stores the tests for that source code.

Of course, that doesn't mean you should limit your tests to your source code! You should also test your pipeline, but a good designed pipeline will put the complicated parts in the source code so your pipeline steps are easy to read, modify and test.

The problem with testing pipeline is that many steps won't be deterministic, but there are some things you can do. [See this for more info](ds_testing.py).

**Tip:** To access the code in `lib` you can either create a `setup.py` file to install or add the folder to your `PYTHONPATH`.

## Where to go from here

*   Read the pytest documentation

## Tools

*   unittest (part of the Python standard library)
*   [py.test](http://pytest.org/latest/) (if you don't know which to use, use this)
*   [nose](https://github.com/nose-devs/nose)
