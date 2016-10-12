# Best Practices: Writing Legible, Good Code

## Motivation
All fellows will have to write code that is usable and understandable by their peers and partners, and potentially other 3rd parties. What does that entail in practice? Many 
fellows are coming from academic backgrounds, have programming skills that are self-taught, and have never worked collaboratively on a software project before. We want to help 
them establish good habits and avoid common mistakes.

---

# There is only one law of good coding:  **Code is for humans, not for computers**

---

# What you write

```python
def fib(n):
    """
    :param int n: The Fibonnaci index you want to return
    :return: The nth Fibonnaci number
    :rtype: int
    """
    if n < 2:
        return 1
    else:
        return fib(n - 1) + fib(n - 2)
```

---

# What the computer sees

```
  2           0 LOAD_FAST                0 (n)
              3 LOAD_CONST               1 (2)
              6 COMPARE_OP               0 (<)
              9 POP_JUMP_IF_FALSE       16

  3          12 LOAD_CONST               2 (1)
             15 RETURN_VALUE

  5     >>   16 LOAD_GLOBAL              0 (fib)
             19 LOAD_FAST                0 (n)
             22 LOAD_CONST               2 (1)
             25 BINARY_SUBTRACT
             26 CALL_FUNCTION            1
             29 LOAD_GLOBAL              0 (fib)
             32 LOAD_FAST                0 (n)
             35 LOAD_CONST               1 (2)
             38 BINARY_SUBTRACT
             39 CALL_FUNCTION            1
             42 BINARY_ADD
             43 RETURN_VALUE
             44 LOAD_CONST               0 (None)
             47 RETURN_VALUE
```

---

# Seriously, the code is for *you*...

* ...one month from now when you've completely forgotten what the heck `alpha` was...
* ...or tomorrow when your teammate wonders why all those `3`s are in the database....
* ...or when your system is on fire at 2am (the witching hour of production systems), you're tired, and your customers are calling wondering what the heck is going on over there...
* ...or when I'm doing code review for you...

---

# The Only Law of Good Coding

## **Code is for humans, not for computers**

---

# The First Consequence of the Only Law

# Give things informative names

```python
import math  
  
def doit(x):  
    output = []  
    y = 2  
    while x != 1:  
        if x % y == 0:  
            output.append(y)  
            x //= y  
        else:  
            y += 1  
            continue  
    return output  
```

```ruby
def magic(input):
    filter = set()
    return sorted(x for x in y 
                    for y in input 
                    if (len(x) < 20 and x not in filter) or filter.add(x))
```





```ruby
def pretty_pictures():
    df = pd.read_csv('2016.csv.gz', names=['STATION', 'DATE', 'TYPE', 'VALUE', 
                                           'MEASUREMENT_FLAG', 'QUALITY_FLAG', 
                                           'SOURCE_FLAG', 'OBS_TIME'])
    first = df[weather_df.STATION == 'US1ILCK0010']
    first[first.TYPE == 'PRCP']['VALUE'].plot()
    plt.title("Precipitation values")
    plt.xlabel("Day")
    plt.ylabel("Value")
    plt.savefig('first_fig.png')

    second = df[weather_df.STATION == 'US1ILCK0014']
    second[second.TYPE == 'PRCP']['VALUE'].plot()
    plt.title("Precipitation values")
    plt.xlabel("Day")
    plt.ylabel("Value")
    plt.savefig('second_fig.png')

    return first[first.TYPE == 'PRCP'].mean(), second[second.TYPE == 'PRCP'].mean()
```

# Give things informative names

* Names should have meaning to the intended readers, e.g.,
  * You a week from now
  * Your teammates tomorrow
  * Your future teammates who have to deal with your code
* .green[`i`, `j`, `k`] for iterators are OK, .red[`alpha`] with a reference to a specific paper is not
* kwargs are a great place to name things
* CONSTANT_VALUES are too
* Do not fear long names; you have autocomplete

---

# The Second Consequence of the Only Law
# Document inputs and outputs
```ruby
import math  
  
def factor(x):  
    output = []  
    fact = 2 
    while x != 1:  
        if x % fact == 0:  
            output.append(y)  
            x //= fact 
        else:
            fact += 1
            continue
    return output
```



