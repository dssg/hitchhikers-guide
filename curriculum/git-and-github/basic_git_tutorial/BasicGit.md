# Git Overview

## Git in a nutshell

![git](https://imgs.xkcd.com/comics/git.png)

[Image source](https://xkcd.com/1597/)

Git is a version control system which helps you keep track changes in files you make during the development
of your project. Think of it as a lab notebook that lets you go back-and-forth to any point in your project,
an undo button, and a tool to safely and efficiently collaborate with others on a shared project. 
All serious software projects use version control. 

While git is mostly used in software development, it can be used for anything you like
([writing books](https://www.gitbook.com/), for example), as long as your files are plain text
(e.g., source code, latex files). 

Simply speaking, git saves snapshots of your work called `commits`; after a `commit` is created, you can go back
and forth through different commits in your project -- maybe you were experimenting with some new function and 
realized the old function was better, no problem, you can bring back anything! The collections of commits and associated
metadata form the `repository` of your project. 

![git 2](https://imgs.xkcd.com/comics/git_commit.png)

[Image source](https://xkcd.com/1296/)

The entire development of your project, the `repository`, is stored on your computer, but we know that's
dangerous, so you can also host a remote copy on a server like GitHub, Bitbucket, or GitLab. Hosting a project's
`repository` on GitHub also allows for the distribution of your work and collaboration. This prevents 
endless emailing of source code and the following situation: 

![final](www.phdcomics.com/comics/archive/phd101212s.gif)


## git sounds awesome! How do I get it?

Chances are, git is already installed on your computer. To check open-up a terminal and type `git`. 
If not, you can get it from [here](https://git-scm.com/).

OS X users: use `homebrew` 
    
## Can I get buttons and stuff?

`git` is a command line tool, which means it doesn't natively have a graphical user interface. Using the
git cli is the most flexible way of working with git, and if you are working on a remote server you will 
unlikely be able to use a GUI. 

However, if you still want a GUI (e.g., for using git on your computer), here are some options 
available:

*   [Options for Mac](https://git-scm.com/download/gui/mac)
*   [GitKraken](https://www.gitkraken.com/) (Windows and Mac)

*Keep in mind that if you are logging into a remote machine like AWS. A GUI may not be an option.*

This tutorial will cover the basics of `git` and hosting a project on GitHub. 


## Configure your Git Profile

First things first. You need to configure you git client so your commits are attributed to you
and you get pretty output. Do the following: 

```
# How my git configuration currently look like
git config --list
```

 My workspace

```
# Adding some, if you don't have a user.name or user.email set
git config --global user.name "Clark Kent"
git config --global user.email "clark.kent@dailyplanet.com"
git config --global color.ui "auto"
git config --global core.editor 'nano' #or vim, emacs sublime
```

Also do the following (important)
```
git config --global push.default current
```
You know have your `git` client configured. Next we will create 
our first repository. 
