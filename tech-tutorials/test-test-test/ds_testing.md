# Testing Python Data Science pipelines

Testing Data Pipelines is **hard**. By definition you do not expect them to produce the same output over and over again. There isn't a standard way of doing it (or at least I don't know it), but here you'll find some tips to test your pipeline steps.

## Tips to test your pipeline

### Separate the source code and your pipeline steps in different modules

As it was mentioned in [Part1](python_testing.md). It's important to separate the source code from your pipeline. Think of source code as the building blocks for processing data, uploading to the database, training models and so on. For example, the training step in your pipeline may look like this:

```python
# training step in your pipeline

# load features
train, test = load_features(['feature1', 'feature2', 'feature3'])

# get a list of models to train
to_train = load_models('RandomForest', 'LogisticRegression')

# train every model
for model in to_train:
    # fit the model
    model.fit(train.y, train.y)
    # evaluate some metrics on the test set,
    # save results in a database,
    # create HTML/PDF reports
    evaluate_model(model, test)
```

In the training step above `load_features`, `load_models` and `evaluate_model` depend on your project, maybe you are loading data from PostgresSQL, maybe from HDF5. The models you train also depend on your project and the evaluation depends on which metrics are best suited for your project's goal.

Those functions are building blocks and the *source code* for those should be outside your training script. Probably the `load_features` function does a lot of data transformations, try to divide it in various *small* functions and run *unit tests* on them.

### Make the data assumptions in your code explicit

When working on your pipeline the math/logic may work fine, but what if you are feeding the wrong data? Imagine what would happen if you train a classifier and you forgot to delete the outcome variable in your feature set, that sounds like a dumb mistake, but as your pipeline gets more and more complex, *it can happen*.

To prevent those things from happening you should *test your pipeline at runtime*, meaning that you should check for red flags while training models. Let's see an example.

```python
def load_features(list_of_features):
    """
    	This function loads features from the database
    """
    uri = load_uri()
    con = db_connection(uri)
    tables = load_from_db(list_of_features, con)
    if 'outcome' in tables:
        raise Exception('You cannot load the outcome variable as a feature')
    if any(tables, has_nas):
        raise Exception('You cannot load features with NAs')
    return tables
```

In the snippet above we are making two assumptions explicit, the first one is that we shouldn't load a column named 'outcome' in our feature set, the second one means that we cannot load columns with NAs, because this may break the following steps in our pipeline.

### Test your code with a fake database

Imagine that you implemented a function to perform some complex feature engineering in your database, then you modify some parts to make it faster and you have a test to check that the results hold the same. If your database has millions of rows and a couple hundred features, how long is the test going to take?

When testing code that interacts with a lot of data is often a good idea to sample it and put it in a test database, that way you can test faster, but don't force yourself to make your tests run fast. Always remember *a fast test is better than slow test, but a slow test is better than not testing at all*.

How do you change which database your code uses? There are a couple of ways, you can for example define an [environment variable](https://en.wikipedia.org/wiki/Environment_variable) to change the behavior of your `open_db_connection` function.

<u>Note: use environmental variables judiciously and don't store any sensitive data.</u>

```python
# db.py
import os

def db_connection():
    if os.environ['testing_mode']:
        return connect_to_testing_db()
    else:
        return connect_to_production_db()
```

Now, you need to add some custom logic to the script that runs your tests, let's see how to do it:

```bash
# run_tests.sh
export testing_mode=YES
py.test # run your tests
export testing_mode=NO
```

### Dealing with randomness

The hardest part of testing pipelines is dealing with randomness, how do you test a random generator function? or a probabilistic function? One of the simplest ways to do it is to take out the randomness by setting the [random seed](https://en.wikipedia.org/wiki/Random_seed) in your tests. Let's see an example.

```python
# random.py
def generate_random_number_between(a, b):
    # generate random number using seed value,
    # a and b
    return number
```

```python
# test_random.py

# set the seed value so you always get random numbers in the same order
# during the tests
set_random_seed(0)

def test_generate_random_number_below_10():
    assert generate_random_number_between(0, 10) == 5

def test_generate_random_number_between_8_12():
    assert generate_random_number_between(8, 12) == 10
```

The example above is a bit naive, but it hopefully gives you an idea on how to take out the randomness by setting the seed, let's see a more robust example.

Another approach is to test your function enough number and check the result against an interval and not an specific value. Let's see how to test a function that draws one sample from the normal distribution:

```python
# normal_sample.py
def normal_dist_sample(mean=0, std=1):
    # do stuff
    return sample
```

```python
# test_normal_sample.py
import numpy.testing as npt

def test_normal_dist_sample_mean():
    # draw 1000 samples
    samples = [normal_dist_sample() for i in range(10000)]
    # calculate the mean
    mean = samples.mean()
    # check that the mean is almost equal to zero
    assert npt.assert_almost_equal(mean, 0)
```

As you can see, testing probabilistic code is not trivial, so do it only when your project highly depends on such functions. But make sure you write unit tests and to check the assumptions in your data!

## Tools for testing

-   [hypothesis](https://github.com/HypothesisWorks/hypothesis-python) - Python library to look for edge cases without explicitly coding them
-   [engarde](https://github.com/TomAugspurger/engarde) - Use Python decorators to test a function outcome (this project had good potential but it's dead now)
-   [feature forge](https://github.com/machinalis/featureforge) - Testing features for ML models (also seems dead)



## External resources

*    [Testing for Data Scientists by Trey Causey](https://www.youtube.com/watch?v=GEqM9uJi64Q)



### Where to go from here

*   **Part 3:** [Continuous Integration](ci.md)