```ruby
def unique_flatten(the_input, max_length=20):
    flattened_set = {val for val in row for row in the_input}
    filtered_list = [val for val in flattened_set if len(val) < max_length]
    filtered_list.sort()
    return filtered_list
```





```ruby
WEATHER_HEADERS = ['STATION', 'DATE', 'TYPE', 'VALUE', 
                   'MEASUREMENT_FLAG', 'QUALITY_FLAG', 
                   'SOURCE_FLAG', 'OBS_TIME']

PRECIPITATION_TYPE = 'PRCP'
CHICAGO_STATION_NAMES = ['US1ILCK0010', 'US1ILCK0014']

def precipitation_in_chicago():
    df = pd.read_csv('2016.csv.gz', names=WEATHER_HEADERS)
    first = df[weather_df.STATION == CHICAGO_STATION_NAMES[0]]
    first[first.TYPE == PRECIPITATION_TYPE]['VALUE'].plot()
    plt.title("Precipitation values")
    plt.xlabel("Day")
    plt.ylabel("Value")
    plt.savefig('first_fig.png')

    second = df[weather_df.STATION == CHICAGO_STATION_NAMES]
    second[second.TYPE == PRECIPITATION_TYPE]['VALUE'].plot()
    plt.title("Precipitation values")
    plt.xlabel("Day")
    plt.ylabel("Value")
    plt.savefig('second_fig.png')

    return (first[first.TYPE == PRECIPITATION_TYPE].mean(), 
            second[second.TYPE == PRECIPITATION_TYPE].mean()) 
```

---

# Document inputs and output

* Every function should have a docstring
* The docstring should
  1. Describe the function briefly
  2. Explicitly document the inputs with .green[`:param type name: description`]
  3. Explicitly document the return value with .green[`:returns: description`]
  4. Explicitly document the return type with .green[`:rtype:`]

---

# The Third Consequence of the Only Law

## Don't repeat yourself (DRY)


# DRY

```python
def max_intersection(left, right):
    """
    Compute the value counts of the left and right lists and then return
    the maximum for each value.

    :param list[object] left: The left list
    :param list[object] right: The right list
    :rtype: dict[object, int]
    :return: A dictionary from the value to
        max(# occurrences in left, # occurrences in right)
    """
    left_counts = {}
    for val in left:
        if left not in left_counts:
            left_counts[val] = 1
        else:
            left_counts[val] += 1

    right_counts = {}
    for val in right:
        if right not in right_counts:
            right_counts[val] = 1
        else:
            right_counts[val] += 1

    left_counts.update({key: max(left_counts.get(key, 0), val)
                        for key, val in right_counts.items()})
    return left_counts
```

---

# DRY (or others!)

```ruby
def value_counts(the_list):
    """
    :param list[object] the_list: The list whose values we'll count
    :rtype: dict[object, int]
    :return: A dict from the value to its count
    """
    output = {}
    for val in the_list:
        if val not in output:
            output[val] = 1
        else:
            output[val] += 1

def max_intersection(left, right):
    """
    Compute the value counts of the left and right lists and then return
    the maximum for each value.

    :param list[object] left: The left list
    :param list[object] right: The right list
    :rtype: dict[object, int]
    :return: A dictionary from the value to
        max(# occurrences in left, # occurrences in right)
    """
    left_counts = value_counts(left)
    right_counts = value_counts(right)

    left_counts.update({key: max(left_counts.get(key, 0), val)
                        for key, val in right_counts.items()})
    return left_counts
```

---

# DRY (or others!) (example solution)

```ruby
from collections import Counter

def max_intersection(left, right):
    """
    Compute the value counts of the left and right lists and then return
    the maximum for each value.

    :param list[object] left: The left list
    :param list[object] right: The right list
    :rtype: dict[object, int]
    :return: A dictionary from the value to
        max(# occurrences in left, # occurrences in right)
    """
    left_counts = Counter(left)
    right_counts = Counter(right)

    left_counts.update({key: max(left_counts.get(key, 0), val)
                        for key, val in right_counts.items()})
    return left_counts
```

---

# DRY

