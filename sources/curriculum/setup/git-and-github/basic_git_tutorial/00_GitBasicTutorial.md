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


### Commits
Git can save snapshots of your work called `commits`. Once you register a set of changes as a `commit`, you can go back and forth through different commits in your project. 
Let's say you were experimenting with some new function and realized the old one was better, no problem, you can bring back anything!


The evolution of your project can be stored as a series of commits. The collections of commits and associated metadata form the `repository` of your project. 


Typically, we would have a local copy and a remote copy of the repository (just like you do with Google Drive).  This prevents 
endless emailing of source code and the following situation: 

![final](https://www.phdcomics.com/comics/archive/phd101212s.gif)

### Github

There are many providers that let you store your git repositories, but the most popular one is Github (we'll use github for DSSG).

Apart from storing a copy of your projects, github comes with a lot of useful features. For example, you can use it to share your projects with your colleagues, so they can see (or modify if you want) your project.

## How do we use git? 
let's take a look at how we can use git. 

### Configuring your Git Profile

First things first. You need to configure you git client so your commits are attributed to you. Do the following: 

```
# How my git configuration currently look like
git config --list
```

 My workspace

```
# Adding some, if you don't have a user.name or user.email set
git config --global user.name "Clark Kent"
git config --global user.email "{the email you used for Github}"
```

Also do the following (important). Ask about this during the branching section of the 
tutorial if you want to know more. 
```
git config --global push.default current
```
You now have your `git` client configured. Next we will create 
our first repository. 

### Initializing a git repository

Note -- We are following [this guide](http://rogerdudler.github.io/git-guide/)

You can create a new directory, and to make it a git repository, we can use the `git init` command. 

```
$ mkdir my-git-repo
$ cd my-git-repo
$ git init
```

Alternatively, if we want to contribute to an already existing repository, we can use the command 

```
git clone /path/to/repo
```

You most likely will be prompted to autheticate your credentials when cloning a remote repo (e.g., from GitHub). 

Hint: You can upload your public SSH key to your Github profile and use the SSH option to clone a repo, so that you don't have to provide your password every time. 


### What is the typical workflow? 

A local git repository consists of three elements:
- Working directory, that contains the actual files
- the Index, which acts as a staging area for the changes you make for the files
- the HEAD which points to the last commit you made


When you make changes to your files and want to register those changes as a snapshot (commit) into the history, we take the following steps:

1. Stage / Propose your changes to the Index using 

```
git add <file_name>
```

2. Register the staged changes to the HEAD and register the commit

```
git commit -m "a meaningful but short message describing the changes you made"
```

3. Now, you have registered your commits and pointed your HEAD to the latest comment. However, the remote copy of your repository doesn't know about the changes you commited. We use the push command for this. 

```
git push
```
