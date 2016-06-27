#DSSG Pre-requisites

In order to be ready for the summer, you need to install some packages on your computer:

## Required

*   SSH (PuTTY for Windows)
*   Git
*   psql (PostgreSQL CLI)
*   Python tools
    *   Python
    *   Anaconda/Miniconda or pip + virtualenv
    *   Packages
        *   pandas
        *   matplotlib
        *   scikit-learn
        *   psycopg2
        *   ipython
        *   jupyter
* R

## Optional

*   RStudio
*   DBeaver
*   Tableau (students can request a free license)
*   Sublime Text/Atom


## How to install pre-requisites?

*   **OS X** users - Follow this [instructions](osx.md)
*   **Linux** users - You probably know how to do it, but still [check this](https://github.com/dssg/hitchhikers-guide/blob/master/prerequisites/osx.md#step-3-install-python-tools) for information on Python tools
*   **Windows** users - We don't have a guide yet (any volunteers?)

## Try it out!

You should give all installed software a quick spin to check that it did install. For your python packages, try to import them. Type `python` in your shell, and then once you are in your python session, try for example `import pandas`, `import matplotlib`, and so on. (You can quit with `exit()`.) Also try `ipython` and `jupyter notebook` in your terminal, and see if you get any errors.

Similarly, try `psql` in your terminal; it should reply 
```
psql: could not connect to server: No such file or directory
```

`ssh` should print a 'helpful' message, and `R` should drop you into an R session that you can quit with `q()`.

## SSH Key Setup

You need to generate a SSH key pair. To do this, follow the instructions on [GitHub](https://help.github.com/articles/generating-a-new-ssh-key-and-adding-it-to-the-ssh-agent/), namely 'Generating a new SSH key' and 'Adding your SSH key to ssh-agent'. Windows users probably want to use [git bash](https://git-for-windows.github.io/) or [PuTTYgen](https://winscp.net/eng/docs/ui_puttygen) (if you're on Linux or OS X, your standard terminal should be the bash shell you need).

The steps in 'Generating a new SSH key' create two new files (by default in `~/.ssh/`: One without a file extension (by default, it's called `id_rsa`), and one with the extension `.pub`. The latter one is your _pub_lic key, which you will share with your project server, so that it can recognize you; the former is your private key, which you must not share with anybody, as it will let you access your project server.

After having generated the key pair, you should set the correct file permissions for your _private_ key: SSH requires that only you, the owner, are able to read/write it, and will give you an error otherwise. You can set the right permissions with this command: `chmod 600 ~/.ssh/nameofyourprivatekey` (where you'll have to substitute in the path and name of your private key that you chose during key generation).

## Asking for help

We just started this repo but we want the [issues section](https://github.com/dssg/hitchhikers-guide/issues) to be a knowledge base for common problems.

If you have any trouble installing anything check closed issues. If you don't find the answer, feel free to [open an issue](https://github.com/dssg/hitchhikers-guide/issues/new) and someone will help you.

*To open issues, you need to create a Github account (you'll need it for the summer anyway).*

