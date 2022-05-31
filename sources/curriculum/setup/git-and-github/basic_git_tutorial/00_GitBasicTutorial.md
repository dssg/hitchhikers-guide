## What is Git?
Git is a free version control system which helps you keep track of file changes in your computer. Think of it as a time machine that lets you go back to any point in your project development.


## Why we use it 

### Commits
Git can save snapshots of your work called `commits`. Once you register a set of changes as a `commit`, you can go back and forth to check the state of your project. 
Let's say you were experimenting with some new function and realized the old one was better, no problem, you can bring back anything!


The evolution of your project can be stored as a series of commits. Typically, we would have a local copy and a remote copy of the repo (just like you do with Google Drive).

### Github

There are many providers that let you store your git repositories, but the most popular one is Github (we'll use github for DSSG).

Apart from storing a copy of your projects, github comes with a lot of useful features. For example, you can use it to share your projects with your colleagues, so they can see (or modify if you want) your project.

## How do we use git? 
let's take a look at how we can use git. 

### How to initialize your git repository? 

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
