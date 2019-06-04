### DSSG 2019 - Imperial College London

**June 2019**

#### Setting up your local machine

1. Installing Anaconda | miniconda | pyenv

**Why do I need this?**

Anaconda and miniconda are package managers, both of them use conda as their package manager. They have been very popular because they already have many of the packages that we as data scientists use on a daily basis.

Anaconda is very heavy (~3GB!) and that is why they built miniconda, which only has the package manager but no packages pre-installed (~400 MB).

Pyenv on the other hand is more flexible because its purpose is to have different python version environments coexisting in your machine without affecting each other.

Linux versions -at least Ubuntu flavors- come with python 2.7 pre-installed, -2.7 is not great for handling encodings!- and **this** python is actually used by some processes of the operating system so we don't want to mess up with that, instead we can use pyenv to create other environments with different versions of python running on them -as required- but we can add other packages as well.

The main difference between pyenv and Anaconda or miniconda is that all the packages that came in Anaconda are veryfied in versioning which means that there will be no conflict using some version of a package with other version of other packages. On pyenv it could be possible that you start to have conflicts with the versions of some packages.

You can use the one that you feel more comfortable with, I prefer to use pyenv, but understand the benefits that Anaconda and miniconda have. (You can have an environment of miniconda or anaconda within a pyenv though! -best of both worlds-)

+ Installing Anaconda:

Download Anaconda
```
curl -O https://repo.anaconda.com/archive/Anaconda3-2019.03-Linux-x86_64.sh
```
Run the Anaconda script
```
bash Anaconda3-2019.03-Linux-x86_64.sh
```
Follow the instructions and select options of installation -take care when adding to `.bashrc` or `.zshrc`.

Activate the installation
```
source ~/.bashrc
```

Test the Installation
```
conda list
```

Set up an Anaconda environment
```
conda create --name my_env python=3
```
Then activate the environment
```
conda activate my_env
```

+ Installing miniconda:

Download miniconda from [Conda site, miniconda distribution]( https://docs.conda.io/en/latest/miniconda.html) and follow the instructions.

+ Installing pyenv:

Download pyenv
```
curl https://pyenv.run | bash
```



2. Installing PyCharm

**What is it?**

Is an open source IDE -there is a paid version: enterprise- for various languages. There are more IDEs ([NINJA IDE](http://ninja-ide.org/)) but this one is simple and efficient enough.


**Why do I need this?**

+ A way to organize your work on a project(s).
+ Allows you to **debug** your scripts/workflows.
+ As you progress on your data science project -or any software project- it becomes much easier to define your scripts in parts of a pipeline -we will see that later!- and an IDE let you easily manage all the scripts that you generate.
+ It will help you to fix conflicts on a git merge! -more on that later-.
+ You can update your changes with your repository directly from here.

**Why not just a notebook?**

There is no way that you can implement a whole data science project in a couple of notebooks -if you can, please don't!-, having your work organized in modules and thinking on a pipeline (or pipelines) will be the best way to keep things simpler to administrate.


**Why not just a text editor**

Sublime and Atom have become very common for developing scripts, they even let you load a project so that you can access all your scripts on an easy way, but they lack the debug functionality.

**Installation**

Download the Community (open source) version at https://www.jetbrains.com/pycharm/

Unpack and execute the `pycharm.sh` script.
