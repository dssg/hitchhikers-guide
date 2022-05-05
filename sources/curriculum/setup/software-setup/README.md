# Software to Install

In order to be ready for the summer, you need to install some packages on your computer:

## Required

*   Git (for version control)
*   DBeaver (GUI to access various databases)
*   Python tools
    *   `pyenv + virtualenv` for python version management
    *   Python 3.8 or higher
    *   Python Packages
        *   pandas
        *   matplotlib
        *   seaborn
        *   scikit-learn
        *   psycopg2
        *   ipython
        *   jupyterlab
  *   Text Editor for Coding (your favorite, or VSCode)
  *   SSH Keypair

## Highly Recommended
*   psql (PostgreSQL command line interface)
*   Tableau (students can request a free education license)

## How to install pre-requisites?

*   **OS X** users - Follow [these instructions](setup_osx.md)
*   **Linux** users - You probably know how to do it, but you can follow the [OS X instructions](setup_osx.md) substituting your appropriate package manage for homebrew
*   **Windows** users - Follow [these instructions](setup_windows.md)

## SSH Key Setup

You need to generate a SSH key pair. To do this, follow the
instructions on
[GitHub](https://help.github.com/articles/generating-a-new-ssh-key-and-adding-it-to-the-ssh-agent/),
namely 'Generating a new SSH key' and 'Adding your SSH key to
ssh-agent'. Windows users probably want to use [git
bash](https://git-for-windows.github.io/) or
[PuTTYgen](https://winscp.net/eng/docs/ui_puttygen) (if you're on
Linux or OS X, your standard terminal should be the bash shell you
need).

The steps in 'Generating a new SSH key' create two new files (by
default in `~/.ssh/`: One without a file extension (by default, it's
called `id_rsa`), and one with the extension `.pub`. The latter one is
your _pub_lic key, which you will share with your project server, so
that it can recognize you; the former is your private key, which you
must not share with anybody, as it will let you access your project
server.

After having generated the key pair, you should set the correct file
permissions for your _private_ key: SSH requires that only you, the
owner, are able to read/write it, and will give you an error
otherwise. You can set the right permissions with this command: `chmod
600 ~/.ssh/nameofyourprivatekey` (where you'll have to substitute in
the path and name of your private key that you chose during key
generation).

## Running into setup issues?

Feel free to post your questions in the #tech_help channel on the slack workspace for the summer. We'll also have some tech setup help sessions to resolve any lingering setup issues (and help you get familiar with the remote servers we'll be using for the projects) during the first week of the fellowship.

