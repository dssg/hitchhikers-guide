# Branching and merging

## Introduction

Teams 
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
The key elements are feature branches, a development and master branch.
It facilitates pull requests, isolated experiments, and more efficient collaboration.




## Some useful commands

This section contains some useful commands:

##### Discard changes
- `git checkout file_name.py`: discard changes made to file `file_name.py`
- `git checkout .`: discard all changes made to files currently tracked by git
- `git reset --hard`: discard changes in the working directory and changes that have been staged but not committed
- `git stash`: discard all local changes but store them for potential re-use later


# TODO:
- create dev branch for each repo
- make dev the default branch
- introduce pull/push
- ask team to pull the latest repo
- introduce view branches, checkout branches
- give everyone the task to update one part of the readme: (Project title & project summary, table of contents, partners, contributors). I will do project title for one team.
- please create a branch with a suitable name (no spaces, lower case)
- introduce create branches, view branches, checkout branches
- Everyone to make a change to their section, diff, add, commit.
- Frequency of committing: Often. Clear messages. Ideally one per file. Often in the day. It doesn't need to be working.
- Create a second branch (different name)
- Edit the same section but a bit differently
- merge the new branch into the old branch
- open the file to show what happens
- show pycharm 3 way merge
- say that usually git is very smart. It only gives conflicts if it can't figure it out.
- resolve conflict - commit.
- make 2 more commits to the feature branch.
- merge in dev
- I will push my branch and show pull request
- lili to review and request changes
- I to fix
- lili to review and approve
- I to merge.
- Everyone to gain push rights (maren to prep groups before and just grant write access) and raise PR
- put me or lili as reviewer
- We will not review until actually happy. Remove me as reviewer and message us when actually happy.




