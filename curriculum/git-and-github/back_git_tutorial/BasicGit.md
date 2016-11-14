# Basic Git Tutorial

# Git in a nutshell

![git](https://imgs.xkcd.com/comics/git.png)

[Image source](https://xkcd.com/1597/)

Git is a version control system which helps you keep track of file changes in your computer. 
Think of it as a lab notebook that lets you go back to any point in your project development and allows you 
to safely collaborate with others on a shared project. 

While git is most used in software development, you can use it for anything you like
([writing books](https://www.gitbook.com/), for example), as long as your files are plain text
(e.g., source code, latex files), you won't have any issue with git (this guide is actually hosted using
git, git-ception!).

Simply speaking, git saves snapshots of your work called `commits`, after a `commit` is done, you can go back
and forth to check the state of your project, maybe you were experimenting with some new function and realized
the old one was better, no problem, you can bring back anything!

![git 2](https://imgs.xkcd.com/comics/git_commit.png)

[Image source](https://xkcd.com/1296/)

The entire development of your project is stored in your computer, but we know that's dangerous, so you can 
also host a remote copy on a server like GitHub, Bitbucket, or GitLab. 


# Git outline

0. Configure your git client

1. Create a git repository
   - Create a repo 
   - Create your first commit
     - Add a file
     - Put it in the staging area
     - Make a commmit
 
    
2. Inspecting your log-file

3. Rolling-back to previous versions 

4. Git Ignore

5. Git Branching

6. Solving Git Conflicts

5. Collaborating with other GitHub 
   1. Solo Flow
   2. Open-Source Flow
   3. GitHub Flow
      Issues
      PR requests
   
