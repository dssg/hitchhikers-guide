

# Agenda

-   Some thoughts about  life

-   First things first

-   Different ways of do stuff

-   "The Flow"

-   "Issue oriented coding"

-   Practice makes the master


# Some thoughts about  life


## Git is a collaboration tool

Git is a version control system that allows you to take snapshots of your project so you can
go back in time or safely add features safely without breaking your code. This is much better
then taking turns working on software and emailing version back to eachother. Git can be used
for any project involving plain text files, including code, books, papers, small datasets.


## Git is a communication tool

Git and Github are used for hosting, distributing and colloborating on your project with others.
Through tools like GitHub issues, GitHub Pull Requests and branches you can manage large scale
collaborations.

Some examples of open-source projects managed on GitHub:

[Software<sub>Carpentry</sub><sub>Git</sub><sub>Lesson</sub>](<https://github.com/swcarpentry/git-novice>)
[MDAnalysis](<https://github.com/MDAnalysis/mdanalysis>)
[Numpy](<https://github.com/numpy/numpy>)


## The first golden Rule

-   You are a team, work as a team

-   You are physically located at the same table, so talk with your teammate

-   Know what he/she doing, Collaborate, Code review (and learn), Pair programming (and learn)


# First things first

-   Open a terminal &#x2026;

-   Command line magic
    -   Use the up-and-down keys to scroll through the history of our commands
    -   \`TAB\` completion
    -   \`Ctrl-R\` to recursively search for previous commands

-   Who am I? Where am I?
    -   \`whoami\`
    -   \`pwd\`

-   `git` `<>` `github`

-   Try `zsh` or `oh-my-zsh`


## My workspace

    # How my git configuration looks like?
    git config --list


## My workspace

    # Adding some, if you don't have a user.name or user.email set
    git config --global user.name "Rayid Ghani"
    git config --global user.email "rayid.ghani@dssg.io"
    git config --global color.ui "auto"
    git config --global core.editor 'subl -n -w' #or nano, vim, emacs


## My workspace

    ## This is very important!!
    ## YOU NEED TO DO THIS
    git config --global push.default current


# Different ways of do things


## Different ways of do things

-   "Solo" workflow
-   Open source workflow
-   Git flow
-   Github flow


## "Solo" workflow

    mkdir my_working_directory
    cd my_working_directory
    git init
    touch some_file.py
    # hack
    # hack
    git add some_file.py
    git commit -m "Working with some awesome idea"
    # hack
    # more hack
    ...

-   This works if you are working by yourself
    -   This is not our case


## Opensource workflow

Some differences:

-   You need a `github`  account
-   Choose a repository in `github.com` in which you want to participate
    -   Lets pretend: `http://github.com/the-repo-you-want-to-participate`
-   Push the `Fork`  button


## Opensource workflow

-   Open your terminal &#x2026;

    git clone http://github.com/my-copy-of-the-repo-you-want-to-participate
    cd the-repo-you-want-to-participate
    # hack
    # hack
    git add some_file.py
    git commit -m "Working with some awesome idea"
    # hack
    # hack
    git push


## Opensource workflow

-   Create a `pull-request` and describe your work

-   Wait


## Opensource workflow

-   This works very well if you want to collaborate, but you don't know the other people involved
    -   This is not our case
-   And this has several more steps:
    -   What if I want to `pull` the most recent changes in the original repo?

    ## See the "remotes"
    git remote -v
    ## Add the original repo
    git remote add original-repo http://github.com/the-repo-you-want-to-participate
    ## Pull the changes of the original repo to your local copy
    git pull original-repo master
    ## Push the added changes to your repo
    git push origin master
    ## etc

-   More prone to errors, merges, conflicts, etc.


## Git flow

-   This is more oriented to software development with a lot of `git`-gurus involved


# "The Flow"


## Github flow

-   Also know as the [*Anti-gitflow*](http://endoflineblog.com/gitflow-considered-harmful)

-   [Github Flow](https://guides.github.com/introduction/flow/) (explained with images and animation!)


# "Issue oriented coding"


## The second golden rule

Don't code anything if there is not a need of doing it


## A good issue

-   Clear
-   Defined output
-   Actionable (written in the Imperative Voice)
-   Could be completed at most in few days
-   Examples
    -   **Good**: *Fix the bug in &#x2026;*
    -   **Good**: *Add a method that does &#x2026;*
    -   **Bad**:  *Solve the dssg project*
    -   **Bad**:  *Some error happen*

x


# About code reviewing


## DEMO


# Into "the flow"


## Github flow

-   Short-lived branches

    ## Pull from the repo
    git pull
    ## Decide what do you want to do and create an issue
    git checkout -b a-meaningful-name
    ## hack, hack, hack, add/rm, commit
    ## Push to the repo and create a remote branch
    git push
    ## Create a pull-request and describe your work (Suggest/add a reviewer)
    ## Code review
    ## The pull-request is closed and the remote branch is destroyed
    ## Switch to master locally
    git checkout master
    ## Destroy your local branch
    git branch -d a-meaningful-name
    ## Pull the most recent changes (including yours)
    git pull


# Practice makes the master

-   Goal: Simulate the creation of a pipeline
-   **You will work in your team repo**
-   Create a directory called: `test`
-   The pipeline is composed for 3 steps:
    -   They have a function called `do_stuff()` (no args)
    -   This function prints on the screen `I'm step X`, where `X` is the number of the step
-   There's a `master.py` that uses that 3 steps in order.
-   Create an issue for deleting the `test` directory
-   Delete it
-   Easy right?
