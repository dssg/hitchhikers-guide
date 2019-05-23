# Technical Workflow and Best Practices


This tutorial is designed to help you understand how to get started with setting up your computing environment, how to decide what to use your local laptop/desktop for, what to do on the server (and how), and how to go back and forth between different environments and tools  on your laptop, the server, and your remote database (an other data resources).

We assume a GNU/linux (Ubuntu) server that's been set up for you, and access to a database (PostgreSQL).

## Things we'll cover in this tutorial:

#### 1. What should you have on your laptop? You should have the following tools installed on your local machine (whether it's a MacOS, windows, or GNU/Linux) that you will use primarily locally:

 * `ssh` (to connect to the server)
 * `psql` (to connect to the database through command line)
 * `dbeaver` (or `dbvisualizer`) to connect to the database through a GUI
 * Git client (to work with github repositories)
 * Tableau
 * GNU/Emacs, Vi, sublime or atom (text editor to edit code locally)
 * `python`, `jupyter` and other coding tools are helpful but you will be primarily using them on the server and not on your laptop

#### 2. What should you set up on the server?

 * Decide which shell you're using. You have `bash` by default, but many of us like `zsh`.

 * Set up dotfiles. you can clone this [repo](http://www.github.com/dssg/dotfiles) with Adolfo's dotfiles
 * [Configure git](https://github.com/dssg/hitchhikers-guide/blob/master/curriculum/2_data_exploration_and_analysis/git-and-github/basic_git_tutorial/01_BasicGit.md)

 * Decide on your editor (vim or GNU/Emacs).

 ??? note "For vim users"
     Get a good `.vimrc` file  to make life easier for yourself if you choose vim. See for example [this](https://dougblack.io/words/a-good-vimrc.html)

 ??? note "If you prefer GNU/Emacs"

     There are several options and depends in your taste, but [Emacs prelude](https://prelude.emacsredux.com/en/latest/) is a good start

 * Create a file with your database credentials ([sample file](https://github.com/dssg/hitchhikers-guide/blob/master/curriculum/1_getting_and_keeping_data/csv-to-db/default_profile.example)) or setup a [.pg_service.conf](./software-setup/pgservice_conf.example)


 * Learn about virtual environments and set one up (if it hasn't been set up for you). For DSSG 2018, we've set up venvs for every project that get activated when you enter your project directory)

 * Learn how to install new python packages through `pip install`

#### 3. Workflow: How should you work day to day with your laptop and the remote server?

 1. screen/tmux: When you log in to your remote machine, run [screen](https://www.digitalocean.com/community/tutorials/how-to-install-and-use-screen-on-an-ubuntu-cloud-server) or [tmux](https://hackernoon.com/a-gentle-introduction-to-tmux-8d784c404340) and work from a screen/tmux session

2. (Optional) When using the database for any reason from your laptop (to connect with tableau or dbeaver or for any other application), open an ssh tunnel from your local machine to the remote server.
  * windows https://www.skyverge.com/blog/how-to-set-up-an-ssh-tunnel-with-putty/
  * mac/linux ssh -N -L localhost:8888:localhost:8888 username@[projectname].dssg.io

3. Writing and Running Code
  * If you're using your laptop (sublime, atom, or some other editor) to edit code, use git to commit nad push to the repo and then do a git pull on the server to get your code there.
  * If you're writing code on the server directly, you should use vim or emacs.
  * git commit often. Every time you finish a chunk of work, do a git commit. git push when you've tested it and it is doing what you intended for it to do. Do not push code to master if it breaks. You will annoy your teammates :) Later in the summer, we'll talk more about how to create git branches.
  * Every time you resume working, do a git pull to get the latest version of the code.
  * If you need to copy files from your laptop to server, use scp. Other way around, DON'T! All the data needs to stay on the remote server.
  * If you're writing (or running) your code in jupyter notebooks, then you should:
   1. create a no-browser jupyter session on the *server* [jupyter notebook --no-browser --port=8888] You may need to chage the port number to avoid conflicts with other teammates using the same port.
   2. On your local machine, create an SSH tunnel that forwards the port for Jupyter Notebook (0888 in the above command) on the remote machine to a port on the local machine (also 888 above) so that we can access it using our local browser. [ssh -N -L localhost:8888:localhost:8889 username@projectname.dssg.io]
   3. Access the remote jupyter server via your local browser. Open your browser and go to http://localhost:8888 (you may need to copy and paste the longer URL with a token that is generated when you run the command in step 1) that looks like http://localhost:8889/?token=343vdfvdfggdfgfdt345&token=fdsfdf345353vc

   [More detailed instructions](https://hsaghir.github.io/data_science/jupyter-notebook-on-a-remote-machine-linux/)

#### 4. Other Workflow Considerations
1. When should you use Jupyter notebooks, versus when you should use .py files to write code
2. When to use psql versus DBeaver
3. When to use SQL versus when to use Python and/or Pandas

#### 5. Other Tips
* Tunneling to the DB for Tableau: ssh  -L 5433:databaseservername:5432 username@projectservername
