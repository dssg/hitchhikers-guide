# Introduction to the Unix Command Line

## Why Use the Command Line?

These days, most of us interact with our computers primarily through point-and-click GUIs, which provide a convenient and intuitive means of navigating your operating system and software. So, why use the command line instead of a GUI? There are several reasons:

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

### What We'll Cover Here

In this brief tutorial, we'll try to provide a very quick high-level introduction to working at the unix command line, focusing on:
- Navigating the unix file system
- Understanding the structure of unix commands and knowing where to look for help
- Using `screen` to run tasks in the background
- Checking on available resources

## Getting Started: Connect to the Server

Let's start by connecting to the compute server the same way we did yesterday:

```
ssh {your_andrew_id}@training.dssg.io
```

or, if you need to tell ssh where to find your private key:

```
ssh -i {/path/to/your/private_key} {your_andrew_id}@training.dssg.io
```

When you first connect to the server, you'll land in your home directory, `\home\{your_andrew_id}\`. Let's take a look around...

## Navigating the Unix File System

Whenever you're working at the unix command prompt, you always have a **working directory** that specifies the location in the file system that you're executing commands from. To see your current working directory, you can use the command `pwd` (that is, "print working directory" -- you'll find that most unix commands are short abbreviations to save on repeated keystrokes!):

```
dssgfellow@dssg-primary:~$ pwd
/home/dssgfellow
```

This prints out an **absolute path** to your current location in the system, which starts with a `/` character (which specifies the root directory of the system). The figure below gives an example of how a typical unix filesystem is organized:

![A typical unix filesystem](FS-layout.png)

From this figure, we can see all directories are under the root directory (`/`).
The folders under the root directory contain information for the configuration and operation of the operating system, so you shouldn't change these (unless you really know what you are doing). The special folder `home` contains the files for all users. In this example, we have the directories `rick`, `anna`, `emmy`, `bob`, which contain files created by users rick, anna, emmy, and bob, respectively.

As you get deep into the file system, specifying the full absolute path to a file you want to edit or run can become very tedious. Fortunately, unix also allows you to specify a **relative path** to a file, starting from your current working directory and **not** beginning with the leading `/`.

There are a few special paths that can be very helpful as you move around:
- `.` always refers to the current working directory
- `..` always refers to the *parent* of the current working directory
- `~` always refers to the home directory of the current user

With those basics in mind, we can start to explore.

For the fellowship, we've created a special directory on the server that's attached to a large disk to store data and modeling results. You can find it at `/mnt/data`. To move there, we'll use the `cd` ("change directory") command:

```
dssgfellow@dssg-primary:~$ cd /mnt/data
dssgfellow@dssg-primary:/mnt/data$ pwd
/mnt/data
```
Notice that two things happened: the last bit of our prompt changed from `~` to `/mnt/data` (helping us keep track of where we are) and the output of the `pwd` command has also changed to `/mnt/data`.

NOTE: to save space, from this point we won't show the full prompt, just the `$` -- lines starting with a `$` are commands to type and those without are outputs.

!!! info "TAB is your friend"

    One useful tip as you're working at the command line: many unix commands support tab-completion. For instance, you can usually type just the first few characters of the directory you're navigating to then hit "TAB" on your keyboard to have the system fill in the rest of the path!

Let's list the contents of this directory with `ls`:

```
$ ls
projects
```

Looks like there's another directory in here called `projects`. And to see what's in there, we can give `ls` a relative path:

```
$ ls projects/
acdhs-housing    dojo-mh           kcmo-mc        vibrant-routing
baltimore-roofs  food_inspections  pakistan-ihhn
```

Now we can see all the directories we've created for the projects this summer. Let's go into the one for the "food inspections" training project:

```
$ cd projects/food_inspections/
```

Now let's see what's in here with `ls` again:

```
$ ls
i_am_a_file.txt
```

You can copy that file to your home directory using the `cp` command (remembering the special path `~` means your home directory):

```
$ cp i_am_a_file.txt ~/
```

Let's do a little reorganization:
```
$ cd ~
$ mkdir a_new_directory
$ cd a_new_directory
```

What did we just do?
- We changed back to our home directory using `cd`
- Then we created a new directory with `mkdir`
- Next we changed into the new directory, again with `cd` and a relative path

Now suppose I want to move my copy of the test file into the new directory that I just created (and that I'm now working from). One way to do so would be specify the full path to the file, but a much easier option is to use the special relative paths of `..`, which means go up one directory, and `.`, which means the current directory:

```
$ mv ../i_am_a_file.txt ./
```

Now try `ls` and `pwd` from here -- what should you get?

Of course, we've done all this work moving this file around but haven't even looked at it's contents. To do so, we can use the very unintuitively-named command `cat` (actually meaning "concatenate"):

```
$ cat i_am_a_file.txt
Hello world!
```

Well, that's not very interesting -- doesn't seem like much of a reason to keep it around, so let's remove our copy of the file with `rm`:

```
$ rm i_am_a_file.txt
```

!!! danger

    Unix commands can be unforgiving in doing exactly what you ask for, even if that's not really what you want! For instance, `rm` will permanently delete your file immediately and without asking for confirmation, so exercise caution when using it. Many other unix commands can likewise delete or overwrite existing files without a warning or an error.

## Basics of Unix Commands

## Backgrounding Tasks with `screen`

## Checking on Available Resources

## Further Resources

If you want to dive a bit deeper into working at the command line (and learn a little about just how powerful it can be for munging data!), check out these additional guides:

- [This 2016 Tutorial](cmdline-2016.md) introduces several of the tools for getting and manipulating data at the command line, such as `curl`, `grep`, `cut`, `awk`, and `sed`

- [Living in the Terminal](../../programming_best_practices/living-in-the-terminal/) has some good details on best practices, shell scripting basics, and editing code directly in the terminal with `vim`
