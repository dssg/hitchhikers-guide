# CommandLine, Git, and GitHub Tutorial (DSSG 2018)

## Introduction

You are most likely comfortable interacting with a computer using point-and-click
interfaces, also known as **GUIs**, or *Graphical User Interfaces*. But there is
another way that came before and will always be: the **CLI**, or *Command Line Interface*.

The command line interface allows you to communicate with your computer more
directly than you can through a GUI, in a **REPL**, or *read-evaluate-print loop*
format: The user (you!) types a command, then presses the return key. The computer
reads the command, evaluates it, and *prints out* the output. This term comes from
the days when we had to use physical printers called "teleprinters" to interact with
computers.

The software you use to communicate with your computer is known as a **shell**,
because it acts as a "shell" from the underlying complexity of the operating system.
The most popular shell is known as [BASH, the Bourne Again Shell](https://www.gnu.org/software/bash/).
Bash is the default shell for most UNIX systems and Macs. You can also look into more exotic shells like
Xonsh, Zsh, plumbum, and fish. I personally like xonsh and zsh.

So, why use the command line instead of a GUI? There are several reasons:

1. In the shell you can easily handle data by chaining programs into a cohesive pipeline
to handle large amounts of data.

2. You can automate your workflow through scripting to save time and be more productive. A good
rule of thumb is if you do something twice -- script it!

3. Your work will be much more reproducible because there will be a
digital record of the steps you took to produce your results compared to
point and clicking in a program like Excel.

4. If you're working with remote machines, like supercomputers or
machines in the cloud, the CLI is often the only interface available.

5. The CLI is usually much faster -- once you get the hang out of it.

The learning objectives of this mini-tutorial are the following:

* Learn how to navigate a UNIX file system.
* Learn some basic shell commands.
* Learn how to use to use git and github.

*The commandline has always been and always will be.*

## Navigating the File System
Now we'll learn how to navigate though a UNIX file system and how to **create**,
**edit**, **rename** and **copy** files and directories within the system.

First, a little background: UNIX has a hierarchical (tree-structure)
directory organization known as the **file system**. In the file system our
data is organized into **files**, which are organized in **directories**.
The base of the directory is called the *root directory* and denoted by a `/`.
All user-available disk space is combined into a single directory under '/'.

Here is an example of the directory tree of a typical Linux system.

![Image source](FS-layout.png)


From this figure, we can see all directories are under the root directory (`/`).
The folders under the root directory contain information for the configuration and operation
of the operating system, so you shouldn't change these (unless you really know
what you are doing). The special folder `home` contains the files for all users. In this
example, we have the directories `rick`, `anna`, `emmy`, `bob`, which contain files
created by users rick, anna, emmy, and bob, respectively.

To navigate through the file system, or **change directories**, we use the `cd`
command. If you just type `cd`, without any arguements it will take you to your
home directory. To see where  you are within the file system, you use the `pwd`,
or **print working directory** command:

```
$ cd
$ pwd

/home/akumar

```

You can also check who is logged into the machine with the `whoami` command.

```
$ whoami

akumar
```

In my case, my home directory is located at `/home/akumar`, because as we saw above
using the `whoami` command, my username is `akumar`. Yours will be something different.



`/home/akumar/` is a **path**; in this case, the path leads to my home directory.
A path can also be a path to a file name, for example
`/home/akumar/Documents/justice_league_meetings_notes.txt`. Paths that start with `/`
are called **absolute paths**, because they begin at the root directory.
They're *absolute* because they start at the root (the beginning of the filesystem),
so they will always be the same *regardless of your current location*.

**Relative paths** start at your current location. So the relative path to the file
above *from my home directory* (`/home/akumar`) would be
`Documents/justice_leage_meetings_notes.txt`.  Note that `/` has two meanings:
To signify an absolute path (originating in the root directory), and to separate
directories and files in the path.

Let's assume that I (user `akumar`) have the following directory data:

 To **list** all the files and subdirectories in a given directory, we can
 type `ls`:
 ```
 $ ls

 data
 Documents
 ```
 Try the command in your terminal.

 We see that the contents of `akumar`'s home directory are two directories called
 `data` and `Documents`, as we'd expect. If we want to see the contents of one
 of these directories, we can use the same `ls` command, but specify the directory
 whose contents we'd like to see as an argument to the `ls` command.:
 ```
 $ ls Documents/DailyPlanet_Articles

 superman_saves_the_day.txt
 ```

 Note that this would have the same output as running:
 ```
 $ cd Documents/DailyPlanet_Articles
 $ ls

 superman_saves_the_day.txt
 ```
 where we moved into the `DailyPlanet_Articles` directory and ran the `ls`
 command from within the directory.

 Say we've navigated to the `DailyPlanet_Articles` directory, and now we want
 to navigate to the `data` directory. There are multiple ways to do this:
 We could use the absolute path: ` cd /home/akumar/data/` (remember, that will
 work from anywhere in the filesystem), or we could use a relative path.
 But how do we use a relative path when `data` is not in our current directory,
 and we have to go up the tree to reach our destination? We can use the
 shorthand `.`. One `.` means our current directory, and `..` means **move up one directory**
 relative to where we currently are in the filesystem:

 First, we would navigate to the `DailyPlant_Articles` directory:
 ```
 cd /home/akumar/Documents/DailyPlant_Articles
 ```
 Now let move up two directories into the data directory.

 ```
 cd ../../data

 ```
 So we move up one directory from `DailyPlanet_Articles` to `Documents`, then up
 one more directory to `/home/akumar`, then down one directory to `data`.

 > Note: When you start typing in the path the data directory, you can use `TAB` to
 > **auto-complete**. The TAB button is your friend on the command-line.

 If you ever get lost in the file system, remember that the command `cd` (without
 specifying another directory) will always drop you into your home directory.
 ```
 $ cd
 $ pwd

 /home/akumar
 ```

