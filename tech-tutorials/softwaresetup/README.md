# Software Setup Session

## Motivation

Every team will settle on a specific setup with their tech mentors. This setup will determine, for example:
- which Python version to use
- versioning via virtual environments
- maintaining package dependencies
- continuous testing tools
- your version control workflow.

Today, we're _not_ doing that. We're making sure that everybody has some basic tools they will need for the tutorials and the beginning of the fellowship, and that you can log into the server and database.

### Format

We'll do this workshop-style: Work through the prerequisites below, making sure that your software works. If you're done with one step, help the people around you. The tech mentors will hover around and help, too. Let's get this over with!

## Package Manager

A package manager will make your life easier.
- on Mac, install [Brew](http://brew.sh/)
- on Linux, you're probably good
- on Windows, you could install [Cygwin](https://www.cygwin.com/) to provide a lot of Linux-style functionality; ask Windows users around you for their preferred way to manage packages

## Git and GitHub Account
1. If you don't have a GitHub account, [make one](https://github.com/join?source=header-home)!

2. Add your username to the spreadsheet on Slack. We'll add your username to the DSSG organization on GitHub.

3. Install Git:
```
brew update
brew install git
```
(and similar for `yum` or `apt`). On Windows, Cygwin can provide git.

4. Configure Git and GitHub. GitHub has, as always, [great instructions for that](https://help.github.com/articles/set-up-git/).

5. Test your installation. For example, create a directory, and make it a git repo:
```
mkdir mytestdir
cd mytestdir/
git init
```
```
> Initialized empty Git repository in [...]/mytestdir/.git/
```
You can un-git the directory by deleting the `.git` folder: `rm -r .git` (or simply delete `mytestdir` entirely).

## SSH / Putty

1. You should have already generated a key pair, and sent the public key to Joe, who will have generated a user account on the server. (If not, follow the instructions on [GitHub](https://help.github.com/articles/generating-a-new-ssh-key-and-adding-it-to-the-ssh-agent/), namely 'Generating a new SSH key' and 'Adding your SSH key to ssh-agent'. Windows users probably want to use [git bash](https://git-for-windows.github.io/) or [PuTTYgen](https://winscp.net/eng/docs/ui_puttygen)).

2. Use your private key file, your username on the server, and the server's URL to ssh into the server:
```
ssh -i pathtoyourkey yourusername@serverurl
```
This should drop you into a shell on the server:
```
> jsmith@servername: ~$
```

If you run into an error, maybe the permissions on your private key are wrong? Do `chmod 600 pathtoyourkey` (with the correct path to your private key, of course).


## PSQL

The server runs Postgres 9.4.7.

1. Make sure you have the `psql` client installed; on Mac, this would be
```
brew install postgresql
```
On Ubuntu: ```sudo apt-get install postgresql-client-9.4```. This won't work for Ubuntu <= 14.4, which by default only packages 9.3; follow [these instructions](https://www.postgresql.org/download/linux/ubuntu/) in that case. (Though the older client seems to be happy to connect to the server, too.)

For Windows, you might want to use DBeaver.

2. Once you have the postgres client installed, you can access the training database with it. However, the database server only allows access from the training server. Thus, you need to set up an SSH tunnel through the training server to the Postgres server:
```
ssh -fNT -L 8888:POSTGRESURL:5432 -i pathtokey yourusername@SERVERURL
```
where you need to substitute the URLs, the path to your private key, and your username on the training server. This command forwards the Postgres server's port 5432 to your laptop's port 8888, but through your account on the training server. So if you access your local port 8888 in the next step, you get forwarded to the Postgres server's port 5432 - but from the Postgres server's view, the traffic is now coming from the training server (instead of your laptop), and the training server is the only IP address that is allowed to access the postgres server.

3. Connect to the Postgres database on the forwarded port
```
psql -h localhost -p 8888 -U USERNAME -d USERNAME
```
where you need to replace `USERNAME` with the postgres [!] username. You then get prompted for a password. This is now the postgres server asking, so you need to reply with the corresponding password!





## Python 2.7
    *   Python
    *   Anaconda/Miniconda or pip + virtualenv
    *   Packages
        *   pandas
        *   matplotlib
        *   scikit-learn
        *   psycopg2
        *   ipython
        *   jupyter

## R

## Optionals
DBeaver
RStudio




Notes:
- changing $PATH and $PYTHONPATH via bash_rc or bash_profile might be necessary
- permissions on SSH keys can cause trouble
