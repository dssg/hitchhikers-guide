# Setting your machine

## Motivation

Every team will settle on a specific setup with their tech mentors. This setup will determine, for example:

- which Python version to use
- versioning via virtual environments
- maintaining package dependencies
- continuous testing tools
- your version control workflow.

Today, we're **not** doing that. We're making sure that everybody has some basic tools they will need for the tutorials and the beginning of the fellowship, and that you can log into the server and database.

!!! info "Getting help"

    Work through the prerequisites below, making sure that all the software you installed works.

    Affix three kinds of post-it notes to your laptop:

    - one with your operating system, e.g. **Ubuntu 18.04**
    - if you get an app working (e.g. `ssh`), write its name on a **green** post-it and stick it to your screen
    - if you tried - but the app failed - write its name on a **red** post-it

    If you're stuck with a step, ask a person with a corresponding green post-it (and preferrably your operating system) for help.

    The tech mentors will hover around and help with red stickers.

    You will need a few credentials for training accounts. We'll post them up front.

!!! important

    The notes below aren't self-explanatory and will not cover all (or even the majority) of errors you might encounter. Make good use of the people in the room!


!!! warning "Getting a terminal environment on a Windows Computer"

    You're going to want to access the terminal. Unfortunately, windows computers don't have this by default (yet). Fortunately, there are a couple options for obtaining a terminal-like environment, such as the following:

    - [git-bash](http://www.techoism.com/how-to-install-git-bash-on-windows/)
    - [Cygwin](https://cygwin.com/install.html)
      - If you go with cygwin, make sure to choose all git packages when you're in the package menu portion of the setup

    If you're a windows user, make sure to download one of these.

Let's get this over with!


## Package Manager

A package manager will make your life easier.

- on Mac, install [Brew](http://brew.sh/)
    - **Testing**: To check that it installed, run the command `which brew` in the terminal. If it returns: `/usr/local/bin/brew`, it means that homebrew is installed; if it returns `brew not found`, it means homebrew is not installed.

- on GNU/Linux, you probably already have `yum` (RedHat based distros)  or `apt` (Debian based distros)
    - **Testing**: run `yum help` or `apt help`

- ask Windows users around you for their preferred way to manage packages. And tell us, so we can add them here!

## Git and GitHub Account

1. If you don't have a GitHub account, [make one](https://github.com/join?source=header-home)!

2. Go to [this site](https://dssg-github-invite.herokuapp.com/), input your username, and click "Add me to organization". Your username will be automatically added to the DSSG organization on GitHub.

3. Install `git` using the appropriate OS’s package manager

??? info "MacOS"

    In the terminal, type:

    ```
    brew update
    brew install git
    ```

??? info "GNU/Linux"

    ```
    sudo apt update
    sudo apt install git
    ```


??? info "Windows"

    On Windows, you should already have git. (Either you installed **git-bash**, which is part of git, or you should have downloaded git in the **cygwin** package menu.)

4. Test your installation. For example, create a directory, and make it a git repo:

 ```
 mkdir mytestdir
 cd mytestdir/
 git init
 ```
 ```
 > Initialized empty Git repository in [...]/mytestdir/.git/
 ```
You can un-git the directory by deleting the `.git` folder: `rm -r .git` (or simply delete `mytestdir` entirely with command `rmdir mytestdir`).

## Python

As said, your team will decide on which Python version (and versioning) to install. Thus, if you have any working setup already, don't break it (for now)! Just make sure you have the packages listed below installed.

!!! warning "pyenv vs anaconda"

    This is a contentious topic! For some people the way to go, because apparently is easier is **Anaconda** (`conda` or `mini-conda`), for other, for consistency and flexibility is `pyenv`. In reality, python library’s system is a mess and in constant evolution.

    We will favor `pyenv` here, since we think is the one that allows you more flexibility and *teaches* you about how `python` works.


If you are in GNU/Linux or in MacOS you have `python` installed. But that `python` is the one use by your operative system for doing stuff, probably you don’t want to mess with it. So we will install a different `python`, for you exclusive use. First we will install some libraries[^1]:


??? info "MacOS"

    ```
    # optional, but recommended:
    brew install openssl readline sqlite3 xz zlib
    ```

??? info "GNU/Linux"

    For Debian based distros:

     ```
    sudo apt-get update; sudo apt-get install --no-install-recommends make build-essential libssl-dev zlib1g-dev libbz2-dev libreadline-dev libsqlite3-dev wget curl llvm libncurses5-dev xz-utils tk-dev libxml2-dev libxmlsec1-dev libffi-dev liblzma-dev
     ```

     For Red hat based distros:

    ```
    dnf install make gcc zlib-devel bzip2 bzip2-devel readline-devel sqlite sqlite-devel openssl-devel tk-devel libffi-devel
    ```

We will install [`pyenv`](https://github.com/pyenv/pyenv)

        $ curl https://pyenv.run | bash


And follow the instructions at the end (Mostly about adding some lines to your `.bash_profile` or `.zsh_profile` or similar.) Restart your terminal.


### Virtual environment

As a last step, we will create a *virtual environment*. 
A virtual environment is a tool that helps to keep dependencies required by different projects separate.
By default, every project on your system will use the same directory to store and retrieve third party libraries (called site packages).
A virtual environment helps avoid conflicts between requirements for different projects and it isolates dependencies.
For example, different projects may use different versions of Python.

There are multiple tools to manage virtual environments.
The most commonly used ones are 

+ `anaconda`:  Environment manager and package manager. Anaconda makes makes managing different environments, and installing packages very easy. In fact, many of the standard Data Science packages are automatically installed when setting up anaconda. However, it requires a large amount of storage space. 
+ `pyenv`: Python version manager. The focus of `pyenv` is to switch between different python versions.
+ `virtualenv`: Python environment manager. `virtualenv` is an intermediate solution between `anaconda` and `pyenv`. 


##### pyenv

To create an environment called `dssg` with Python 3.7.3 in `pyenv`, install the python version:

        $ pyenv install 3.7.3

This will take several minutes. Once complete, create the environment

    $ pyenv virtualenv 3.7.3 dssg

And then assign it as the virtual environment to use in your directory of choice with

    $ echo dssg > .python-version

Depending on your command shell (`bash`, `zsh`, `csh`, etc) configuration you should get some info that the environment is in use,  if not you can check it with

    $ pyenv version
    dssg (set by /home/user/projects/.python-version)
    
##### anaconda

To perform the same task in anaconda, type

    $ conda create -n dssg python=3.7
 
Press `y` to proceed. This wil install the Python version and all the default anaconda packages in `path_to_your_anaconda_location/anaconda/envs/dssg`

We activate the environment with 

    $ source activate dssg

Note that the active environment is visible in your command prompt.
Virtual environments are only active in the current terminal. If you ever need to deactivate it, type

    $ source deactivate


### Package installations

Packages are installed using pip. To install a single package:

    $ pip install pandas

To install many packages at once, list all the packages needed in a file (usually called `requirements.txt`), 
navigate to the folder of the file and execute

    $ pip install -r requirements.txt

To try it out, use this file: [`requirements.txt`](https://github.com/dssg/hitchhikers-guide/blob/master/sources/curriculum/0_before_you_start/prerequisites/requirements.txt).


#### Jupyter

Jupyter notebooks are a convenient environment for experimentation, prototyping, and sharing exploratory work.
Jupyter notebooks require a kernel that executes the code. It should link to the virtual environment:


    $ python -m ipykernel install --user --name=myenv --display-name "myenv"

It's time to test! In order to test that both jupyter and the python packages installed appropriately, you should do the following:

- Download the file [`SoftwareSetup.ipynb`](https://github.com/dssg/hitchhikers-guide/blob/master/sources/curriculum/setup/software-setup/SoftwareSetup.ipynb) into your directory.
- Type in the terminal

    $ jupyter notebook

Your browser will open a new tab and you will see something like the following:

<img src="imgs/jupyter.png" width="900px;"/>

- Click on `SoftwareSetup.ipynb` to open the notebook
- Follow the instructions in the notebook to run each cell.

## SSH / Putty

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




[^1]: for an updated version of this instructions see [here](https://github.com/pyenv/pyenv/wiki)
