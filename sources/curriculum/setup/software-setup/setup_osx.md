# Setting up your MacOS X machine

This guide helps you walk through how to set up the various technical tools you'll need for the summer and is focused on MacOS X users (if you're on Windows, see the related [guide here](setup_windows.md); if you're on Linux, most of the instructions here should work with the appropriate package manager depending on your distribution)


## Package Manager

We'll use a package manager called Homebrew to manage the installation of many of the other tools we'll need below. To get started, install [Homebrew]](http://brew.sh/) from the terminal:

```
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
```

To check that it installed, run the command `which brew` in the terminal. If it returns: `/usr/local/bin/brew`, it means that homebrew is installed; if it returns `brew not found`, it means homebrew is not installed.

If that doesn't work, you need to add the following to your PATH:

```bash
export PATH=/usr/local/bin:/usr/local/sbin:$PATH
```

If you don't know how to do that, run this:

```bash
echo 'export PATH=/usr/local/bin:/usr/local/sbin:$PATH' >> ~/.profile
```

### Learning more about working at the command line

If you haven't used the terminal/command line much, [here are a few resources](further_resources#terminal-and-the-command-line) that might be helpful to explore.


## Git and GitHub Account

Working on code together is almost impossible without using a version control system. This summer, we’ll be using Git. Our code will be stored on Github. These are fantastic tools for any software project.

1. If you don't have a GitHub account, [make one](https://github.com/join?source=header-home)!

<!-- 2. Go to [this site](https://dssg-github-invite.herokuapp.com/), input your username, and click "Add me to organization". Your username will be automatically added to the DSSG organization on GitHub. -->

2. Install `git` using homebrew:

In the terminal, type:

```
brew update
brew install git
```

3. Test your installation. For example, create a directory, and make it a git repo:

 ```
 mkdir mytestdir
 cd mytestdir/
 git init
 ```
 ```
 > Initialized empty Git repository in [...]/mytestdir/.git/
 ```
You can un-git the directory by deleting the `.git` folder: `rm -r .git` (or simply delete `mytestdir` entirely with command `rmdir mytestdir`).

### Learning more about git

If you haven't used git/github before, [here are a couple of useful resources](further_resources#git-and-github) where you can learn a bit more.


## Python

We'll primarily use the python programming language for scripting, doing analyses, and building models throughout the summer, so let's make sure we have the right version and packages installed.

!!! warning "pyenv vs anaconda"

    This is a contentious topic! Some people argue that they find **Anaconda** (`conda` or `mini-conda`) easier to get up and running while others argue for the consistency and flexibility of `pyenv`. In general, python's library system is a bit of a mess and in constant evolution.

    We favor `pyenv` here, since we think it provides you with more flexibility and *teaches* you about how `python` works.


Note that in MacOS you will already have `python` installed, but that `python` is the one use by your operative system for doing stuff, so probably you don’t want to mess with it. Instead, we will install a different `python`, for you exclusive use. First we will install some libraries[^1]:

```
xcode-select --install
brew install openssl readline sqlite3 xz zlib
```


To manage different python versions and virtual environments, we will install a tool called [`pyenv`](https://github.com/pyenv/pyenv)

```
$ curl https://pyenv.run | bash
```

This command will generate some instructions at the end (mostly about adding some lines to your `.bashrc`, `.bash_profile` or `.zsh_profile` or similar.) Follow these then restart your terminal. Generally, this will look something like:

And add the following lines to the end of your `.bashrc`:
```
# pyenv
export PYENV_ROOT="$HOME/.pyenv"
export PATH="$PYENV_ROOT/bin:$PATH"
eval "$(pyenv init -)"
eval "$(pyenv virtualenv-init -)"
```

To test things out, **restart your terminal** then type `which pyenv` to make sure the system can find `pyenv` and `pyenv versions` to see the currently-installed python versions. Note that if you're using a shell other than `bash`, you might need to check out the [instructions here](https://github.com/pyenv/pyenv/#set-up-your-shell-environment-for-pyenv) (if you're just using the default that came with terminal, it's most likely bash).


### Virtual environment

As a last step, we will create a *virtual environment*. 
A virtual environment is a tool that helps to keep dependencies required by different projects separate.
By default, every project on your system will use the same directory to store and retrieve third party libraries (called site packages).
A virtual environment helps avoid conflicts between requirements for different projects and it isolates dependencies.
For example, different projects may use different versions of Python.

To create an environment called `dssg` with Python 3.8.2 in `pyenv`, install the python version:

    $ pyenv install 3.8.2

This will take several minutes. Once complete, create the environment

    $ pyenv virtualenv 3.8.2 dssg-3.8.2

And then assign it as the virtual environment to use in your directory of choice with

    $ echo dssg > .python-version

Depending on your command shell (`bash`, `zsh`, `csh`, etc) configuration you should get some info that the environment is in use,  if not you can check it with

    $ pyenv version
    dssg (set by /home/user/projects/.python-version)


### Package installations

Packages are installed using pip. To install a single package:

    $ pip install pandas

To install many packages at once, list all the packages needed in a file (usually called `requirements.txt`), 
navigate to the folder of the file and execute

    $ pip install -r requirements.txt

To try it out, use this file: [`requirements.txt`](requirements.txt).


#### Jupyter

Jupyter notebooks are a convenient environment for experimentation, prototyping, and sharing exploratory work.
Jupyter notebooks require a kernel that executes the code. It should link to the virtual environment:

    $ pyenv activate dssg-3.8.2
    $ python -m ipykernel install --user --name=dssg-3.8.2 --display-name "dssg-3.8.2-env"

It's time to test! In order to test that both jupyter and the python packages installed appropriately, you should do the following:

- Download the file [`SoftwareSetup.ipynb`](https://github.com/dssg/hitchhikers-guide/blob/master/sources/curriculum/setup/software-setup/SoftwareSetup.ipynb) into your directory.
- Type in the terminal

    $ jupyter lab

Your browser will open a new tab with the jupyterlab interface.

<!-- Your browser will open a new tab and you will see something like the following:

<img src="imgs/jupyter.png" width="900px;"/> -->

- Click on `SoftwareSetup.ipynb` to open the notebook
- Follow the instructions in the notebook to run each cell.

### Learning more about python

Python is a powerful, expressive, and easy to read (even by non-programmers) programming language. If you're still relatively new to it, you might find some of [the resources here](further_resources#python) helpful.


## SSH

SSH helps you access the remote servers using your laptop. For this to work, we generate a key-pair that consists of a Public Key (something that you would share with the server), and a private key (something that you would NEVER share with anyone!).

Inside your terminal, we can use a built-in utility to generate a new keypair: 

```
$ ssh-keygen
```

This will prompt you to select a location for storing the key (the default is generally fine, but you may want to give it a different name if you already have an existing keypair), and give you the option to add a passphrase to the key. If you want to use the default locaion and not use a passphrase, you just have to hit return. 

Then, your keys will be stored in the place your specified. By default, 
- there'll be a `.ssh` folder in your home directory
` ~/.ssh/`
- private key would be named `id_rsa`
- public key would be named `id_rsa.pub`

You've successfully generated the Keys!

After having generated the key pair, you should set the correct file
permissions for your private key: SSH requires that only you, the
owner, are able to read/write it, and will give you an error
otherwise. You can set the right permissions with this command:

    chmod 600 ~/.ssh/nameofyourprivatekey

(where you'll have to substitute in
the path and name of your private key that you chose during key
generation).


## Text Editor

You'll need a good text editor for all the amazing code you're going to write this summer. If you've already got one you like (vim, emacs, sublime, etc), that's great! If not, we reccomend using [VSCode](https://code.visualstudio.com/), which has some great functionality for complex projects, including github integrations and allowing you to work on files directly on a remote server. 

You can download and install VSCode [here](https://code.visualstudio.com/download).

As we said above, one of the most useful features of VSCode is that it let's you edit code directly on a remote server using SSH. To use this feature, you should [install the Remote-SSH extention for VSCode](https://code.visualstudio.com/learn/develop-cloud/ssh-lab-machines).


## Database Tools

The data for most of the projects will be stored in a PostgreSQL database, and you'll need software on your computer to be able to access it. You won't be able to access the database itself until you get to DSSG, so for now we'll just set up the tools you'll need, and then walk through setting up your connection at the beginning of the summer.

### DBeaver

There are several GUI tools for connecting to databases, including DBeaver, DataGrip, DBVizualizer, etc. For the summer, we'll prefer DBeaver, which you can install directly from the [DBeaver Website](https://dbeaver.io/download/), since it offers a free version and works with every operating system. NOTE: you'll want to install the free "community edition" version.

### psql

There is also a command-line tool for accessing postgres databases called `psql`, which can be useful for quickly or programmatically working with the database as well.

To get it, you'll need to install the `libpq` library:

```
$ brew update
$ brew install libpq
```

!!! info "Note for Linux Users"

    Most of the instructions for OS X are similar for linux. However, for installing the postgresql client on linux, they're actually a bit different:

    ```
    $ sudo apt-get update
    $ sudo apt-get install postgresql-client
    ```

Unfortunately, this won't add the location of the `psql` client to your path, so you'll need to do so manually.

If you're on an intel-based mac, this should be:

```
echo 'export PATH="/usr/local/opt/libpq/bin:$PATH"' >> ~/.bash_profile
source ~/.bash_profile
```

If you're on a mac with apple silicon (e.g. M1), this should be:

```
echo 'export PATH="/opt/homebrew/opt/libpq/bin:$PATH"' >> ~/.bash_profile
source ~/.bash_profile
```

To tesst it out, try typing `psql` into the terminal, you should see the following output. 

```
$ psql
psql: could not connect to server: No such file or directory
        Is the server running locally and accepting
        connections on Unix domain socket "/var/run/postgresql/.s.PGSQL.5432"?
```

### Learning more about databases and sql

SQL can provide a very efficient way to process large amounts of data quickly, for instance, for ingesting/cleaning raw inputs, performing data exploration, building features for modeling, and keeping track of model artifacts and results. If you're still relatively new to using relational databases, you might find some of [the resources here](further_resources#databases-and-sql) helpful.


## Congratulations -- You Made It!

Good news -- that's it in terms of software setup (for now)! 

Take some time to familiarize yourself with them before the summer, and check out the [resources here](further_resources) for some helpful guides. On that page, you'll also find some good background information on [machine learning concepts](further_resources#machine-learning-concepts) and [causal inference](further_resources#causal-inference) which may be helpful as well.


[^1]: for an updated version of this instructions and troubleshooting FAQs see [this page](https://github.com/pyenv/pyenv/wiki)
