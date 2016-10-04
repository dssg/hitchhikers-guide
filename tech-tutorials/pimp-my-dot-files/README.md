# dotfiles - working on every computer and feel just like home

On this tutorial, you'll learn about `dotfiles`, what they are, why are they important and how to use them.

## What are dotfiles anyway?

Dotfiles are used to configure system settings, you can configure anything from them. From text editor syntax to a list of commands to execute each time you open a terminal session.

Dotfiles names start with `.`, e.g. `.bash_profile`, `.Rprofile`, `.vimrc` and most of them reside in your home folder. As you get familiar with the command line, you are going to start tweaking your computer with personal settings. Maybe setting special shortcuts for common commands (e.g. typing `jnb` to start Jupyter instead of typing `jupyter notebook`).

As your system becomes more and more customized, it's going to be pretty different to the original configuration. So imagine you have dozens of nice shortcuts and configuration settings for your favorite applications, then you start working on the DSSG server and all the magic is gone... not cool.

A common practice is to store your files in a git repository. This way you have a history of the modifications you've done but more important, a copy you can grab from anywhere (e.g. the DSSG server) and get all your magic.

## Finding your dotfiles

Most applications store a dotfile in your home folder, type the following in the command line to see yours:

```bash
find . -name '.*' -maxdepth 1
```

Here are some of mine:

```bash
.Rprofile #settings for your R sessions
.vimrc #vim settings
.bash_profile #shell settings
```

Let's see how my `.Rprofile` looks:

```R
## Change colors when running R in the terminal
if (Sys.getenv("TERM") == "xterm-256color") library("colorout")
```

If you have an `.Rprofile ` file, Whatever it is there will be executed when you start an R session. Mine just loads a package `colorout` which adds nice colors to the R interpreter.

**Note:** even though every dotfile starts with `.`, not everything that starts with a `.` is a dotfile. For example `.DS_Store` is a file you'll find on many folder if you use OS X, this file stores custom attributes for the folder but you don't want to modify it directly, it's just a file the system uses to keep track of folder customizations (e.g. changing the icon)

## `.bashrc` and `.bash_profile`

When you open a terminal, a program called `bash` starts, this program let's you execute commands such as `cd`, `ls`, etc. Bash is highly configurable through its dotfiles: `.bashrc`and `.bash_profile`. There are some differences between those two and they get executed at different times, but a nice setting to get started is to make `.bash_profile` call  `.bashrc` and set your configuration file in the later. To to that follow this steps:

```bash
# open .bash_profile
open ~/.bash_profile
```

Your default editor will open the file, chances are the file contains some settings already, to avoid breaking your system, do not delete anything and just put this at the top of the file.

```bash
# just load ~/.bashrc
if [ -f ~/.bashrc ]; then
   source ~/.bashrc
fi
```

Now you can start twerking your shell, for example adding shortcuts. Let's create one that outputs only folders in our current working directory.

First, open your `.bashrc`:

```bash
open ~/.bashrc
```

Add this line:

```bash
# List only directories
alias lsd='ls -l | grep "^d"'
```

Save the file. Close the terminal and open a new one.

Now, every time you execute  `lsd`, your command line will print only folders in the current directory and not the files.

Ok, that was a pretty simple example, not let's see how to use git.

## Using git to manage your dotfiles

As I mentioned before, your dotfiles live in your home folder (type `cd ~; pwd` to see which is yours). Your home folder contains a lot of stuff and you probably don't want to create a git repo there (please don't). To solve this issue we can do the following: create a folder anywhere in your computer, create your dotfiles there and then link them to your home folder, where your applications expect your dotfiles to be.

Let's imagine you want to save your dotfiles in `~/dotfiles`. Run the following to create the folder add some files and start a git repository:

```bash
# create and move to the folder
mkdir ~/dotfiles; cd ~/dotfiles
# get the content from your original .bashrc and copy it in your
# .bashrc stored in ~/dotfiles, to the same with .bash_profile
cat ~/.bashrc > ~/dotfiles/.bashrc
cat ~/.bash_profile > ~/dotfiles/.bash_profile
# init repo and commit
git init
git add --all
git commit -m 'dotfiles are awesome'
```

Now you have a copy of your `.bashrc` and `.bash_profile` outside your home folder and you created a repo to store them. But there's one step missing, if you modify your dotfiles in `~/dotfiles`, your computer won't do anything because it will look in your home folder. To fix it we need to link our files in `~/dotfiles` to our home folder.

To do that we'll create *symlinks*, which are basically pointers to files, that way you can store your dotfiles anywhere and your computer is still going to find them.

```bash
# link files in ~/dotfiles to your home folder
ln -s ~/dotfiles/.bashrc ~/.bashrc
ln -s ~/dotfiles/.bash_profile ~/.bash_profile
```

Now, you can modify, commit, push, pull from `~/dotfiles` and still make your computer find them in your home folder!

Now, create a remote repository to host them on github. If you don't know how, check out the [git tutorial](../gitandgithub).

## Using your dot files in another machine

At this point you setup your dotfiles (only two for now) using git, you can version them and backup using github. Let's see how to bring your dotfiles to a new machine.

First, login in the new machine and clone your repo:

```bash
git clone https://github.com/youruser/yourrepo
cd yourrepo
```

You just got your files, now it's time to link them to your home folder on this new machine.

```bash
ln -s .bashrc ~/.bashrc
ln -s .bash_profile ~/.bash_profile
```

Now, you can use your local settings in the server!

## It's all about automation

Manually linking each dotfiles is tedious, let's automate it. The easiest way of doing it is to add a script in your repo to run the code to create the links, the problem is that every time you create a new dotfile, you'll also need to update the script. If you only have a couple of dotfiles this is fine.

But if you want superpowers, you can automate the process so next time you use a new machine, setting up your dot files will look like this:

```bash
git clone https://github.com/youruser/yourrepo
cd yourrepo
./install
```

There are many ways of doing the `./install` step but you need to be familiar with bash.  If you want to see examples of it, [see this](http://dotfiles.github.io/).

## Resources

* [dotfiles - unofficial guide to dotfiles on Github](http://dotfiles.github.io/)
