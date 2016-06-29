While having a repo for yourself is nice for version control, how do you add to somebody else's work? There are some pretty neat ways of handling this, but right now, we'll go through one of the simplest.

# Commands you'll learn

In this tutorial you'll be using the following commands:
* `git pull`: Get changes from the repo's GitHub page (or another 'remote') into your local folder
* `git push`: Sync your commits back to your repo's GitHub page (or another 'remote')

# Adding to It

1. **Learner C**: Create a new repo called 'soup', and add Learner A and Learner B as collaborators.

2. **Learner C**: Add a file `ingredients.md`. Populate it with a short list of ingredients that would make a medieval witch scratch her head. Commit your list. Add a few more ingredients (or delete some!). Commit again. Push your commits with `git push origin master`.

3. **Learners A and B**: Get the necessary URL from Learner C, then clone Learner C's 'soup' repo (`git clone https://github.com/learnerc/soup.git`, where you need to substitute the correct URL), and go into the repo's folder: `cd soup/`

4. **Learners A and B**: Do `git log` to see what Learner C has been up to so far.

5. **Learner C**: Add another ingredient to your file, commit and push again.

6. **Learner A and B**: As Learner C has added more stuff, you need to update your local clone of their repository! To do this, call `git pull`. Check what just happened with `git log`. Do you see the new commit that Learner A only added to their repo _after_ you first cloned it?

7. **Learner A**: In the repo's folder, create a new file called `spices.md`. In that file, list some fantasmorgacically hot spices. Do a `git status`. What does have git to say about your new file so far?

8. **Learner A**: Do `git add spices.md` to tell git that it should prepare for a snapshot of your changes to that file. (Just like in the first tutorial.) Check `git status`.

9. **Learner A**: Do `git commit -m 'blablabla'` to create a new snapshot (commit) of the repo as you have it now, which includes your new file now! You should probably make the commit message more meaningful than 'blablabla'. Then, push your changes: `git push origin master`, to synchronize your local commits with your repo on GitHub (your 'remote').

10. **Learner B and C**: Pull the changes that Learner A made, and show Learner A that you now have the spice list. Also show Learner A your `git log`. Learner A's commit is there! _(Great success._)

Here is the [next tutorial](04_thesecretsauce.md).

-----------------

_Talking of spicy food, here is YouTube channel of [a Dutchman eating chili peppers while interviewing people](https://www.youtube.com/user/wunderhits)._
