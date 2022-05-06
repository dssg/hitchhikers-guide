# Setting your machine

## Motivation

Every team will settle on a specific setup with their tech mentors. This setup will determine, for example:

- which Python version to use
- versioning via virtual environments
- maintaining package dependencies
- continuous testing tools
- your version control workflow.

Today, we're **not** doing that. We're making sure that everybody has some basic tools they will need for the tutorials and the beginning of the fellowship, and that you can log into the server and database. Hopefully you already got many of these tools set up on your computer before arriving, but we'll quickly check that your local enviroment is working (and resolving any lingering issues), and then talk a bit about some of the remote servers and tools we'll be using throughout the summer.

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

Let's get this over with!

## Setting Up Your Local Environment

First, let's work through the guide for setting up the software for your local machine that we sent earlier in the summer:

*   **OS X** users - Follow [these instructions](setup_osx.md)
*   **Linux** users - You probably know how to do it, but you can follow the [OS X instructions](setup_osx.md) substituting your appropriate package manage for homebrew
*   **Windows** users - Follow [these instructions](setup_windows.md)


## Remote Environment for the Summer

The data you'll be using for the summer is generally of a sensitive nature and needs to be protected by remaining in a secure compute environment. As such, all of your work directly with the data will be on one of the remote servers we've set up. Let's see how connecting to those resources works:

### Reaching the Compute Server

Now that you've created an SSH key, you should be able to use your username and server's address to ssh into the server:

    ssh yourusername@serverurl

Once you enter your password, you should be dropped into a shell on the server:

    yourusername@servername: ~$


!!! important "PRO tip"

    Your life will be easier if you set up a [`.ssh/config` file](ssh_config.example)


## Reaching the Database Server

The database server runs PostgreSQL.

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


