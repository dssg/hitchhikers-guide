# Command Line Tools

## Motivation

As data scientists, we often receive data in text-based files. We need
to explore these files to understand what they contain, we need to
manipulate and clean them and we need to handle them on our file
system. The most robust way to do this, even with large files, is the
command line.

Command line tools are the data scientist's swiss army knife. They are
versitile, portable, and have plenty of functions that you may not quite
sure how to use, but you're sure they'll be useful at some point. From
helping you obtain, clean, and explore your data, to helping you build
models and manager your workflow, command line tools are essential to
every well-built data science pipeline, will be used throughout DSSG,
and should be your starting point as you build your data science
toolkit.


## Slides

Here's the
[presentation](./intro-to-command-line-tools.pdf) from a previous workshop.

## The basics

### Where am I?
`pwd` print working directory - this prints the name of the current working directory  
`cd ..` changes directory to one level/folder up  
`cd ~/` goes to the home directory  
`cd -` return to the previous directory

### What's in my folder?
`ls` lists the contents in your current dictory.  
`ls -l` "long listing" format (`-l`) shows the filesize, date of last change, and file permissions  
`ls -la` "long listing" format (`-l`), shows all files (`-a`) including hidden dotfiles
`tree` lists the contents of the current directory and all sub-directories as a tree structure (great for peeking into folder structures!)  
`tree -L 2` limits the tree expansion to 2 levels  
`tree -hs` shows file sizes (`-s`) in human-readable format (`-h`)  

### What's in my file?  
`head -n10 $f` shows the "head" of the file, in this case the top 10 lines  
`tail -n10 $f` shows the "tail" of the file  
`tail -n10 $f | watch -n1` watches the tail of the file for any changes every second (`-n1`)  
`tail -f -n10 $f` follows (`-f`) the tail of the file every time it changes, useful if you are checking the log of a running program 
`less $f` paginated viewer for the contents of a text file 
`wc $f` counts words, lines and characters in a file  (separate counts using `-w` or `-l` or `-c`)

### Where is my file?
`find -name "<lost_file_name>" -type f` finds files by name  
`find -name "<lost_dir_name>" -type d` finds directories by name  

### Renaming files
Rename files with `rename`. For example, to replace all space bars with underscores:  
`rename 's/ /_/g' space\ bars\ .txt`  

This command substitutes (`s`) space bars (`/ /`) for underscores (`/_/`) in the entire file name (globally, `g`). (The 3 slashes can be replaced by any sequence of 3 characters, so `'s# #_#g'` would also work and can sometimes be more legible, for example when you need to escape a special character with a backslash.)  

You can replace multiple characters at a time by using a simple logical OR "regular expression" (`|`) such as [ |?] which will replace every space bar or question mark.    
`rename 's/[ |?]/_/g' space\ bars?.txt`

(The file will be renamed to `space_bars_.txt`)

Bonus points:  
`rename 'y/A-Z/a-z/'` renames files to all-lowercase  
`rename 'y/a-z/A-Z/'` renames files to all-uppercase  

