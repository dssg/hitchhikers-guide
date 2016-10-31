# Introduction to Data Analysis in Python

## Background and Motivation

Python is a high-level interpreted general purpose programming language named after
a British Comedy Troupe, created by Guido van Rossum (Python's benevolent dictator
for life), and maintained by a international group of python enthusiasts. *In a python
interpreter type import this to read Python's guiding principles.* 

As of the time of this writing (10/2016) python is currently the fifth most popular
programming language. It is popular for data science due to being powerful, fast, 
playing well with others, runs everywhere, easy to learn, highly-readable, open-source,
and its fast development time compared to other languages. Because of its general-purpose 
and ability to call compiled languages like FORTRAN or C it can be used for full-stack development.
There is a growing and every improving list of open-source libraries for scientific programming, 
data manipulation, and data analysis (e.g. NumPy, SciPy, Pandas, Scikit-Learn, Statsmodels
Matplotlib, Seaborn, PyTables, etc.)

IPython is an enhanced, interactive python interpreter that started as a grad school project
by Fernando Perez. The IPython project then evolved into the IPython notebook that would allow 
users to archive their code, figures, and analysis in a single document making doing reproducible 
computational research and sharing said research much easier. The creators of the IPython notebook 
quickly realized that the "notebook" aspects were agnostic to a specific programming language and
ported the notebook to other languages include but not limited to Julia, Python and R. This then led
to a rebranding known as the Jupyter Project. 


The Pandas library, created by Wes McKinney, introduced the R-like dataframe object in Python making
working with data in Python much easier. 

This tutorial will go over over the basics of Data Analysis in Python using the PyData stack. 


## Getting started with Jupyter Notebooks

To start up a Jupyter notebook server, simply navigate to the directory where you want the 
notebooks to be saved and run the command
```
jupyter notebook
```
A browser should open with a notebook navigator. Click the "New" button and select "Python 2".
A beautiful blank notebook should open in a new tab
Name the notebook by clicking on "Untitled" at the top of the page.
Notebooks are sequences of cells. Cells can be markdown, code, or raw text. 
Change the first cell to markdown and briefly describe what you are going to do in the notebook.

## Running a remote Jupyter Server

You can also run a Jupyter server from a remote machine (e.g, EC2 Instance) and forward the
notebook to your local machine. This is preferable if you need to access a large amount of data
on a database. Your work will also be saved on a server that is periodically backed-up which will 
make your work immune to computer-crashes/someone-stealing-your-computer/(some)acts-of-god.

Basic port forwarding:
```
ssh -L 44444:localhost:44444 <username>@<instance-name>.dssg.io
```
Now go to the location in the file system you would like to launch a Jupyter server and type

```
jupyter notebook --no-browser --port 44444
```

You should now be able to go to your browser and go to the address `localhost:44444`. 

> **Note**:The port *44444* is an arbitrary port. If another user is running a server with 
> the same port forwarding then you will not be able to run a Jupyter Server using that port. 
> You will then need to switch to another port number. Anything between 30000-70000 should work
