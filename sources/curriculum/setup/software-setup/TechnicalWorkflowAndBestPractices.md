# Technical Workflow and Best Practices


This tutorial is designed to help you understand how to get started with the DSSG computing environment, how to decide what to use your local laptop/desktop for, what to do on the server (and how), and how to go back and forth between different environments and tools on your laptop, the server, and your remote database (an other data resources).

We assume a GNU/linux (Ubuntu) server that's been set up for you, and access to a database (PostgreSQL).

??? note "Looking at this before the summer?"

     Many of the specific instructions here rely on the server and database we'll have set up for you to use during the summer, so you may not be able to follow along yet, but please do read through the workflow here so you'll have an idea what to expect.

## Know Your Infrastructure

![](imgs/infrastructure_components.png)

In our initial [setup session](setup_session_guide.md), we very briefly talked about the different components of the infrastructure we'll be using this summer. In this tutorial we'll take a bit of a deeper dive into how these different pieces fit together and help you perform different types of tasks.

### Why Remote Infrastructure?

As you'll find there's a bit of overhead (and a learning curve!) to using a remote computing environment. So, why are we making you do it? A few reasons:

1. **Confidentiality:** Most importantly, the data we're using is generally of a sensitive nature and needs to be protected, which means only working with it in a secure computing environment. 

1. **Computing Power and Scalability:** We can use computing resources with much more power than your laptop, and scale them up and down as needed.

1. **Collaboration:** Working in a shared environment with code under version control makes for a much better experience working on a collaborative project.

1. **Learning New Tools:** You're also at DSSG to learn new things, of course, and are likely to encounter many of these (or similar) tools again in the future.

!!! danger "Data Confidentiality"

    Remember that the data we're using is confidential and must stay in our secure computing environment at all times. **Do not download the data to your laptop!**

    Inform DSSG staff immediately if you accidentally download data or your computer or key is compromised!

## Connecting to the Server: SSH

Here's what happens when you connect to the DSSG server via SSH:

![](imgs/infra_when_you_ssh.png)

The public and private SSH keys are based around two large prime numbers and created in such a way that someone with the public key can encrypt a message that only you can decrypt with your private key (well, or someone with a quantum computer).

!!! danger

    I know it's in big red letters in the image but, really, it's worth repeating: don't share your private key!!

Note that the CMU VPN is also adding an extra layer of encryption and routing all your traffic through the CMU network.

Let's give it a try and explore using the unix command line a bit by working through the [Introduction to Command Line Tools](../command-line-tools/)

## Talking to the Database with psql

One way to talk to our postgres database is via the `psql` command line tool running directly on the server. To do so, you connect to the server via SSH (as above) then use the `psql` client to reach the database:

![](imgs/infra_when_you_psql.png)

## Talking to the Database with DBeaver

Here's where things get a little more complicated: you want to use a nice GUI client for running SQL queries, but to keep the data more secure, we only allow it to be reached from our compute server. To do so, you'll need to encrypt the otherwise less-secure database connection though an **SSH Tunnel**:

![](imgs/infra_when_you_dbeaver.png)

Notice that the tunnel (blue) is encrypting your connection to the database (purple) as far as the compute server, where it gets decrypted and forwarded on to the database. Between your laptop and the CMU servers, the CMU VPN (red) does effectively the same thing.

Fortunately, DBeaver has a built-in interface for establishing an SSH tunnel for you, which we set up during the initial [setup session](setup_session_guide.md).

## Using jupyter lab

Another useful tool for some code prototyping and data visualization can be `jupyter lab`. To use it, you'll need to run a `jupyter` server on the compute server and then route your traffic to it from your browser through an SSH tunnel (just as with your dbeaver connection):

![](imgs/infra_when_you_jupyter.png)

Unlike DBeaver, `jupyter lab` doesn't provide a built-in interface for creating the SSH tunnel, so we'll have to do it manually.

There are three components:
- The remote machine (our course server) hosts a jupyter notebook server that does things like loads files, runs python, activates virtual environments
- Your web browser connects to that server and presents a frontend interface for opening, editing, and running notebooks
- These connect using SSH

let's set it up:

1. Connect to the server `ssh {andrewid}@training.dssg.io`

2. Find an open port on the course server to send your Jupyter traffic through:
    - In the terminal (on the course server) type ss -lntu. This will list all ports
    - Pick a port number between 1024 and 65535 that is **NOT on that list**.

3. Navigate to `/mnt/data/projects/food-inspections` to activate your virtual environment (you might need to run `direnv allow` if this is your first time doing so) 
    - If you want to confirm your virtualenv has properly activated, run `which python` -- this should return {Fill Here}. If you get anything different (or nothing at all), your virtualenv hasn't activated correctly!

4. Now, start the jupyter server

```
$ jupyter lab --no-browser --port {Your port from step 2} 
```
(note: to ensure this persists, you may want to start your server in a screen session as discussed above!)

5. When the server starts, take note of the token printed in the server terminal output:

![](imgs/jupyter-token.png)

6. On your local machine, set up an SSH tunnel. This will allow your web browser (on your local computer) to reach your Jupyter notebook server (on the course server)


```
$ ssh -i {path to your private key} -N -L localhost:8888:localhost:{ your port from step 2} {andrewid}@training.dssg.io
```

7. Now, we can open the notebook on your local machine:
    - Navigate to http://localhost:8888

    - If this is the first time opening Jupyter, this should take you to a login page asking you to enter the token that was generated (step 5). Copy and paste the token to proceed. 

![](imgs/jupyter-login.png)

    - On the next screen (which should be a view of the folders and files in your working directory)

![](imgs/jupyterlab-launcher.png)

8. To shut down the server, you can return to the screen/terminal window where the server is running and type (1) `ctrl+c` and (2) `y` when prompted.  


## Editing Remotely with VSCode

The easiest way to edit your code (and the one we recommend for the summer) is using a tool, such as VSCode, that provides a GUI text editor on your laptop but allows you to remotely edit the files on the server via SSH:

![](imgs/infra_when_you_vscode.png)

Note that you'll still need to commit and push your code up to github using the `git` CLI from the server to make sure your teammates have access to your latest changes.

## Editing Files Locally

Another option is to have a copy of the code you're working on locally on your computer and edit it using a local text editor (e.g., sublime, atom, etc.). However, you won't be able to run the code locally (have we mentioned that the data needs to stay in the secure environment we've set up for it?), so you'll need to use github to sync your local edits to the server for testing:

![](imgs/infra_when_you_local_edit.png)

Of course, a third option is to connect to the server via SSH in a terminal and then edit files directly at the command line using a text-based editor such as `vim` or `emacs`, which you're definitely free to do if you're confortable in those environments.


## The Typical Workflow

Now that we've taken a quick tour of some of the common tasks on the DSSG infrastructure, let's see how these pieces fit together into a typical technical workflow:

![](imgs/tech_workflow.png)

We'll talk about github in another session, but a good practice to keep in mind is:

- **Every time you resume working** after any break, do a `git pull` to get be sure you're starting from the latest version of the code.

- `git commit` often. Every time you finish a chunk of work, do a `git commit`. `git push` when you've tested it and it is doing what you intended for it to do. Do not push code to the main branch if it breaks. You will annoy your teammates :) Later in the summer, we'll talk more about how to create git branches to make this process a little more resiliant as well.

!!! important "Pro Tip"

    Every time you connect to the server in your terminal use a `screen` session (or `tmux` if you prefer) to ensure your processes remain alive on the server even if your SSH connection drops. This is particularly useful for long-running processes (like modeling jobs or your jupyter server), but a good habit to get in generally.



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


