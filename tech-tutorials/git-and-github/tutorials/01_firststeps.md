In this tutorial, we will go through some git basics, using commands that you will use again and again in your work. Git is a pretty amazing tool, and you will only be scratching the surface in the next half hour. Still, you should be able to use git to keep a history of your changes to files, to exchange your work with others, and to build on their changes in return.

Don't worry if the commands seem like arcane incantations for now; we will cover many of the concepts that underlie them in the coming weeks.

Your group is composed of fellows with different levels of experience with git. Help each other loads, and ask each other all the questions!

# Commands you'll learn

In this tutorial you'll be using the following commands:
* `ls -a`: List files in a directory (`ls`) even ones that begin with `.` (`-a`)
* `cd`: Change directories
* `git clone`: Clone a repository from GitHub (or another "remote")
* `git add`: Tell `git` you'd like to save changes to this file in your history
* `git commit`: Tell `git` you'd like to save the changes you've `git add`ed
* `git status`: Your favorite command: "What's going on?!"

# First Things First

First things first: You need to create a repository (which is the place that stores your work and changes). There are several ways to do this, but one of the most convenient ones is to start on GitHub - that way, your repo will be super easy to share with your... fellow fellows.

1. **Learner A**: Go to [github.com](https://github.com/), log in, and find the 'New Repository' button. Name your repo 'rhymes', and give it a short description if you like; the remaining options can be left at their default. (Ask your partners for details if you're interested!)

2. **Learner A**: Now, you need to get the repo on your local machine! Find (or have your partners point you to) the 'Clone or download' button, and copy the URL that pops up. Then go to your command line and do: `git clone https://github.com/username/rhymes.git`, where you need to substitute the URL for the one that you just copied from GitHub.

3. **Learner A**: Once git is done copying all kinds of things from your newly creating repo on github, we can look around a bit. First, go into the new folder that has the same name as your repo: `cd rhymes`.

 Say `ls -a`; you will see that git has created the (hidden) directory called `.git`, where it stores all its inner workings. If you say `git remote -v`, you can see where you cloned your repo from (and where changes will go to later!). Saying `git status` tells you that you are at the start of working on this repo, and, importantly, that there is 'nothing to commit'. This means that you haven't told git to keep track of anything yet.

4. **Learner A**: In your 'rhymes' folder, add a new file called `words.md`. Open it, and add a few words that rhyme. Pro tip: Ask your partners for suggestions as to what rhymes with 'orange'.

5. **Learner A**: Do `git status` again. What has changed?

6. **Learner A**: You need to tell git that you'd like take a snapshot of your work (which you can later go back to and do all kinds of interesting things with). Say `git add words.md`. Then check `git status` again. Do you see how git now tells you how `words.md` is now among the 'changes to be commited' (i.e., the changes that will go into your snapshot)?

7. **Learner A**: It's time to take the snapshot! Say `git commit -m 'blablabla'`, where you should substitute the `blablabla` with a short description of what you have done in this snapshot, like `'create file with rhymes'`. Congratulations! You have made a _commit_ to your repo. Check `git status` again.

8. **Learner A**: Over time, you will do many commits. To see a list of them, do `git log`. There's only one so far!

Go to the [next tutorial](02_showtheothers.md).

-------------

![git 2](https://imgs.xkcd.com/comics/git_commit.png)

[Image source](https://xkcd.com/1296/)
