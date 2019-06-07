# Branching and merging

## Introduction

Teams want to 
+ work on the same repository simultaneously
+ version control frequently
+ share their work 
+ maintain a working version of the library at all time

Git is a highly optimised tool to satisfy these complex and conflicting requirements.
However, to use it effectively, alignment on a robust workflow is required.

This document introduces the key concepts needed.

## Gitflow

Gitflow workflow is a Git workflow design that was first published and made popular by [Vincent Driessen at nvie](https://nvie.com/posts/a-successful-git-branching-model/). 
The Gitflow workflow defines a strict branching model designed for managing larger projects.  

The workflow assigns very specific roles to different branches and defines how and when they should interact. 
The key elements are feature branches, a development branch and a master branch.
It facilitates pull requests, isolated experiments, and more efficient collaboration.

## Branches

Branches are used to isolate work on different issues and experiments. 

To see existing branches:

    git branch
    
The current branch is highlighted with a star.
Note that this doesn't show all branches but only those that you have shown an interest in in the past.

Checkout an existing branch:

    git checkout branch_name

Have a look at `git branch` to see how the star changed. 
Note that work present on the old branch, will vanish in your file explorer if they are not present in the new branch.
Don't worry, the files will be visible again once you switch back to the old branch.

Create a new branch starting from the current branch (and commit)

    git branch new_branch_name
    
Branch names cannot have spaces and it is advisable to make them lowercase.
Check `git branch` to see that the new branch is created but we are still on the old branch.
We can change to the new branch via `git checkout new_branch_name`.

A shortcut for creating and immediately checking out the new branch is

    git checkout -b new_branch_name

Usually, only one person will work on any given feature branch.

Positive consequences
- Your work is isolated from experiments of others
- You can commit even if it is not perfect or even not working
- Commit often (many times a day)

Committing often is important because
- Enable granular version controlling
- If bugs appear, you can checkout past versions and find out where the bug krept in
- Each bit-size change is easy to parse for you and your teammates
- Write a clear commit message explaining why a commit was made. `Changes` or `qwerty` is not a good commit message.
- Ideally make one commit per file

Negative consequences
- Your work is not available to others
- Your work can become disconnected from the main development

To overcome these problems:
- Merge dev into the feature branch frequently (once a day)
- Break tasks into small to medium size chunks, complete only one chunk on one feature branch, then bring it into `dev` and start a new feature branch

## Merging

Git is a fantastic tool for combining work.
It is very good at working out what is new and what is old and can even handle multiple changes to the same file.
To integrate the latest work from branch `branch_name` into the current branch, use

    git merge branch_name

To get the work from the remote instead of local, use

    git merge origin branch_name

The main situation where this does not work well, is when there are two conflicting changes to the same line.
Git cannot work out on its own how to combine the work and will report a merge conflict.

The error message will say

    CONFLICT (content): Merge conflict in file_name
    Automatic merge failed; fix conflicts and then commit the result.

There are many merge tools to overcome this problem.
For example, PyCharm has a very good [merge tool](https://www.jetbrains.com/help/pycharm/resolving-conflicts.html).

Once you have resolved the conflicts, commit your changes to complete the merge.

## Pull requests

Pull requests are a tool to receive feedback and quality control on your work before contributing it to the development branch.
To make a pull request, first make sure your branch is up-to-date with the main development branch

    git pull origin dev
    
Then publish the latest version of your work to the remote repository.

    git push origin feature_branch

On the GitHub website, you will see a prompt to open a pull request into the default branch (`dev` in our case).
Provide a summary of what the feature branch is doing, select reviewers (usually your technical mentor and some team mates)
and assign the PR to yourself.

Pull requests show diffs, or differences, of the content from both branches. 
The changes, additions, and subtractions are shown in green and red, respectively.

By using GitHub’s @mention system in your pull request message, you can ask for feedback from specific people or teams, whether they’re down the hall or 10 time zones away.

It is usually enough to have one person's review.
However, if multiple people comment, make sure you address all the comments (either via a discussion or a code change).
Once the PR is approved, the person who raised the PR will

- Click on the green **Merge pull request** button to merge the changes into `dev`
- Click **confirm merge**
- Since you're now done with this new branch, delete the branch by clicking the **Delete branch** button.

Celebrate on slack!

## Stash

Sometimes you might produce a chunk of work on the wrong branch.
For example
- when thinking the change would just be one line but then turns into a larger piece
- when forgetting which branch is currently checked out

One usually remembers when trying to commit.
But it's not possible to change branch when there is uncommitted work.
The solution is

    git stash
    
Stashing takes the dirty state of your working directory — that is, your modified tracked files and staged changes — and saves it on a stack of unfinished changes that you can reapply at any time.
Once you ran `git stash`, your working directory is clean and you can conveniently switch branches.

You can then re-apply the changes (the last ones stashed) using 

    git stash apply

All stashed changes can be seen with `git stash list` and older stashes can be applied using `git stash apply stash@{ID}`,
where ID is the number of the stash to be applied (found by inspecting the stash list). 

## Tags

At DSSG, we you to use weekly tags to reference weekly milestones. 

To create a tag run `git tag <tagname>`. 

This will create a local tag with the current state of the branch you are on. 
When pushing to your remote repo, tags are NOT included by default. 
You will need to explicitly say that you want to push your tags to your remote repo.

To push your tag run `git push origin <tag>`. 
Or to push all tags (in the case there are multiple), you'd run `git push origin --tags`. 
In our case, we'll just be working with one at a time.

**Create and push an end-of-week tag each Friday.**

If feasible, we will also merge `dev` into `master` at that time.

## `.gitignore`

`.gitignore` files specify which files are ignored in a git repository. 

Example:

```
#ignore a single file
`mycode.class`

#ignore an entire directory
`/mydebugdir/`

#ignore a file type
`*.json`

#add an exception (using !) to the preceding rule to track a specific file
`!package.json`
```

Let's create an empty `.gitignore` file (touch `.gitignore`) and add some stuff!


## Some useful commands

This section contains some useful commands:

##### Discard changes
- `git checkout file_name.py`: discard changes made to file `file_name.py`
- `git checkout .`: discard all changes made to files currently tracked by git
- `git reset --hard`: discard changes in the working directory and changes that have been staged but not committed
- `git stash`: discard all local changes but store them for potential re-use later
- `git clean`: remove untracked files that are unknown to git (i.e. gitignored files are not removed)

##### Sharing with others

Pull:
- `git pull origin branch_name`: fetch the latest version of `branch_name` from github and merge into the current branch
- `git pull`: fetch the latest version of all branches from github. If the current branch is tracking a remote branch, merge the remote into the local branch. 

Push:
- `git push origin branch_name`: merge the latest version of the current branch into the remote branch called `branch_name`. This only works if a branch called `branch_name` exists.
- `git push -u origin branch_name`: create a remote branch called `branch_name` with the content of the current branch.
- `git push`: Abbreviation for `git push origin branch_name` where `branch_name` is the remote branch tracked by the current branch.

##### Check changes

- `git diff`: Show all changes made since the last commit
- `git diff file_name`: Show changes made to the file named `file_name`. If the file is not in your directory, write the whole path.

## Plan for the teaching session

1. Introduce gitflow
2. Everyone to discard changes from last session
3. Pull latest version from remote to get the dev branch
4. Introduce branches
5. View branches, checkout dev branch
6. Each team member, take on the task to update the readme one of the README.md sections: 
    - Project title & project summary
    - table of contents
    - partners 
    - contributors
7. Create a feature branch from dev for the task. Give the branch a suitable name. Checkout the branch.
8. Spend 1 min to make a small amount of progress on your task.
9. Diff your changes, add, commit. It's not perfect but ok since you're on a feature branch.
10. Create a second branch from dev
11. Edit the same section in the README.md but differently, diff, add, commit.
12. Merge the two feature branches (direction up to you)
13. Make another commit on the feature branch
14. TMs to demo raising a PR, requesting changes, addressing, approving, merging.
15. Everyone to raise a PR for their work in progress feature branches


## References:

There is a countless number of git tutorials out there
and you should be able to find answers to most questions on stackoverflow. 

Some resources that we like:
- [Cheat sheet](https://gist.github.com/davfre/8313299)
- [Git hello world tutorial](https://guides.github.com/activities/hello-world/)
