# GitHub

* This part of the tutorial will go over how to host your project on GitHub
* The virtue of using a `.gitignore` file
* The GitHub workflow
* How to solve a merge conflict

## What is GitHub?

There are several popular providers --[Bitbucket](bitbucket.org), [GitLab](gitlab.com) --
that let you store your git repositories but the most widely used is [GitHub](https://github.com/).

Apart from storing a copy of your projects, GitHub comes with a lot of useful
features. For example, you can use it to share your projects with your
colleagues so they can see or modify your project. Is is also
a collaboration tool that you can use to work as a part of a team.

## Getting started on GitHub?
1. Go to https://github.com and create a free account.

2. Create a new repository called *NYC-311*

3. The repository URL will then be
*https://github.com/username/NYC-311*

4. Add the remote repository in your local repository
```
> git remote add origin https://github.com/username/nyc-311.git
```
You can then see the remote repository with the following command
```
> git remote -v
```
The remote is named "origin" which is a common choice for the
primary repository.

Now we are going to `push` the local changes on our repository
to the GitHub repository using the command
```
> git push --set-upstream origin master
```
What we have done is taken a copy of our repository and `pushed` it
to GitHub. When you push changes to GitHub in the future you just
need to use the command
```
git push origin master
```

To pull in changes in your repository done by yourself or
another person you can use the following command
```
git pull origin master
```

To see this in action grab a friend and have them `clone` your
repo with the command. First make sure they also have a GitHub
account and add them as a collaborator to your repository. If
you can't find a friend you can still do this part of the tutorial
just skip the parts about using `git clone` and `git pull`.
```
> git clone https://github.com/username/nyc-311.git
```
They will then have a copy of your repository. Now `cd` into
the project folder and add a special file called `.gitignore`.
Fire up a text editor and add the following
```
#Ignore pyc files
*.pyc
```
The `.gitignore` file is a special file that git looks at when trying
to make a commit. We added the entry '*.pyc'. This is an instruction
for git to not commit files that end in `.pyc`. Files that end
in pyc are python bytecode files that will appear when you run your
python code. All lines prefixed with `#` are comments and will be
ignored; they are meant to be read by people not computers.

Now lets add this file to our repository
```
git add .gitignore
git commit -m "Added .gitignore"
```
And push our changes to the repository
```
git push origin master
```

Now on your machine `git pull` the new state of the repository
```
git pull origin master
```
If we then use the command `ls -a` you should then see the .gitignore file.

And if we look at the log using 'git log` you should see the new commit.

## GitHub Flow

In this portion of the tutorial we will go over branching and the
general GitHub workflow.

So far we have been doing the "solo" workflow which consists
of the following:
```
  mkdir my_working_directory
  cd my_working_directory
  git init
  touch some_file.py
  # hack
  # hack
  git add some_file.py
  git commit -m "Working with some awesome idea"
  git push origin master
  # hack
  # more hack
```
We are now going to introduce the GitHub flow that is largely done in
teams.

In the GitHub flow we never code anything unless there is a need to. When
there is a need we then create an issue on the GitHub repository. Good
issues should be

- Clear
- Defined output
- Actionable (written in the Imperative Voice)
- Could be completed at most in few days
- Examples
  - *Good*: /Fix the bug in .../
  - *Good*: /Add a method that does .../
  - *Bad*:  /Solve the project/
  - *Bad*:  /Some error happen/

Here is how to create a GitHub [issue.](https://help.github.com/articles/creating-an-issue/)

Once we have an issue we will then pull from the repo and create a *branch*.
A *branch* is a copy of the code base separate from the main master branch
where we can work on our issue (e.g, fixing a bug, adding a feature) without
affecting the master branch during our work and then ultimately merge our
change into the master branch.

The flow goes something like this:
```
## Pull from the repo
git pull
## Decide what do you want to do and create an issue
git checkout -b a-meaningful-name
```
The command `git checkout -b` creates a new branch which in this case
is named "a-meaningful-name". We can see what branch we are on by using
the command `git branch` which will show all the branches in the local
repository and place an * next to the branch we are currently on.
```
## hack, hack, hack, add/rm, commit
## Push to the repo and create a remote branch
git push
## Create a pull-request and describe your work (Suggest/add a reviewer)
## Someone then reviews your code
## The pull-request is closed and the remote branch is destroyed
## Switch to master locally
git checkout master
## Pull the most recent changes (including yours)
git pull
## Delete your local branch
git branch -d a-meaningful-name
```
Here is how to create a GitHub [pull request.](https://help.github.com/articles/creating-a-pull-request/)

## Solving a merge conflict

As you work on projects with others you will inevitably run into
merge conflicts. A merge conflict is caused when you and another
person edits the same line of a file. Git will not know which
line is the correct one and create a conflict.

Let's make a conflict!
```
#create a branch called drama
> git checkout -b drama
#now modify the descriptive_stats.py file and change the top 10
#values to top 13
#commit your changes
> git add descriptive_stats.py
> git commit -m "Changed top 10 to top 13 in descriptive_stats.py
#switch back to master
> git checkout master
#now modify the descriptive_stats.py file and change the top 10
#values to top 3
# commit your changes
> git add descriptive_stats.py
> git commit -m "Changed the top 10 to the top 3 in descriptive_stats.py"
```
Now we are going to merge the drama branch into the master branch
```
> git merge drama

Auto-merging descriptive_stats.py
CONFLICT (content): Merge conflict in descriptive_stats.py
Automatic merge failed; fix conflicts and then commit the result.
```
Our arbitrary drama has now lead to a conflict.
If we check the status we should see the following
```
On branch master
You have unmerged paths.
  (fix conflicts and run "git commit")

  Unmerged paths:
    (use "git add <file>..." to mark resolution)

            both modified:      descriptive_stats.py
```
Let's examine the conflicting file `descriptive_stats.py`, you should
see the following:
```
from __future__ import print_function
import pandas

fname_data = '311-service-requests.csv'
df_311_calls = pd.read_csv(fname_data)
<<<<<<< HEAD
print(df_311_calls['Complaint Type'].value_counts()[:3])
=======
print(df_311_calls['Complaint Type'].value_counts()[:13])
>>>>>>> drama
```
The `>>>>>>>` and `<<<<<<<` denote the section of the conflicting code. `HEAD`
means the following line if from the maser branch while `drama` shows that
the preceding line is from the drama branch. The lines of the two branches
are separated by the `=======`. Given a merge conflict we have
three choices: either keep the line from the master branch, keep the line
from the drama branch or create an entirely new line. In this case we are
going to keep the line from the master branch. To do that we delete the
merge conflict markers and the line from the drama branch and then make a
commit.

Your code should look like this:
```
from __future__ import print_function
import pandas

fname_data = '311-service-requests.csv'
df_311_calls = pd.read_csv(fname_data)
print(df_311_calls['Complaint Type'].value_counts()[:3])
```
Now add this file and make a commit.
```
git add descriptive_stats.py
git commit -m "Fixed merge conflict in descriptive stats"
```
Our merge conflict is know solved.

That concludes the tutorial on GitHub! Good Luck!

## Acknowledgements, References and Furthur Resources

This tutorial is derived from tutorials created by Eduardo Blancas Reyes,
Benedict Kuester, Adolfo De Unanue, [Software Carpentry](swcarpentry.github.io/git-novice/),
and [ASU PHY-494](asu-compmethodsphysics-phy494.github.io/ASU-PHY494/2016/01/21/git_basics/).

Furthur resources for becoming a git master are:
* [Software Carpentry](swcarpentry.github.io/git-novice/) -- a more in-depth intro tutorial

* [15 minute tutorial to learn git](https://try.github.io/levels/1/challenges/1) - Intro tutorial.

* [git - the simple guide](http://rogerdudler.github.io/git-guide/) - A simple guide to get to know
the most important concepts.

* [A successful git branching model](http://nvie.com/posts/a-successful-git-branching-model/) - A
model to work with git using branches. This model is widely used in the open source community.

* [Learn Git Branching](http://learngitbranching.js.org/) - Understanding what branches and rebases
are, in an amazing interactive tutorial.

* [Reset Demystified](https://git-scm.com/blog/2011/07/11/reset.html) - A blog post on `git reset`
which develops some useful concepts along the way.

* [Understanding git for real by exploring the .git
directory](https://medium.freecodecamp.com/understanding-git-for-real-by-exploring-the-git-directory
-1e079c15b807#.5pe75gc07) - A blog post on what's inside a commit.

[Pro Git](https://git-scm.com/book/en/v2) -- An in-depth discussion written by git masters.
