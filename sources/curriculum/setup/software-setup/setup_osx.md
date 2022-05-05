# Setting your machine

This guide helps you walk through how to set up the various technical tools you'll need for the summer and is focused on MacOS X users (if you're on Windows, see the related [guide here](setup_windows.md); if you're on Linux, most of the instructions here should work with the appropriate package manager depending on your distribution)

## Package Manager

We'll use a package manager called Homebrew to manage the installation of many of the other tools we'll need below. To get started, install [Homebrew]](http://brew.sh/) from the terminal:

```
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
```

To check that it installed, run the command `which brew` in the terminal. If it returns: `/usr/local/bin/brew`, it means that homebrew is installed; if it returns `brew not found`, it means homebrew is not installed.

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

This command will generate some instructions at the end (mostly about adding some lines to your `.bash_profile` or `.zsh_profile` or similar.) Follow these then restart your terminal. Generally, this will look something like:

Add the following lines to your `.bash_profile` (before `.bashrc` is sourced):
```
# pyenv
export PYENV_ROOT="$HOME/.pyenv"
export PATH="$PYENV_ROOT/bin:$PATH"
eval "$(pyenv init --path)"
```

And add the following lines to the end of your `.bashrc`:
```
# pyenv
eval "$(pyenv init -)"
eval "$(pyenv virtualenv-init -)"
```

To test things out, **restart your terminal** then type `which pyenv` to make sure the system can find `pyenv` and `pyenv versions` to see the currently-installed python versions.


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

Your browser will open a new tab and you will see something like the following:

<img src="imgs/jupyter.png" width="900px;"/>

- Click on `SoftwareSetup.ipynb` to open the notebook
- Follow the instructions in the notebook to run each cell.

### Learning more about python

Python is a powerful, expressive, and easy to read (even by non-programmers) programming language. If you're still relatively new to it, you might find some of [the resources here](further_resources#python) helpful.

## SSH

### SSH keys

You need to generate a SSH key pair. To do this, follow the
instructions on GitHub, namely 'Generating a new SSH key' and 'Adding
your SSH key to ssh-agent'. Windows users probably want to use git
bash or PuTTYgen (if you're on Linux or OS X, your standard terminal
should be the bash shell you need).

The steps in 'Generating a new SSH key' create two new files (by
default in ~/.ssh/: One without a file extension (by default, it's
called id_rsa), and one with the extension .pub. The latter one is
your _pub_lic key, which you will share with your project server, so
that it can recognize you; the former is your private key, which you
must not share with anybody, as it will let you access your project
server.

After having generated the key pair, you should set the correct file
permissions for your private key: SSH requires that only you, the
owner, are able to read/write it, and will give you an error
otherwise. You can set the right permissions with this command:

    chmod 600 ~/.ssh/nameofyourprivatekey

(where you'll have to substitute in
the path and name of your private key that you chose during key
generation).


### Testing it

Use your username and server's address to ssh into the server:

    ssh yourusername@serverurl

Once you enter your password, you should be dropped into a shell on the server:

    yourusername@servername: ~$


!!! important "PRO tip"

    Your life will be easier if you set up a [`.ssh/config` file](ssh_config.example)


## PSQL

The database server runs Postgres 9.5.10.

??? info "For Windows users"

    Windows users should skip the steps below, and instead use [DBeaver](http://dbeaver.jkiss.org/). When setting up the connection in DBeaver, you will need to specify the SSH tunnel; the database credentials are the ones we shared with you, and the SSH tunnel credentials are the ones you used in the previous step to SSH into the training server. Alternatively, everybody can access `psql` from the training server: SSH into the training server as in the step before, then, on the server's shell, call `psql -h POSTGRESURL -U USERNAME -d DBNAME`, where you need to substitute `POSTGRESURL` with the postgres server's address, `USERNAME` with your database username, and `DBNAME` with the name of the database.



For all non-Windows users, also do these steps to access the PostgreSQL server from your local machine. First we need to install the *database client*, `psql`


??? info "MacOS"

    Make sure you have the `psql` client installed; on Mac, this would be

    ```
    $ brew tap-pin dbcli/tap
    $ brew install pgcli
    ```

    Note, we are installing `pgcli` instead of `psql`, but apparently there is no way of install *just* the client without installing the whole database server.

    If you still want to give it a shot:

    ```
    $ brew postgres
    ```


??? info "GNU/Linux"

    On Debian based distros:

    ```
    sudo apt install postgresql-client libpq-dev
    ```


Once you have the postgres client installed, you can access the training database with it. However, the database server only allows access from the training server. Thus, you need to set up an *SSH tunnel* through the training server to the Postgres server:

 ```
 $ ssh -NL localhost:8888:POSTGRESURL:5432 ec2username@EC2URL
 ```

where you need to substitute `POSTGRESURL`, `ec2username`, and `EC2URL` with the postgres server's URL, your username on the training server, and the training server's URL respectively. Also, you should substitute `8888` with a random number in the 8000-65000 range of your choice (port `8888` might be in use already).

 This command forwards your laptop's port 8888 through your account on the EC2 (EC2URL) to the Postgres server port 5432. So if you access your local port 8888 in the next step, you get forwarded to the Postgres server's port 5432 - but from the Postgres server's view, the traffic is now coming from the training server (instead of your laptop), and the training server is the only IP address that is allowed to access the postgres server.


 ![](https://cdn-images-1.medium.com/max/1000/1*0JaPjL3O5Se96b7IGt5P_A.png)
 *Figure. A graphical representation of a ssh tunnel. Not quite our situation -they are using a MySQL db who knows why-, but it is close enough. Courtesy from this [Medium post](https://myopswork.com/ssh-tunnel-for-rds-via-bastion-host-6659a48edc).*


Connect to the Postgres database on the forwarded port

```
$ psql -h localhost -p 8888 -U USERNAME -d DBNAME
```

where you need to replace `USERNAME` with the postgres [!] username, `DBNAME` with the name of your database, and the `8888` with the number you chose in the previous step. You then get prompted for a password. This is now the postgres server asking, so you need to reply with the corresponding password!

This should drop you into a SQL shell on the database server.

!!! note

    In some configurations, you'll need to explicitly assume a role to do anything beyond connecting to the database. To make changes to the training database, use the `training_write` role. Let's test it by creating and dropping a schema:

    ```
    set role training_write;
    create schema jsmith;
    drop schema jsmith;
    ```

!!! important "PRO tip"

    You could save a lot of keystrokes if you setup a [`.pgservice.conf`](./pgservice_conf.example)file  and a [`.pgpass`](./pgpass.example) file in your `$HOME` folder.

    Then you could simply type

    ```
    $ psql service=mydb  # mydb is the name of the dbservice
    ```






??? info "I really prefer a GUI"

    if you want a graphical interface to databases - you might  want to use [DBeaver](http://dbeaver.jkiss.org/).




[^1]: for an updated version of this instructions and troubleshooting FAQs see [this page](https://github.com/pyenv/pyenv/wiki)
