# GitHub Basics

## Our goal for this session:

This session will give a quick overview of what git is, and its basic usage.

For this tutorial you will need to have access to git, a Terminal and a Text Editor.


## What is Git?

![git](https://imgs.xkcd.com/comics/git.png)

[Image source](https://xkcd.com/1597/)

Git is a free version control system which helps you keep track of file changes you make during development. Think of it as a time machine that lets you go back to any point in your project development with an undo button, and a tool to safely and efficiently collaborate with others on a shared project.

While git is mostly used in software development, it can be used for anything you like
([writing books](https://www.gitbook.com/), for example), as long as your files are plain text
(e.g., source code, latex files).

## How does it work?

### Commits
Git can save snapshots of your work called `commits`. Once you register a set of changes as a `commit`, you can go back and forth through different commits in your project.
Let's say you were experimenting with some new function and realized the old one was better, no problem, you can bring back anything!


The evolution of your project can be stored as a series of commits. The collections of commits and associated metadata form the `repository` of your project.


Typically, we would have a local copy and a remote copy of the repository (just like you do with Google Drive).  This prevents
endless emailing of source code and the following situation:

![final](https://www.phdcomics.com/comics/archive/phd101212s.gif)

### Github

There are many providers that let you store your git repositories -gitlab, bitbucket, mercurial, etc.-, but the most popular one is Github (we'll use github for DSSG).

Apart from storing a copy of your projects, github comes with a lot of useful features. For example, you can use it to share your projects with your colleagues, so they can see (or modify if you want) your project.

## How do we use git? 

First, let's login to the server.

```
$ ssh {andrewid}@training.dssg.io
```

### Configuring your Git Profile

First things first. You need to configure you git client so your commits are attributed to you. Do the following:

```
# How the current git configuration look like
git config --list
```

The workspace

```
git config --global user.name "Clark Kent"
git config --global user.email "{the email you used for Github}"
```

You now have your `git` client configured. Next we will create
our first repository.

### Initializing a git repository

You can create a new directory, and to make it a git repository, we can use the `git init` command.

First, let's navigate to the project folder and create a folder with your andrewid so that everyone can have their own directory. 

```
$ cd /mnt/data/projects/food_inspections
$ mkdir {andrew_id}
$ cd {andrew_id}
$ mkdir my_git_repo
$ cd my_git_repo
$ git init
```

Alternatively, if we want to contribute to an already existing repository, we can use the command

```
git clone /path/to/repo
```


### What is the typical workflow?

When you make changes to your files and want to register those changes as a snapshot (commit) into the history, we take the following **minimum** steps:

+ We let git know which files we want to put on the next snapshot -- `add`  
+ We "take" the snapshot -- `commit`
+ We update the remote repository to add our snapshot into its history of snapshots -- `push`

A more "complete" and recommended workflow consists of the following steps:

**Do not type these commands yet!**

0. Update your local repo. 

Before you make any changes to the files in the repo, you should make sure that your copy of the repo reflects the latest versions of files. 

```
git pull
```  

1.  Check what has changed since the last snapshot

```
git status
```

2. Tell git which files have changed and you are interested to be in the next snapshot.

Note -- It's good practie to add a single file at a time.

```
git add {filename}
```


3. Take the snapshot of your changes

```
git commit -m "a meaningful but short message describing the changes you made"
```

4. Make the snapshot available on the remote repository so that everyone on your team could access your changes.

```
git push
```

### Let's practice the commands

To clone a github repo we will need to authenticate, in DSSG we prefer to use
 ssh. We will need to create another pair of keys **within** the server and
  add the **public key** to Github. 
 
```
$ ssh-keygen
$ cd ~/.ssh
$ cat id_rsa.pub
```

To copy your public key into Github go to your profile on Github `Settings
 >  SSH and GPS keys > New Key`


Let's try to clone a practice repository for this session.

```
$ cd /mnt/data/projects/food_inspections/{andrew_id}
$ git clone git@github.com:dssg/github_practice.git
$ cd github_practice
```

+ Update any changes made in the remote repo: `git pull`
+ Create a file with your name in it (change `{andrewid}` for your actual andrewid - withouth the `{` and `}`):

```
$ nano {andrew_id}.txt
```

That will open an editor window, put your name in it and then use `Ctrl+X` then type `Y` to save the changes.

Verify the changes we made in the file: `cat {andrewid}.txt`

+ Tell git which files to take into account for the next snapshot

```
$ git add {andrewid}.txt
```

+ Make the snapshot

```
$ git commit -m "file with my name"
```

+ Make available your snapshot on the remote repository

```
$ git push
```


### Other useful commands

+ Look up for the difference between versions. Let's make some changes into
 your file. Let's add your month of birth date. 

```
$ git status
$ git diff {andrew_id}.txt
```

Now lets `push` this change: 

```
$ git pull 
$ git add {andrew_id}.txt 
$ git commit -m "adding my month birht date"
$ git push
```

+ Delete a file from the repo. If you want to get rid of a file you need to
 tell git to remove it.\* 

```
git rm {andrew_id}.txt
```

### Useful git files

+  `.gitignore` This file will allow us to tell git which files/directories
 we don't to be part of the repo ever. Very useful to keep credentials files out
  of a github repo.  


