# Python with SQL and Pandas

We will need to import the virtual environment in which we are working to jupyter, so that we work with the same packages -and versions of those- within jupyter. To do that, go to `/mnt/data/projects/food_inspections/` and type the following command:

```
$ python -m ipykernel install --user --name=food_inspections --display-name food_inspections
```

Also, since we are going to connect to the database through Python we will need to chage some environment variables.

```
$ nano ~/.bashrc
```

Add your credentials for the variables: `PGUSER`, `PGPASSWORD`, `PGHOST`, `PGPORT`, and `PGDATABASE`. For example:

```
export PGUSER='yourandrewid'
export PGPASSWORD='yourandrewid'
export PGHOST='db.dssg.io'
export PGPORT=5432
export PGDATABASE='food-inspections'
```

Then make these variables available to the session:

```
$ source ~/.bashrc
```


Start a Jupyter notebook, remember to use a port available from the list `ss -tulnp`:

```
$ jupyter notebook --port {XXXX}
```

Make a port forwarding between your local machine and the server so that we can use the browser in your machine as GUI.

```
$ ssh localhost:{YYYY}:localhost:{XXXX} andrewid@training.dssg.io
```

Open your browser and open the URL `localhost:{YYYY}` it will ask for a token.

[Let's code!](./python_sql_pandas_viz.ipynb)

----



Python is the language of choice here at DSSG. If you’re only going to
learn one programming language, learn Python! It’s powerful,
expressive, and easy to read (even by non-programmers).

## Python Package & Environment Management


  - To properly create a python environment, we recommend you use [Pyenv](https://github.com/pyenv/pyenv) or [Anaconda](https://www.continuum.io/downloads) /
  [Miniconda](http://conda.pydata.org/miniconda.html).

## Some e-books

- [Think Python](https://greenteapress.com/wp/think-python-2e/) An amazing book from Allen B. Downey.
  - Also check all of his book series [*Think …*](http://greenteapress.com/)!
- [Lectures in Quantitative Economics](https://lectures.quantecon.org/py/) A Econometrics  web course with `python` code
- [A tutorial for Economists](http://www.alexmbell.com/python-tutorial-for-economists/) A short (34 pages!) intro to python
- [Python for Informatics - Exploring Information](https://www.pythonlearn.com/book.php#python-for-informatics) A more traditional (CS) approach


## More Python resources

- [Writing efficient Python](https://www.memonic.com/user/pneff/folder/python/id/1bufp)
- [Tips for Idiomatic Python](https://web.archive.org/web/20180411011411/http://python.net/~goodger/projects/pycon/2007/idiomatic/handout.html)
- [Introduction to Python debugging tools](https://web.archive.org/web/20141209082719/https://blog.safaribooksonline.com/2014/11/18/intro-python-debugger/)
- Jupyter Notebooks and Jupyter Lab
    - [Beginner's Guide to Jupyter Lab](https://medium.com/@brianray_7981/jupyterlab-first-impressions-e6d70d8a175d)
    - [Example of how IPython notebooks are used in data science](http://nbviewer.ipython.org/github/jvns/talks/blob/master/pydatanyc2013/PyData%20NYC%202013%20tutorial.ipynb)
    - [Tutorial for setting up and opening IPython notebook](http://opentechschool.github.io/python-data-intro/core/notebook.html)
    - [Amazing examples of IPython notebooks](https://github.com/jupyter/jupyter/wiki/A-gallery-of-interesting-Jupyter-and-IPython-Notebooks)
