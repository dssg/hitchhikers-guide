# Adding to It

While having a repo for yourself is nice for version control, how do you add to somebody elses work? There are some pretty neat ways of handling this, but right now, we'll go through one of the simplest.

1. **Learner C**: Create a new repo called 'soup', and add Learner A and Learner B as collaborators.

2. **Learner C**: Add a file 'ingredients.md'. Populate it with a short list of ingredients that would make a medieval witch scratch her head. Commit your list. Add a few more ingredients (or delete some!). Commit again. Push your commits.

3. **Learners A and B**: Get the necessary URL from Learner C, then clone Learner C's 'soup' repo (`git clone https://github.com/learnerc/soup.git`, where you need to substitute the correct URL), and go into the repo's folder: `cd soup/`

4. **Learners A and B**: Do `git log` to see what Learner C has been up to so far.

5. **Learner C**: Add another ingredient to your file, commit and push again.

6. **Learner A and B**: As Learner C has added more stuff, you need to update your local clone of their repository! To do this, call `git pull`. Check what just happened with `git log`. Do you see the new commit that Learner A only added to their repo _after_ you first cloned it?

7. **Learner A**: In the repo's folder, create a new file called `spices.md`. In that file, list some fantasmorgacically hot spices. Do a `git status`. What does have git to say about your new file so far?

8. **Learner A**: Do `git add spices.md` to tell git that it should start caring about your file.

9. **Learner A**: Do `git commit -m 'blablabla'` to create a new snapshot (commit) of the repo as you have it now, which includes your new file. You should probably make the commit message more meaningful than 'blablabla'.

10. **Learner B and C**: Pull the changes that Learner A made, and show them that you now have the spice list. Also show `git log`.

11. **Learner B**: You would like to add an ingredient to the soup which should _not_ be mentioned to the public, or your partners. Create a file `sauce.secret`, and name your secret ingredient in it. Do a `git status`. What does git think about your new file?

12. **Learner B**: Create a `.gitignore` file, and add a line saying `*.secret` to it. Do `git status` again. What has changed?

13. **Learner B**: Tell git that you want it to include the `.gitignore` file: `git add .gitignore`. Then commit and push your changes.

14. **Learner A and C**: Get the changes that Learner B just made: `git pull`. List all files (includen hidden ones) with `ls -a`. Did you receive the `.gitignore`? What about the `sauce.secret`? Which of those two files appear in the repo on GitHub? Also have a look at your `git log`.

Here is the [next tutorial](04_backtothepast).

-----------------

_Talking of spicy food, here is YouTube channel of [a Dutchman eating chili peppers while interviewing people](https://www.youtube.com/user/wunderhits)._