```ruby
def precipitation_in_chicago():
    """ Saves plots of the precipitation from two Chicago weather stations
    in 2016 to `first_fig.png` and `second_fig.png` and returns the mean
    precipitation at them for the year.

    :return: The mean precipitation at two weather stations in 2016
    :rtype: (float, float)
    """
    df = pd.read_csv('2016.csv.gz', names=WEATHER_HEADERS)
    first = df[weather_df.STATION == CHICAGO_STATION_NAMES[0]]
    first[first.TYPE == PRECIPITATION_TYPE]['VALUE'].plot()
    plt.title("Precipitation values")
    plt.xlabel("Day")
    plt.ylabel("Value")
    plt.savefig('first_fig.png')

    second = df[weather_df.STATION == CHICAGO_STATION_NAMES[1]]
    second[second.TYPE == PRECIPITATION_TYPE]['VALUE'].plot()
    plt.title("Precipitation values")
    plt.xlabel("Day")
    plt.ylabel("Value")
    plt.savefig('second_fig.png')

    return (first[first.TYPE == PRECIPITATION_TYPE].mean(), 
            second[second.TYPE == PRECIPITATION_TYPE].mean())
```

---

# DRY (example solution)

```ruby
def plot_precipitation(df, station_id, output_file='out.png'):
    """ Plot the preciptation at the passed weather station and return
    the mean precipitation among all values.

    :param pd.DataFrame df: NOAA data (see parsers.py for more info)
    :param str station_id: The station to plot
    :param str output_file: Where to store the output plot
    :return: The mean precipitation in the data frame
    :rtype: float
    """
    res_df = df[df.STATION == station_id]
    res_df[res_df.TYPE == PRECIPITATION_TYPE]['VALUE'].plot()
    plt.title("Precipitation values")
    plt.xlabel("Day")
    plt.ylabel("Value")
    plt.savefig(output_file)

    return res_df['VALUE'].mean()


def precipitation_in_chicago():
    """ Saves plots of the precipitation from two Chicago weather stations
    in 2016 to `first_fig.png` and `second_fig.png` and returns the mean
    precipitation at them for the year.

    :return: The mean precipitation at two weather stations in 2016
    :rtype: (float, float)
    """
    df = pd.read_csv('2016.csv.gz', names=WEATHER_HEADERS)
    return (plot_precipitation(df, CHICAGO_STATION_NAMES[0], output_file='first_fig.png'),
            plot_precipitation(df, CHICAGO_STATION_NAMES[1], output_file='second_fig.png'))    
```

---

# DRY

* Use functions to not repeat yourself
* Good rule of thumb: If you've gone .red[20 lines without making a comment] (e.g., the .green[docstring] of a function), you likely should add one.

---

# The Fourth Consequence of the Only Law

## Reduce Cognitive Load: Follow PEP-8

---



```python
def GCD(a,b):
   """Return the GCD of a and b"""
   a,b=max(a,b),min(a,b)
   return b if a%b==0 else GCD(b,a%b)
```

```python
def gcd(a, b):
    """Return the GCD of a and b
    
    :param int a: The first number (positive)
    :param int b: The second number (positive)
    :return: The GCD of a and b
    :rtype: int
    """
    if a < b:
        b, a = a, b

    if a % b:
        return gcd(b, a%b)

    return b
```

---

# PEP-8 is your friend

## What makes this one better?

```python
def gcd(a, b):
    """Return the GCD of a and b
    
    :param int a: The first number (positive)
    :param int b: The second number (positive)
    :return: The GCD of a and b
    :rtype: int
    """
    if a < b:
        b, a = a, b

    if a % b:
        return gcd(b, a%b)

    return b
```

---

# PEP-8 is your friend

* 79 character lines
* function_names are snake_case
* ClassNames are CamelCase
* CONSTANT_NAMES are BIG_CASE
* One statement per line
* Use spaces not tabs!

---

# The Only Law of Good Coding

## Code is for humans, not computers

* Give things informative names
* Document inputs and outputs
* Don't repeat yourself (or others!)
* PEP-8 is your friend

---

# Fix this class!

```ruby
class myclass(object):
    def __init__(self, R, I):
        self.R = R
        self.I = I

    def Multiply(self, other):
        return myclass(self.R * other.R - self.I * other.I,
                       self.R * other.I + self.I * other.R)
```
---

# Fix this function!

```ruby
def bang(n):
    return n == 1 or (n * bang(n))
```

---

# Fix this function!

```ruby
def read_data(filename):
    """ Return the precipitation field from the csv passed in """
    with open(filename, 'r') as f:
        return [line.split(',')[2] for line in f]
```