## Some useful things to know
* Be careful what you wish for, the command line is very powerful, it will do exactly what you ask. This can be dangerous when you're running commands like `rm` (remove), or `mv` (move). You can "echo" your commands to just print the command text without actually running the command.  
* Use tab completion to type commands faster and find filenames, press the tab key whilst typing to see suggestions  `tab`
* Prepend `man` to a command to read the manual for example `man rm`
* You can use `ctrl + r` to search the command line history, and search for previously searched commands. Or type `history` to see the history.
* Beware of spaces when creating filenames, this is not generally good practice, if you must you can use the `\` escape character to add blank spaces in a file name. For example `touch space\ bars\ .txt`, if you run `touch space bars .txt` this will create three files `space`, `bars`, and `.txt`.
* Have a look into using `screen` or `tmux` for keeping processes alive and working with multiple terminals (see further reading [living-in-the-terminal](../../programming_best_practices/living-in-the-terminal/)).
* Use `htop` for monitoring the usage of your instance ([usage guide](https://www.deonsworld.co.za/2012/12/20/understanding-and-using-htop-monitor-system-resources/)).
* Have a go at learning the basics of `vim`, since it is ubiquitous on unix servers (see further reading [living-in-the-terminal](../../programming_best_practices/living-in-the-terminal/)).
* Check out some tutorials on regular expressions if you are not already familiar with them.

## Command Line for Data Science - Let's talk about the weather

As an exercise, let's take a shot at creating our own weather predictions using data from NOAA.

You can find daily data from 2016 for the US here:

    ftp://ftp.ncdc.noaa.gov/pub/data/ghcn/daily/by_year/2016.csv.gz

(The documentation is [here](http://www1.ncdc.noaa.gov/pub/data/cdo/documentation/GHCND_documentation.pdf))

### Getting Data from the Command Line

First we have to get the data. For that we're going to use curl.

    $ curl ftp://ftp.ncdc.noaa.gov/pub/data/ghcn/daily/by_year/2016.csv.gz

Whoa! Terminal is going crazy! This may impress your less savvy
friends, but it's not going to help you answer your question. We need
to stop this process. Try control-c. This is the universal escape
command in terminal.

We obviously didn't use curl right. Let's look up the manual for the command using `man`.

    $ man curl

Looks like if we want to write this to a file, we've got to pass the `-O` argument.

    $ curl -O ftp://ftp.ncdc.noaa.gov/pub/data/ghcn/daily/by_year/2016.csv.gz

Let's check to see if it worked.

    $ ls -lah

Great. Now we need to know the file format so we know what tool to use to unpack it.

    $ file 2016.csv.gz

Looks like it's a gzip so we'll have to use `gunzip`.

    $ gunzip 2016.csv.gz

    $ ls -lah

Now we've got a .csv file we can start playing with. Let's see how big it is using `wc`

## Viewing Data from the Command Line

The simpilest streaming command is `cat`. This dumps the whole file, line by line, into standard out and prints.

    $ cat 2016.csv

That's a bit much. Let's see if we can slow it down by viewing the file page by page using `more` or `less`.

    $ less 2016.csv

Great. But let's say I just want to see the top of the file to get a sense of it's structure. We can use `head` for that.

    $ head 2016.csv

    $ head -n 3 2016.csv

Similarly, if I'm only interested in viewing the end of the file, I can use `tail`.

    $ tail 2016.csv

These commands all print things out raw and bunched together. I want
to take advantage of the fact that I know this is a csv to get a
prettier view of the data. This is where `csvkit` starts to shine. The
first command we'll use from csvkit is `csvlook`.

    $ csvlook 2016.csv

But that's everything again. We just want to see the top. If only we could take the output from `head` and send it to `csvlook`.

We can! It's called *piping*, and you do it like this:

    head 2016.csv | csvlook

The output from `head` was sent to `csvlook` for processing. Piping
and redirection (more on that later) are two of the most important
concepts to keep in mind when using command line tools. Because most
commands use text as the interface, you can chain commands together to
create simple and powerful data processing pipelines!


## Filtering Data from the Command Line

It looks like in order for us to make sense of the weather dataset,
we're going to need to figure out what these station numbers
mean. Let's grab the station dictionary from NOAA and take a look at
it.

    $ curl -O https://www1.ncdc.noaa.gov/pub/data/ghcn/daily/ghcnd-stations.txt

    $ head ghcnd-stations.txt

Looks like the station description might come in handy. We want to look at just the stations in Chicago.

    $ grep CHICAGO ghcnd-stations.txt | csvlook -H

Let's pick OHARE as the station we'll use for now. Its ID is 'USW00094846'

Let's take a look at just the ID column from the weather file. We can do this using `cut`.

    $ cut -f 1 2016.csv

Looks like `cut` isn't smart enough to know that we're using a csv. We can either use csvcut, or pass a delimiter argument that specifies comma.

    $ cut -d , -f 1 2016.csv | head

Now let's filter out just the oberservations from OHARE.

    $ cut -d , -f 1 2016.csv | grep USW00094846 | head

Another powerful tool that can do filtering (and much more) is
`awk`. `awk` treats every file as a set of row-based records and
allows you to create contition/{action} pairs for the records in the
file. The default {action} in `awk` is to print the records that meet
the condition. Let's try reproducing the above statement using `awk`.

    $ cut -d , -f 1 2016.csv | awk '/USW00094846/' | head

`awk` requires familiarity with regular expressions for contitions and
has its own language for actions, so `man` and stack overflow will be
your friends if you want to go deep with `awk`.

## Editing and Transforming Data

Let's say we want to replace values in the files. PRCP is confusing. Let's change PRCP to RAIN.

To do this, we use `sed`. `sed` stands for streaming editor, and is
very useful for editing large text files because it doesn't have to
load all the data into memory to make changes. Here's how we can use
`sed` to replace a string.

    $ sed s/PRCP/RAIN/ 2016.csv | head

Notice the strings have changed!

But when we look at the source file

    $ head 2016.csv

Noting has changed. That's because we didn't write it to a file. In fact, none of the changes we've made have.

    $ sed s/PRCP/RAIN/ 2016.csv > 2016_clean.csv

    $ head 2016_clean.csv

We can also use awk for subsitution, but this time, let's replace
"WSFM" with "WINDSPEED" in all the weather files in the
directory. Once again, stackoverflow is your friend here.

    $ ls -la > files.txt

    $ awk '$9 ~/2016*/ {gsub(/WSFM/, "WINDSPEED"); print;}' files.txt

## Group Challenges

For group challenges, log onto the `training` ec2 instance and change
directories to /mnt/data/training/yourusername. This should be your
working directory for all the excercises.

1. Create a final weather file that just has weather data from OHARE
airport for days when it rained, and change PRCP to RAIN. Save the
sequence of commands to a shell script so it's replicable by your
teammate and push to a training repository you've created on github.

2. Create a separate file with just the weather from OHARE for days
when the tempurature was above 70 degrees F. (hint: try using csvgrep
to filter a specific column on a range of values)

3. Get ready to explore the relationship between weather and crime in
Chicago. Using crime data from 2016 (below), parse the json and
convert it to a csv. Explore the fields and cut the dataset down to
just day, location, and crime type. Then subset the dataset to just
homicides and save as a new file.

    https://data.cityofchicago.org/resource/6zsd-86xi.json

4. Using just command line tools, can you use the lat and long
   coordinates of the weather stations to rapidly identify which
   weather station is closest to the DSSG building?

## Cheat Sheet

We're going to cover a variety of command line tools that help us
obtain, parse, scrub, and explore your data. (The first few steps
toward being an
[OSEMN](http://www.dataists.com/2010/09/a-taxonomy-of-data-science/)
data scientist). Here's a list of commands and concepts we'll cover:

- Getting to know you: navigating files and directories in the command line
	- `cd`
	- `mkdir`
	- `ls`
	- `file`
	- `mv`
	- `cp`
	- `rm`
	- `findit` (bonus)

- Getting, unpacking, and parsing Data
	- `curl`
	- `wget` (bonus)
	- `gunzip`
	- `tar` (bonus)
	- `in2csv`
	- `json2csv` (bonus)

- Exploring Data
	- `wc`
	- `cat`
	- `less`
	- `head`
	- `tail`
	- `csvlook`

- Filtering, Slicing, and Transforming
	- `grep`
	- `cut`
	- `sed`
	- `awk`
	- `csvgrep`
	- `csvcut`
	- `csvjoin` (bonus)
	- `jq` (bonus; sed for JSON)

- Exploring & Summarizing
	- `csvstat`

- Writing shell scripts

## Further Resources

Jeroen Janssens wrote the book
[literally](http://datascienceatthecommandline.com/) on data science
in the command line. Also, check out his
[post](http://jeroenjanssens.com/2013/09/19/seven-command-line-tools-for-data-science.html)
on 7 essential command line tools for data scientists.

For command line basics, [Learning CLI the Hard
Way](http://cli.learncodethehardway.org/book/) is, as always, a great
resource.

## Potential Teachouts

- `tmux`: Getting your command line organized
	- `tmux` is a great way to manage many environments at once. Give it a shot!
