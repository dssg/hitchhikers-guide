A# Create a Repository

Let's work on creating our first git repository.

All shell commands will be prefixed with `>`
All comments, text not meant to be parsed by the computer,
is prefixed with `#`.


## Create a git repository
First create a directory for our project and `cd` into the directory
```
> mkdir -v nyc-311
> cd nyc-311
```
The `-v` flag produces verbose output so you can see what happened after the invocation of the command.

Now lets initialize the git repository. All git commands start with `git <verb>`.  To initialize the git repo
for our project we invoke the command
```
> git init
```
Let's look at the contents of our directory using the command `ls -a`
```
> ls -a

.  ..  .git/
```
The `-a` flag tells the `ls` command to include hidden directories when displaying files. We can see that there
is now a `.git` directory.  *Unless you really know what you are doing* **DO NOT EVER** *modify anything in this
directory. If you delete this directory, the entire history of your project will be gone.*

## Make our first commit!!

All good projects should have a README.md to describe the project. So let's start with that. Fire up
you favorite text editor and name a file `README.md`.

Add something like this in your README:
```
# Exploring 311 Calls in NYC

## Description

This repo is for an analysis of 311 calls in NYC using Python 3.4
```
The `#` are part of `markdown` syntax for designating headings.

Now let's look at the status of our repo using `git status`:
```
> git status
On branch master

Initial commit

Untracked files:
  (use "git add <file>..." to include in what will be committed)

          README.md

          nothing added to commit but untracked files present (use "git add" to track)
```
We can see that git knows that we have added a file but it is `untracked`. What this means is that `git`
knows that this file has been added but it is currently "untracked" by git. Like the command said let's use `git add` to
track changes in the the file by invoking the command `git add README.md`.
```
> git add README.md
```
Now lets look at the status of the repository by invoking the command `git status` again.

```
> git status

On branch master

Initial commit

Changes to be committed:
  (use "git rm --cached <file>..." to unstage)

          new file:   README.md
```
Now that we have added the file it has been "staged" in the staging area. We can now make our first commit!
```
> git commit
```
When you invoke this command an editor should pop-up and you have to leave a commit message. Good commit
messages lead to a usable git log and separates the novice git users from the competent practitioners.
Generally you should follow these guidelines in a commit message:

1. First line is a one line summary of the commit that is in title case and less
then 80 characters, written in the imperative voice.

2. Second line should be blank.

3. Third and subsequent lines should be more details of the commit.

Anyone can look at a commit and examine what was changed. The commit message
is where you provide a context of what and why you did what you did in the project.

A good rule of thumb is *If applied this commit will, <insert title of git message here>*

My commit message is the following:
```
Checking in README file

* Added short description of the project
* Added python3 as a dependency

### Using Nano as a text editor
```
>If you are using nano, to save your text use Ctrl-O, write a filename
>and to exit use Ctrl-X.

Now that we have made our first commit we can examine our log!
```
> git log
```
The first line should output
```
* commit aaf89fd77e9b43d99fe32823843a7519b2108c90
  Author: Clark Kent <clark.kent@dailyplanet.com>
  Date:   Sat Nov 05 13:45:11 2016 -0600

          Checking in README file

          * Added short description of the project
          * Added python3 as a dependency
```
The first line is a unique identifier of your commit. The second
give information on who made the commit. The third line gives the
date. The rest is the commit message.

To just get titles of commit messages you can use the following command
```
> git log --oneline
```
Another useful command is
```
> git log --oneline --graph --all --decorate
```

## Some helpful commands
Removing files via git allows them to be recovered.
```
git rm FILENAME
git rm -r DIRECTORY
```
Renaming files can be done by moving a file and then
adding it or you can use the following command:
```
git mv OLD NEW
```
`git rm` and `git mv` will stage the changes that will ulimately
need to be commited.
That is it we have our first commit and repo! Next we are going to write some code!
