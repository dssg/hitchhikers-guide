# Technical Workflow and Best Practices


This tutorial is designed to help you understand how to get started with setting up your computing environment, how to decide what to use your local laptop/desktop for, what to do on the server (and how), and how to go back and forth between different environments and tools  on your laptop, the server, and your remote database (an other data resources).

We assume a GNU/linux (Ubuntu) server that's been set up for you, and access to a database (PostgreSQL).

??? note "Looking at this before the summer?"

     Many of the specific instructions here rely on the server and database we'll have set up for you to use during the summer, so you may not be able to follow along yet, but please do read through the workflow here so you'll have an idea what to expect.


## 1. What should you have on your laptop?

You'll need a few tools (such as SSH, a good text editor, a database utility, etc) installed on your local machine (whether it's a MacOS, windows, or GNU/Linux). If you haven't already done so, be sure to follow [the setup instructions here](../../setup/software-setup/) to get these installed on your laptop.

## 2. What should you set up on the server?

 * Decide which shell you're using. You have `bash` by default, but some people may prefer `zsh` (if you're new to working at the linux command line, stikcing with `bash` is a reasonable thing to do).

 * Optionally, set up dotfiles (these are configuration files that start with a `.` and allow you to specify shortcuts and change the behavior of your environment and various tools). you can clone this [repo](http://www.github.com/dssg/dotfiles) with Adolfo's dotfiles as a starting point to work from.

!!! danger

    You should **never** blindly copy lines to your dotfiles that you don't understand. Check the files in dotfiles repository and adapt/adopt what suits your needs and tastes

* [Configure git](../setup/git-and-github/basic_git_tutorial/01_BasicGit.md)

* Decide on your editor (vim or GNU/Emacs). Note that this is the editor you can use to edit files directly on the server. Some local text editors, such as VSCode, will allow you to edit files remotely on the server but through a GUI interface on your laptop.

??? note "For vim users"

     Get a good `.vimrc` file  to make life easier for yourself if you choose vim. See for example [this](https://dougblack.io/words/a-good-vimrc.html)

??? note "If you prefer GNU/Emacs"

     There are several options and depends in your taste, but [Emacs prelude](https://prelude.emacsredux.com/en/latest/) is a good start

* Create configuration files with your database credentials: [.pg_service.conf](https://github.com/dssg/hitchhikers-guide/blob/master/sources/curriculum/setup/software-setup/pgservice_conf.example) and [.pgpass](https://github.com/dssg/hitchhikers-guide/blob/master/sources/curriculum/setup/software-setup/pgpass.example) files, which should live in your home directory and have `600` permissions (e.g., `chmod 600 .pgpass && chmod 600 .pg_service.conf`) so only you can read/write it.

 * Learn about pyenv and virtual environments and set one up (if it hasn't been set up for you).

 * Learn how to install new python packages through `pip install`

## 3. Workflow: How should you work day to day with your laptop and the remote server?

* `screen`/`tmux`: When you log in to your remote machine, run [screen](https://linuxize.com/post/how-to-use-linux-screen/) (note: it will already be installed, so you can ignore those details; also [here's a quick video intro](https://www.youtube.com/watch?v=3txYaF_IVZQ)) or [tmux](https://medium.com/hackernoon/a-gentle-introduction-to-tmux-8d784c404340) and work from a screen/tmux session

* (Optional) When using the database for any reason from your laptop (to connect with tableau or dbeaver or for any other application), open an [ssh tunnel from your local machine to the remote server](../setup/software-setup/setup_session_guide.md#reaching-the-database-server):

```
ssh -N -L localhost:8888:localhost:8888 username@[projectname].dssg.io
```

Note that many GUI tools like `dbeaver` or `dbvisualizer` have a built-in interface for establishing an SSH tunnel that you can use as well.

* Writing and Running Code

    - Because your data needs to stay in the secure environment we've set up for it, you'll only be able to run your code on the server. As such, you have three options for how/where you want to write code:

        - *[Reccomended (especially if you're new to remote workflows)]* Using an GUI editor on your laptop (such as VSCode) that allows you to remotely edit files stored on the server over SSH.

        - Using another editor on your laptop (sublime, atom, etc) to edit code stored locally, then use git to commit and push to the repo and then do a git pull on the server to get your code there.

        - Editing code on the server directly, using a text-based editor such as vim or GNU/Emacs in a terminal window.

    - `git commit` often. Every time you finish a chunk of work, do a `git commit`. `git push` when you've tested it and it is doing what you intended for it to do. Do not push code to master if it breaks. You will annoy your teammates :) Later in the summer, we'll talk more about how to create git branches.

    - **Every time you resume working**, do a `git pull` to get be sure you're starting from the latest version of the code.

    - If you need to copy files from your laptop to server, use `scp`.

    !!! danger

        Other way around, i.e. *from the server to your laptop*, **DON'T!** All the data needs to stay on the remote server.

    - If you're writing (or running) your code in jupyter notebooks, then you should:
        1. create a no-browser jupyter session on the *server* `jupyter lab --no-browser --port=8889` You may need to chage the port number to avoid conflicts with other teammates using the same port.

        2. On your local machine, create an SSH tunnel that forwards the port for Jupyter Lab (`8889` in the above command) on the remote machine to a port on the local machine (also `8888` above) so that we can access it using our local browser. `ssh -N -L localhost:8888:localhost:8889 username@projectname.dssg.io`

        3. Access the remote jupyter server via your local browser. Open your browser and go to [http://0.0.0.0:8888](http://0.0.0.0:8888)

        !!! info ""
            you may need to copy and paste the longer URL with a token that is generated when you run the command in step 1) that looks like `http://localhost:8889/?token=343vdfvdfggdfgfdt345&token=fdsfdf345353vc`

        See [More detailed instructions](https://hsaghir.github.io/data_science/jupyter-notebook-on-a-remote-machine-linux/)

## 4. Other Workflow Considerations

1. When should you use Jupyter lab, versus when you should use .py files to write code
2. When to use `psql` versus DBeaver
3. When to use SQL versus when to use Python and/or Pandas

## 5. Other Tips
* Tunneling to the DB for Tableau (or another app like QGIS): `ssh  -L 5433:databaseservername:5432 username@projectservername`



# BELOW COPIED FROM OLD setup_session_guide.md

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


