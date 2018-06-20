# GitHub Continued

**Agenda**

- Branches
- Committing (and why it's important to commit OFTEN!)
- Merging Branches
- Finding (and fixing) bugs with commit history
- `.gitignore`
- Tags
- Pull Requests

To get started, clone [this repo](https://github.com/dssg/github_practice/tree/mollie_edits).

## Branches

**Branching** is the way to work on different versions of a repository at one time.

By default your repository has one branch named `master` which is considered to be the definitive branch. People use branches to experiment and make edits before committing them to `master`.

When you create a branch off the `master` branch, you’re making a copy, or snapshot, of `master` as it was at that point in time. If someone else made changes to the `master` branch while you were working on your branch, you could pull in those updates.

This diagram shows:

- The `master` branch
- A new branch called feature (because we’re doing ‘feature work’ on this branch)
- The journey that feature takes before it’s merged into master

TKTK picture

Have you ever saved different versions of a file? Something like:

- story.txt
- story-joe-edit.txt
- story-joe-edit-reviewed.txt

**Branches** accomplish similar goals in GitHub repositories.

## Creating a Branch

### On Github:
- Go to [this practice repository](https://github.com/dssg/github_practice).
- Click the drop down at the top of the file list that says branch: master.
- Type a branch name (perhaps your name?) into the new branch text box.
- Select the blue **Create branch** box or hit “Enter” on your keyboard.

TKTK add video of this

### On Command line:

Create new branch with `git branch [branchname]`

Move to the new branch with `git checkout branchname`

Now you have two branches, `master` and your new branch. They look exactly the same, but not for long! Next we’ll add our changes to the new branch.

## Making and Committing Changes

Now, you’re on the code view for your new branch, which is a copy of `master`. Let’s make some edits.

On GitHub, saved changes are called commits. Each commit has an associated commit message, which is a description explaining why a particular change was made. Commit messages capture the history of your changes, so other contributors can understand what you’ve done and why.

Some reasons why COMMITTING OFTEN IS IMPORTANT:
- Committing often makes each bit-size change easy to parse for your teammates
- If bugs appear, you can checkout past versions and compare the commit history. If you are committing often, it will be much easier to find where the bug krept in. 

**Rid yourself of your fear of committment!**

There are five practice files in the [practice repo](https://github.com/dssg/github_practice/tree/master). Let's split up which document we'll work with based on rows. 

### On Github:

- Click the README.md file.
- Click the  pencil icon in the upper right corner of the file view to edit.
- In the editor, write a bit about yourself.
- Write a commit message that describes your changes.
- Click Commit changes button.

### On the Command Line: 

1. Open your practice markdown file
2. Make a change somewhere in the document. Perhaps you want to profess your love for your favorite sweets, or add some new confections to the [cupcake ipsum](http://www.cupcakeipsum.com/). Or, go crazy and just make your own file with whatever gibberish you like.
3. Add file to staging -  - `git add *`
4. Commit your changes -  - `git commit -m 'some description of edit I just made'`
5. Push  - `git push`

## Merging branches

**Note: If at this point you wanted to merge the branch without a pull request, you would do the following; however, for this example, we'll skip ahead to the pull request**

### On Command Line:

- Switch to master - `git checkout master`
- Merge the edits from your branch - `git merge [branchname]`
- Delete old branchname - `git branch -d [branchname]`

## Using commit history to find bugs

Why is committing so important you might ask? Well, one reason is that you can use your commit history to find bugs!!! Let's take a look at how that might be done.

Run `git log` to see your commit history. From here, you can use the version commit number to checkout different versions of your code.

To explore a past version, you can simply run `git checkout [revision]` where `revision` is the commit hash (for example: 12345678901234567890123456789012345678ab). You are now viewing the code as it was during that version! Let's say a bug has crept into the code at some point, and you're trying to find where that happened. You can simply checkout various versions of your code, run the buggy file, and find the point at which the bug was introduced.

Then, you'll want to look at the difference between the last version where the code was not present, and the first version where it was introduced. You can check out these differences by running `git diff [revision1] [revision2]`. So, for example, something like `git diff d8f59d0d27a50adba45a54fd50047ea94d6effcf 12f74c691786445d675f1b45ed244778eb3328dd`.

Something to keep in mind is that if you are **not** committing often (for example, committing every few days instead of multiple times a day), this process will be unhelpful because the differences will be so large and the commit messages will not be very meaningful/helpful. 

Make sure to commit often with informative commit messages! :)

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

Let's create an empty `.gitignore` file (touch `.gitignore`) and play around!

## Tags



## Opening a pull request

Pull Requests are the heart of collaboration on GitHub. When you open a pull request, you’re proposing your changes and requesting that someone review and pull in your contribution and merge them into their branch. Pull requests show diffs, or differences, of the content from both branches. The changes, additions, and subtractions are shown in green and red.

As soon as you make a commit, you can open a pull request and start a discussion, even before the code is finished.

By using GitHub’s @mention system in your pull request message, you can ask for feedback from specific people or teams, whether they’re down the hall or 10 time zones away.

You can even open pull requests in your own repository and merge them yourself. It’s a great way to learn the GitHub Flow before working on larger projects.

- Click the **Pull Request** tab, then from the Pull Request page, click the green **New pull request** button.
- In the **Example comparisons** box, select hte branch you made to compare with `master` (the original).
- Look over  your changes in the diffs on the compare page to make sure they're what you want to submit.
- When you're satisfied these are the changes you want to submit, click the green **Create Pull Request** button.
- Give your pull request a title and write a brief description of your changes.
- Click **Create pull request**!

### Merging a Pull Request

In this final step, it’s time to bring your changes together – merging your readme-edits branch into the master branch.

- Click on the green **Merge pull request** button to merge the changes into `master`
- Click **confirm merge**
- Since you're now done with this new branch, you can delete the branch by clicking the **Delete branch** button.

## Github Command Line Cheatsheet

There are a bunch of these out there, but here is [one](https://gist.github.com/davfre/8313299) that you might find useful on your journey.

