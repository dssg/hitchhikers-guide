Sometimes, you want to keep a files in your repo's directory local, and not share it. Git has an app, errm, file, for that!

# Commands you'll learn

In this tutorial you'll be using the following commands:
* `.gitignore`: A file that lists files (or file and folder name patterns) that should be excluded from commits.

# Keeping It Special

1. **Learner B**: You would like to add an ingredient to the soup which should _not_ be mentioned to the public, or your partners. Create a file `sauce.secret`, and name your secret ingredient in it. Do a `git status`. What does git think about your new file?

2. **Learner B**: Create a `.gitignore` file, and add a line saying `*.secret` to it. Do `git status` again. What has changed? Your secret file should no longer appear there.

3. **Learner B**: Tell git that you want it to include the `.gitignore` file in your commit: `git add .gitignore`. Then commit and push your changes.

4. **Learner A and C**: Get the changes that Learner B just made: Say `git pull`. List all files (includen hidden ones) with `ls -a`. Did you receive the `.gitignore`? What about the `sauce.secret`? Which of those two files appears in the repo on GitHub? Also have a look at your `git log`.

Here is the [next tutorial](05_backtothepast.md).