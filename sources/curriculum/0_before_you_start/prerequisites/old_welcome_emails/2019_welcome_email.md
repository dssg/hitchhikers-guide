Hey DSSG 2019 Fellows!

We’re excited that DSSG 2019 is comning up soon!

A lot of you have expressed both excitement about the fellowship
and trepidation about being prepared. We are here to help! Here is a
guide of everything you need to install before showing up in Chicago,
on your machine as well as in your brain.

We expect everyone should at least be familiar with Python to an
intermediate level, and have some knowledge of data analysis,
computers, and stats. However, everyone comes from different
backgrounds. Make sure you have everything on the **Things to
Install** list installed, look through the **Explanations &
Tutorials** section if you don't know why/how to use any of these
tools, and check out the **Background Reading** section to brush up on
quantitative social science or machine learning (or both!) and you’ll
be ready to roll.

Cry out for help on Slack if you are having trouble! And get used to
it, you’ll be doing a lot of it over the summer (the Slacking, not the
crying).

Things to Install
-------------

- SSH (PuTTY or cygwin if you’re Windows)
- Git
- psql (PostgreSQL CLI)
- Python tools
  - Python 3.6
  - Anaconda/Miniconda or `pyenv + virtualenv`
  - Packages
    - Pandas
    - Matpotlib
    - Scikit-learn
    - Psycopg2
    - Ipython
    - Jupyter
    - Seaborn
- R (you won't need it but it may make some of you feel better)
- DBeaver *(to query databases)*
- Tableau *(get the free license for students)*
- GNU/Emacs, VIM or … Sublime Text *(if you need a decent editor)*
- **If you are an OS X user,** we recommend to install [Homebrew](osx.md#step-1-install-homebrew)
  to make software installation easier. A guide to install
  pre-requirements on OS X is available [here](osx.md).

Explanations & Tutorials
-------------

**Command Line**

You will be running code and storing project data on Amazon Web
Services (AWS) machines that run Linux, requiring the use of the
command line. If you are on Mac or Windows, you can open up Terminal
(on Mac) or download Cygwin or Putty (on Windows).

- [General command line navigation](http://linuxcommand.org/)
- [Secure Shell (ssh)](http://code.tutsplus.com/tutorials/ssh-what-and-how--net-25138): You’ll need this to connect to AWS/cloud computers. If you’re on Windows, you’ll need [putty](http://putty.org/).
- [grep/awk/sed](http://www-users.york.ac.uk/~mijp1/teaching/2nd_year_Comp_Lab/guides/grep_awk_sed.pdf): Quickly find and manipulate files, without ever leaving the command line.


**Python**

Python is the language of choice here at DSSG. If you’re only going to
learn one programming language, learn Python! It’s powerful,
expressive, and easy to read (even by non-programmers).

- **Python Package & Environment Management:** To properly create a
  Python environment, we recommend you use [Anaconda][^8] or
  [Miniconda][^9]. If you feel adventurous, feel free to use pip +
  virtualenv.
- **Python Programming Resources:**
    - [Writing efficient Python][^10]
    - [Tips for Idiomatic Python][^11]
    - [Introduction to Python debugging tools][^12]
- Jupyter Notebooks and Jupyter Lab
    - [Beginner's Guide to Jupyter Lab][^32]
    - [Example of how IPython notebooks are used in data science][^13]
    - [Tutorial for setting up and opening IPython notebook][^14]
    - [Amazing examples of IPython notebooks][^15]

[^8]: https://www.continuum.io/downloads
[^9]: http://conda.pydata.org/miniconda.html
[^10]: https://www.memonic.com/user/pneff/folder/python/id/1bufp
[^11]: https://web.archive.org/web/20180411011411/http://python.net/~goodger/projects/pycon/2007/idiomatic/handout.html
[^12]: https://web.archive.org/web/20141209082719/https://blog.safaribooksonline.com/2014/11/18/intro-python-debugger/
[^13]: http://nbviewer.ipython.org/github/jvns/talks/blob/master/pydatanyc2013/PyData%20NYC%202013%20tutorial.ipynb
[^14]: http://opentechschool.github.io/python-data-intro/core/notebook.html
[^15]: https://github.com/jupyter/jupyter/wiki/A-gallery-of-interesting-Jupyter-and-IPython-Notebooks
[^32]: https://medium.com/@brianray_7981/jupyterlab-first-impressions-e6d70d8a175d


**Databases**

- We typically use Postgres (full name PostgreSQL) for our projects
  (and Redshift or mongodb when necessary). That will be installed on
  the server but you need a client to connect to it:

   - [Dbeaver](http://dbeaver.jkiss.org/) is a free database access tool that allows you to
     easily query different types of databases.
   - [psql](http://postgresguide.com/utilities/psql.html) is a
     powerful command line tool to interact with
     Postgres databases

- [SQL introduction]( http://joshualande.com/) and [SQL
  Cheatsheet](https://gist.github.com/hofmannsven/9164408)

**Git and Github**

Working on code together is almost impossible without using a version
control system. This summer, we’ll be using Git. Our code will be
stored on Github. These are fantastic tools for any software project.

- [Installing Git](http://git-scm.com/book/en/v2/Getting-Started-Installing-Git)
- [Complete Beginner’s Guide to Git and Github](http://readwrite.com/2013/09/30/understanding-github-a-journey-for-beginners-part-1)
- [10-minute Hello World Tutorial to using Git and Github](https://guides.github.com/activities/hello-world/)
- [Github’s interactive web tutorial](https://try.github.io/levels/1/challenges/1)


**Other Useful Tools**

- Text Editors and/or IDEs: If for some **weird** reason[^1] you don’t use
  [GNU/Emacs](https://www.gnu.org/software/emacs/) or
  [VIM](https://www.vim.org), we suggest you install
  text editor  such as [Sublime Text](http://www.sublimetext.com/).
- [Tableau](http://www.tableau.com/products/desktop) is a good tool to explore and visualize data without
  using any programming. If you’re a student, you can request a free
  license.

Background Reading
-------------
- General Concepts in Machine Learning
    - [A few useful things to know about machine learning](http://homes.cs.washington.edu/~pedrod/papers/cacm12.pdf)
    - [Survey of machine learning tools for social scientists](http://people.ischool.berkeley.edu/~hal/Papers/2013/ml.pdf)
    - [Machine Learning book chapter from Big Data and Social Science](https://github.com/dssg/hitchhikers-guide/blob/master/sources/curriculum/3_modeling_and_machine_learning/machine-learning/mlchapter.pdf)
    
- Quantitative Social Science Methods
    - [Intro to Causal Inference](http://dholakia.web.rice.edu/CausalInference.pdf)
    - [Causal Inference in Social Science](http://people.ischool.berkeley.edu/~hal/Papers/2015/cause03.pdf)


[^1]: Why do you do that to yourself?
