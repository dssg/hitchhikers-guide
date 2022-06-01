Hey DSSG 2016 Fellows!

Jane Zanzig, Benedict Kuester, and Eduardo Blancas Reyes reporting. We’re SUPER stoked that DSSG 2016 is less than a month away. A lot of you have expressed both excitement about the fellowship and trepidation about being prepared. We are here to help! Here is a guide of everything you need to install before showing up in Chicago, on your machine as well as in your brain. 

We expect everyone should at least be familiar with Python (or R) to an intermediate level, and have some knowledge of data analysis, computers, and stats. However, everyone comes from different backgrounds. Make sure you have everything on the **Things to Install** list installed, look through the **Explanations & Tutorials** section if you don't know why/how to use any of these tools, and check out the **Background Reading** section to brush up on quantitative social science or machine learning (or both!) and you’ll be ready to roll.

Cry out for help on Slack if you are having trouble! And get used to it, you’ll be doing a lot of it over the summer (the Slacking, not the crying).

Things to Install
-------------

- SSH (PuTTY or cygwin if you’re Windows)
- Git
- psql (PostgreSQL CLI)
- Python tools
  - Python 3.6
  - Anaconda/Miniconda or pip + virtualenv
  - Packages
    - Pandas
    - Matpotlib
    - Scikit-learn
    - Psycopg2
    - Ipython
    - Jupyter
- R
- DBeaver *(to query databases)*
- Tableau *(get the free license for students)*
- Sublime Text *(if you need a decent editor)*
**If you are an OS X user,** we highly recommend to install [Homebrew][1] to make software installation easier.

For more information on requirements, see [this][2]. A guide to install pre-requirements on OS X is available [here][3].

[1]: https://github.com/dssg/hitchhikers-guide/blob/master/curriculum/prerequisites/osx.md#step-1-install-homebrew
[2]: https://github.com/dssg/hitchhikers-guide/tree/master/curriculum/prerequisites/
[3]: https://github.com/dssg/hitchhikers-guide/blob/master/curriculum/prerequisites/osx.md

Explanations & Tutorials
-------------

**Command Line**
You will be running code and storing project data on Amazon Web Services (AWS) machines that run Linux, requiring the use of the command line. If you are on Mac or Windows, you can open up Terminal (on Mac) or download Cygwin or Putty (on Windows).
- [General command line navigation][4]
- [Secure Shell (ssh)][5]: You’ll need this to connect to AWS/cloud computers. If you’re on Windows, you’ll need [putty][6].
- [grep/awk/sed][7]: Quickly find and manipulate files, without ever leaving the command line. 

[4]: http://linuxcommand.org/
[5]: http://code.tutsplus.com/tutorials/ssh-what-and-how--net-25138
[6]: http://putty.org/
[7]: http://www-users.york.ac.uk/~mijp1/teaching/2nd_year_Comp_Lab/guides/grep_awk_sed.pdf

**Python**

Python is the language of choice here at the Fellowship. If you’re only going to learn one programming language, learn Python! It’s powerful, expressive, and easy to read (even by non-programmers).
- **Python Package & Environment Management:** To properly create a Python environment, we recommend you use [Anaconda][8] or [Miniconda][9]. If you feel adventurous, feel free to use pip + virtualenv.
- **Python Programming Resources:**
  - [Writing efficient Python][10]
  - [Tips for Idiomatic Python][11]
  - [Introduction to Python debugging tools][12]
- Jupyter (formerly known as IPython)
  - [Example of how IPython notebooks are used in data science][13] 
  - [Tutorial for setting up and opening IPython notebook][14]
  - [Amazing examples of IPython notebooks][15]

[8]: https://www.continuum.io/downloads
[9]: http://conda.pydata.org/miniconda.html
[10]: https://www.memonic.com/user/pneff/folder/python/id/1bufp
[11]: http://python.net/~goodger/projects/pycon/2007/idiomatic/handout.html
[12]: https://blog.safaribooksonline.com/2014/11/18/intro-python-debugger/
[13]: http://nbviewer.ipython.org/github/jvns/talks/blob/master/pydatanyc2013/PyData%20NYC%202013%20tutorial.ipynb
[14]: http://opentechschool.github.io/python-data-intro/core/notebook.html
[15]: https://github.com/jupyter/jupyter/wiki/A-gallery-of-interesting-Jupyter-and-IPython-Notebooks


**R** 

R is an open-source programming language for statistical analysis, with lots of great packages for modeling and visualization. 
- [RStudio (IDE made for R)][16]
- [Shiny][17] - Shiny is a web framework for R, so that you can build interactive visualizations and web widgets. You can use this to prototype tools for project partners to visualize and understand your analyses.

[16]: http://www.rstudio.com/products/rstudio/
[17]: http://www.shinyapps.io/

**Databases**

- We typically use postgres for our projects (and Redshift or mongodb when necessary). That will be installed on the server but you need a client to connect to it:
   - [Dbeaver][18] is a free database access tool that allows you to easily query different types of databases.
   - [psql][19] is a powerful command line tool to interact with Postgres databases
- [SQL introduction][20] and [SQL Cheatsheet][21]

[18]: http://dbeaver.jkiss.org/
[19]: http://postgresguide.com/utilities/psql.html
[20]: http://joshualande.com/
[21]: https://gist.github.com/hofmannsven/9164408

**Git and Github**

Working on code together is almost impossible without using a version control system. This summer, we’ll be using Git. Our code will be stored on Github. These are fantastic tools for any software project.
- [Installing Git][22]
- [Complete Beginner’s Guide to Git and Github][23]
- [10-minute Hello World Tutorial to using Git and Github][24]
- [Github’s interactive web tutorial][25]

[22]: http://git-scm.com/book/en/v2/Getting-Started-Installing-Git
[23]: http://readwrite.com/2013/09/30/understanding-github-a-journey-for-beginners-part-1
[24]: https://guides.github.com/activities/hello-world/
[25]: https://try.github.io/levels/1/challenges/1

**Other Useful Tools**

- Text Editors and/or IDEs: Unless you prefer to program using vim/emacs, we suggest you install a general purpose text editor, such as [Sublime Text][26].
- [Tableau][27] is a good tool to explore and visualize data without using any programming. If you’re a student, you can request a free license. 

[26]: http://www.sublimetext.com/
[27]: http://www.tableau.com/products/desktop

Background Reading
-------------
- General Concepts in Machine Learning
  - [A few useful things to know about machine learning][28]
  - [Survey of machine learning tools for social scientists][29]
- Quantitative Social Science Methods
  - [Intro to Causal Inference][30]
  - [Causal Inference in Social Science][31]
  
[28]: http://homes.cs.washington.edu/~pedrod/papers/cacm12.pdf
[29]: http://people.ischool.berkeley.edu/~hal/Papers/2013/ml.pdf
[30]: http://dholakia.web.rice.edu/CausalInference.pdf
[31]: http://people.ischool.berkeley.edu/~hal/Papers/2015/cause03.pdf
