# I Just Want To Go Back

Sometimes, you check out a repo, happily working along, and then just screw your files up badly. Let's do that.

1. **Learner A, B, and C**: Go to your 'soup' repo from the previous exercise. Just to be sure that everybody is up to date, everybody should call `git pull`. You can also have a look at your `git log`; they should all look the same.

2. **Learner A, B, and C**: Individually, do something bad to your local files (only in the repo, of course!). Delete the `ingredients.md`, or delete lines in one of the files, and then save them. **Learner B**! Do **not** delete your `sauce.secret`! It has never been committed, so you cannot get it back!

3. **Learner A, B, and C**: Now, again individually, you decide that those working changes were really not great, and you want to restore the last commit. There are several ways of doing this in git. Say `git status` - it will recommend one possible way.

4. **Learner A, B, and C**: As `git status` tells you, you can use `git checkout -- <filename>` to discard your working changes. If you call `git checkout -- .`, you will discard all your working changes in your current directory, and thus be thrown back to the last commit. _Be super careful._ This _discards_ your working changes. They will be lost. (If you feel like it, google `git stash` at this point if you would like to back up your working changes, just to be safe.)

5. **Learner A, B, and C**: What do you do if you have _committed_ changes that you would like to undo? That is, if you want to go back to a commit far back in time? There are really neat ways of doing this in git, even if you have already pushed (shared) your newer commits to GitHub. Cliffhanger: You will learn about this in the git branching tutorial. (`git revert` and `git reset` is where it's at.)

Done already? [Here](05_solveyeconflicts.md) is an optional next tutorial.

-----------

![back](http://media1.s-nbcnews.com/j/newscms/2015_01/831346/150102-back-to-the-future-mn-850_6c1cc5c2a0c7767b593e1bf9054a4d0f.nbcnews-fp-1200-800.jpg)

[Image source](http://media1.s-nbcnews.com/j/newscms/2015_01/831346/150102-back-to-the-future-mn-850_6c1cc5c2a0c7767b593e1bf9054a4d0f.nbcnews-fp-1200-800.jpg)