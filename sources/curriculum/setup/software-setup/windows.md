
## Installing DSSG Prerequisites on Windows 10/11

We would do the following in this guide

1. Generate an SSH keypair
2. Install Git and setup a Github profile if you don't already have one
3. Install Python
4. Install pyenv + virtualenv to help manage different versions of Python and python packages on your machine
5. Install several necessary python packages
6. Install VSCode, a text editor that can help you edit code on your machine and on the server directly
7. Install DBeaver, a GUI based DB explorer
8. How to use command line tools on windows


In addition, we'll recommend a few other pieces of software that we recommend that you install, but not absolutely critical. 


### Windows Subsystem for Linux (WSL)

Before we get to the specific software installations, let's explore a feature from newer versions of windows have the option of running a linux environment directly on windows. You can [learn more about WSL here](https://docs.microsoft.com/en-us/windows/wsl/about).

Today we'll show you how to use command line tools on both Windows Power Shell, and on WSL.

First we have to install WSL on Windows. We'll give you the quick installation guide, if you want to customize things, please refer the [detailed installation guide](https://docs.microsoft.com/en-us/windows/wsl/install).

First, open a PowerShell or a Command Prompt Window as an Administrator. Next, we can see the available Linux distributions for install by using:

```
wsl --list --online
```

Then, you can install the version of Linux you would like to install. We recommend picking one of the Ubuntu distributions (because it's the most popular) and our guide will assume Ubuntu installation for WSL. 

We can install Ubuntu 20.04 by:

```
wsl --install -d Ubuntu-20.04
```

This will take a few minutes, and will prompt you to provide a UNIX username and a password. Please note that you might have to restart your computer at some point during the installation for things to take full effect. 

Now, you can use Linux from within your Windows machine. You should have a shortcut in your start menu to launch WSL, and when you launch it should open up a CLI. 

 Note that this will have no GUI and you'll have to rely on the CLI. If you need to access the file system of WSL through the Windows File Explorer, you can type the following in the address bar of the File Explorer. 

```
\\wsl.localhost\Ubuntu-20.04
```

This will take you to the root folder of the linux file system. 

_Note - Appending `\home\<username>` to the above command will take you to your home directory._

For the next few pieces of software, we'll provide you instructions on how to run things on both WSL and on 'pure' Windows. 




### Git and GitHub Account

1. If you don't have a GitHub account, [make one](https://github.com/join?source=header-home)!

2. Install Git on your machine

Git comes preinstalled with WSL. Therefore, nothing to do here. When you type in the command `git` to the terminal, it should show you a long output that starts with the following

```
$ git
usage: git [--version] [--help] [-C <path>] [-c <name>=<value>]
           [--exec-path[=<path>]] [--html-path] [--man-path] [--info-path]
           [-p | --paginate | --no-pager] [--no-replace-objects] [--bare]
           [--git-dir=<path>] [--work-tree=<path>] [--namespace=<name>]
           <command> [<args>]
```

If you don't see this output by any chance, you can install git by using the following commands:

```
$ sudo apt-get update
$ sudo apt-get install git
```




In windows, you can [download and install Git by going to this link](https://git-scm.com/download/win) 




## Setting up Python and Related Tools

Your WSL system should come with `python` preinstalled. With some distros it does not, you can install system level python. But this is NOT necessary as we won't be using this version of Python anyway. 

```
$ sudo apt-get install python
```

Allow it to restart services when prompted. Once installed, you should be able to try it out.

```
$ python
Python 2.7.17 (default, Mar 18 2022, 13:21:42)
[GCC 7.5.0] on linux2
Type "help", "copyright", "credits" or "license" for more information.
>>>
```

Now you have system level Python installed. But, we don’t want to mess with it. So we will install a different python, for your exclusive use. 

First, we will install some libraries

```
$ sudo apt-get update
$ sudo apt-get install --no-install-recommends make build-essential libssl-dev zlib1g-dev libbz2-dev libreadline-dev libsqlite3-dev wget curl llvm libncurses5-dev xz-utils tk-dev libxml2-dev libxmlsec1-dev libffi-dev liblzma-dev
```

Some of these might be already installed, but good to make sure. 

It's good to be able to manage different versions of Python on your dev environment (different projects you work on might require different versions of Python). We recommend using `pyenv` as the python version manager. 

```
$ curl https://pyenv.run | bash
```

Once this finishes, you will see some instructions at the end for adding `pyenv` to the load path. To do this, we update a dot file on your home drive named `.bashrc`[^1].

[^1]: [More info about the .bashrc file](https://www.linuxfordevices.com/tutorials/linux/bashrc-and-bash-profile)

You can open and edit your bashrc file using either `vi` or `nano`. If you are not familiar with either, use `nano`.

```
$ nano ~/.bashrc
```

navigate to the end of the file, and add the following snippet to the file. This will add to `pyenv` to the load path. 

```
export PYENV_ROOT="$HOME/.pyenv"
command -v pyenv >/dev/null || export PATH="$PYENV_ROOT/bin:$PATH"
eval "$(pyenv init -)"
```

Don't close the file yet! 
We need to install `pyenv-virtualenv` to enable us to use virtual enviroments. This is the manager that helps us maintain different dev environments with differen python versions and different python package versions. To enable `pyenv-virtualenv`, add the following line to the `.bashrc` below the above snippet. 

```
eval "$(pyenv virtualenv-init -)"
```

Now we can save and close the file. In order for the changes to take effect, either you have restart the terminal, or type:

```
$ source ~/.bashrc
```

Now we should have `pyenv` and `pyenv-virtualenv` installed. Let's make sure:

```
$ pyenv --version
pyenv 2.3.0

$ pyenv virtualenv
pyenv-virtualenv: no virtualenv name given.

```

If you see those outputs (pyenv version might be different depending on when you run this), you have installed both. Let's create a virtualenv with a specific python version and install the base packages we would need.

Let's create an environment named `dssg-3.8.2` (this could be any name you like) with `Python 3.8.2`. First, install the Python version we need on `pyenv`. 

_Note: You can check all available Python versions on pyenv by using `$ pyenv install --list`_

```
$ pyenv install 3.8.2
```

This will take several minutes. Once complete, create the environment

```
$ pyenv virtualenv 3.8.2 dssg-3.8.2
```

Now you have created the virtual environment. To use it with a specific project, you can navigate to the project folder and assign it to the directory:

```
$ echo dssg-3.8.2 > .python-version
```
This will ensure that whenever you are inside that directory, the `dssg-3.8.2` environment will be activated.

If not, you can use the command 

```
$ activate dssg
```
to manually activate the environment. 

Once you have activated the environment you can start installing Python packages. 

### Package Installations

Packages are installed using pip. To install a single package:

```
$ pip install pandas
```

To install many packages at once, list all the packages needed in a file (usually called requirements.txt), navigate to the folder of the file and execute

```
$ pip install -r requirements.txt 
```

to try it out use this file: [requirements.txt](requirements.txt)


### Jupyter 

Jupyter notebooks are a convenient environment for experimentation, prototyping, and sharing exploratory work. We install Jupyter in the above requirements.txt file. 

Jupyter notebooks require a kernel that executes the code. It should link to the virtual environment:

```
$ python -m ipykernel install --user --name=dssg-3.8.2 --display-name "dssg-3.8.2"
```

Note that you should have the virtual environment activated when you issue this command. 

To test, let's launch a Jupyter notebook

```
$ jupyter lab
```

Your browser should open a new tab with the jupyter lab interface.  


### SSH Keys

SSH helps you access the remote servers using your laptop. For this to work, we generate a key-pair that consists of a Public Key (something that you would share with the server admin), and a private key (something that you would NEVER share with anyone!).

**Option A - WSL**

Inside WSL, we can use the same process as a UNIX system to generate keys. 

```
ssh-keygen
```

This will prompt you to select a location for storing the key, and give you the option to add a passphrase to the key. If you want to use the default locaion (Recommended!) and not use a passphrase, you just have to hit return. 

Then, your keys will be stored in the place your specified. By default, 
- there'll be a `.ssh` folder in your home directory
- private key would be named `id_rsa`
- public key would be named `id_rsa.pub`

You've successfully generated the Keys!


**Option B - Windows**

Luckily, Windows 10/11 have OpenSSH already installed, and we don't need to use Putty anymore 🥳.

Just to make sure that it's installed, open up a Powershell window and enter `ssh`. When you hit return you should see an output like this. 

```
usage: ssh [-46AaCfGgKkMNnqsTtVvXxYy] [-B bind_interface]
           [-b bind_address] [-c cipher_spec] [-D [bind_address:]port]
           [-E log_file] [-e escape_char] [-F configfile] [-I pkcs11]
           [-i identity_file] [-J [user@]host[:port]] [-L address]
           [-l login_name] [-m mac_spec] [-O ctl_cmd] [-o option] [-p port]
           [-Q query_option] [-R address] [-S ctl_path] [-W host:port]
           [-w local_tun[:remote_tun]] destination [command]
```

If you do not see this output, you can [use this guide to install OpenSSH](https://docs.microsoft.com/en-us/windows-server/administration/openssh/openssh_install_firstuse). 


Once you have OpenSSH, you can use the same command as WSL to generate the Keys on a Powershell Window. As with WSL, you would be prompted to select the location to store the keys, and then the option to add a passphrase. You can just hit return to use the default location (recommended!) and not have a passphrase. 

By default, the keys will be stored in `C:\Users\<windows_username>/.ssh/` and the file names would be as same as the WSL one. 


## VSCode 

Visual Studio Code is a free text editor that enables you to code directly on a remote server. You can [download VSCode for windows here](https://code.visualstudio.com/). 

If you development environment is on WSL, you can [install the Remote-WSL extension for VSCode](https://code.visualstudio.com/learn/develop-cloud/wsl) and navigate to your project folder on the WSL terminal and type:

```
$ code .
```

This will launch a VScode window that will let you develop on your WSL machine. 

As we said above, one of the most useful features of VSCode is that it let's you edit code directly on a remote server ussing SSH. To use this feature, you should [install the Remote-SSH extention for VSCode](https://code.visualstudio.com/learn/develop-cloud/ssh-lab-machines). 

We need to tell VSCode where your private key is to authenticate the SSH connection. VSCode would automatically check for the default private key named `id_rsa` at the default Windows location `C:\Users\<windows_username>/.ssh/`. As we created the SSH keys in WSL, they keys would be inside the WSL file system. We can copy the keys to the windows location. 

```
$ mkdir /mnt/c/<windows username>/.ssh
$ cp -r ~/.ssh/ /mnt/c/<windows username>/.ssh/
```

Note that this will overwrite an existing ssh key in the Windows folder. 


## Database


**DBeaver**

We woud install DBeaver on directly on Windows. You can [download the installer here](https://dbeaver.io/download/).



**PSQL**

On WSL terminal, you can enter the following commands to install psql

```
$ sudo apt-get update
$ sudo apt-get install postgresql-client
```

Try typing `psql` into the terminal, you should see the following output. 

```
$ psql
psql: could not connect to server: No such file or directory
        Is the server running locally and accepting
        connections on Unix domain socket "/var/run/postgresql/.s.PGSQL.5432"?
```



