## Creating, Editing, Moving, Copying, and Deleting Files

 Now let's put the UNIX file system to work for us. Let's get started
 in our home directory:
 ```
 $ cp <source-file> <destination-file> #copy file
 $ mv <source-file> <destination-file> #move file
 $ rm <source-file> <destination-file> #remove a file
 $ find ~/ -name '*.txt' #find all text files in my home directory
 ```
 **Note: There is no Recycle Bin or Trash rm can be a weapon of mass
 destruction**


# Using Git

Git is a version control system that allows you to take snapshots of your
project so you can go back in time or safely add features without breaking
your code. This is much much better than taking turns working on software and
emailing versions to eachother. Git can be used for any project involving plain
text files, including code, books, papers, small datasets.

Git and GitHub are used for hosting, distributing, and collaborating on a project
with others. Through tools like GitHub issues, GitHub Pull Requests, and branches
you can manage large scale collaborations.

An example of an open-source project here at DSaPP is Triage or Aequitas.

## Guidelines to keep in mind for effective collaboration

 * You are a team, work as a team.
 * You are physically located with your teammate so actually work together.
 * Know what eachother is doing. Collaborate, code review (and learn), Pair Program
 * People come before process (most of the time).



 Say we are starting a new project called "where_not_to_eat". About the chicago
 food inspections. We are going to combine data from different years into a
 single CSV. First we are going to clone a project using `git`.



 Link to the project on github.

 ```
 $ git clone <add link to repo here>
 ```

 We are going to use the github flow for this project. First we want to configure our
 git profile.

 ```
 # See how your git config looks
 git config --list
 ```

 Set your workspace
 ```
 # Adding some if you dont have a user.name or user.email

 git config --global user.name "Rayid Ghani"
 git config --global user.email "rayid.ghani@dssg.io"
 git config --global color.ui "auto"
 git config --global core.editor 'vim'
 git config --global push.default current
 ```

 Different work flows:

 **Solo Style**
 ```
 mkdir my_working_directory
 cd my_working_directory
 git init
 touch some_file.py
 # hack
 # hack
 git add some_file.py
 git commit -m "Working with some awesome idea"
 # hack
 # more hack
 ```

 **GitHub Style**

 - Also know as the [[http://endoflineblog.com/gitflow-considered-harmful][/Anti-gitflow/]]

 - [[https://guides.github.com/introduction/flow/][Github Flow]] (explained with images and animation!)


 *Don't code anything if there isn't a need for it.*

 First create good issues. A good issue is

 - clear
 - defined output
 - actionable
 - should only take a few days at most
 - good: *fix this bug*, *add this method* (good to write in the imperative voice)
 - bad: *it doesn't work for me*, *finish the project*


Now do a `git pull` to fetch any changes in the remote repository and
merge into your repository.

```
$ git pull


```

Now create your own "branch" of the project where you can make changes
separate from the *master* branch. The *master* branch should always be
pristine.

```
$ git checkout -b <username>-branch
```
Alternativly, you can name branches with the issue number of the issue you are
working on (e.g., add_features_issue#44).

Now we do a little hacking where we are going to write a bash script that will
clean the header of a CSV file and concatenate all the files.

Then we are going to `push` our changes to the remote repo. And create a pull
request.

# Class Exercise

Download data via the commandline and clean it, concatenate files so it can be
read into a database.

First clone the project:

Then create your own branch:

```
$ git checkout -b <username>-branch

```

Link to download data: https://github.com/avishekrk/where_not_to_eat/archive/master.zip

Here is my solution:

``` shell
wget https://github.com/avishekrk/where_not_to_eat/archive/master.zip;
unzip master.zip;
rm -v master.zip
mv -v where_not_to_eat-master raw
cd ./raw/
pwd
find -name "* *" | while read f; do echo ${f}; new=$(echo $f | sed "s/ /_/g"); echo ${new}; mv -v "$f" $new; done
mkdir -v ./../staging
head -1 food_inspection_2018-01-01.csv| tr '[:upper:]' '[:lower:]' | sed -e "s/#//g" -e "s/ ,/,/g" -e "s/ /_/g" -e s"/^,//g" > header
cat header > all_inspections.csv
for f in food_inspection_2018-0*.csv; do echo ${f}; awk 'NR > 1 {print}' ${f} >> all_inspections.csv; done
mv -v all_inspections.csv ./../staging

```

After saving our script we can commit our changes on our branch:

```
git add clean.sh
git commit -m "Added script to clean and concatenate files
git push #push to our remote repository
```

Then you can create a Pull Request.
