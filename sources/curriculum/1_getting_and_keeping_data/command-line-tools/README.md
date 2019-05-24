# Command Line Tools

## Motivation

As data scientists, we often receive data in text-based files. We need to explore these files to understand what they contain, we need to manipulate and clean them and we need to handle them on our file system. The most robust way to do this, even with large files, is the command line.

Command line tools are the data scientist's swiss army knife. They are versitile, portable, and have plenty of functions that your not quite sure how to use, but you're sure they'll be useful at some point. From helping you obtain, clean, and explore your data, to helping you build models and manager your workflow, command line tools are essential to every well-built data science pipeline, will be used throughout DSSG, and should be your starting point as you build your data science toolkit.


## Content

Here's the [presentation](https://docs.google.com/presentation/d/1twh7vH3EnB5fypn0tl1Fi0PhjlrMKExZoPhpu7-lWtk/edit?usp=sharing) from the start of the workshop.

### Let's talk about the weather

Since there's been so much controversy over weather predictions from paid vs free apps this year, we're going to just do it ourselves and create out own predictions using weather data from NOAA.

You can find daily data for the US here:

`ftp://ftp.ncdc.noaa.gov/pub/data/ghcn/daily/by_year/2016.csv.gz`

(The documentation is [here](http://www1.ncdc.noaa.gov/pub/data/cdo/documentation/GHCND_documentation.pdf))

### Getting Data from the Command Line

First we have to get the data. For that we're going to use curl.

`curl ftp://ftp.ncdc.noaa.gov/pub/data/ghcn/daily/by_year/2016.csv.gz`

Whoa! Terminal is going crazy! This may impress your less savvy friends, but it's not going to help you answer your question. We need to stop this process. Try control-c. This is the universal escape command in terminal.

We obviously didn't use curl right. Let's look up the manual for the command using `man`.

`man curl`

Looks like if we want to write this to a file, we've got to pass the `-O` argument.

`curl -O ftp://ftp.ncdc.noaa.gov/pub/data/ghcn/daily/by_year/2016.csv.gz`

Let's check to see if it worked.

`ls -la`

Great. Now we need to know the file format so we know what tool to use to unpack it.

`file 2016.csv.gz`

Looks like it's a gzip so we'll have to use `gunzip`.

`gunzip 2016.csv.gz`

`ls -la`

Now we've got a .csv file we can start playing with. Let's see how big it is using `wc`

### Viewing Data from the Command Line

The simpilest streaming command is `cat`. This dumps the whole file, line by line, into standard out and prints.

`cat 2016.csv`

That's a bit much. Let's see if we can slow it down by viewing the file page by page using `more` or `less`.

`less 2016.csv`

Great. But let's say I just want to see the top of the file to get a sense of it's structure. We can use `head` for that.

`head 2016.csv`

`head -n 3 2016.csv`

Similarly, if I'm only interested in viewing the end of the file, I can use `tail`.

`tail 2016.csv`

These commands all print things out raw and bunched together. I want to take advantage of the fact that I know this is a csv to get a prettier view of the data. This is where `csvkit` starts to shine. The first command we'll use from csvkit is `csvlook`.

`csvlook 2016.csv`

But that's everything again. We just want to see the top. If only we could take the output from `head` and send it to `csvlook`.

We can! It's called *piping*, and you do it like this:

`head 2016.csv | csvlook`

The output from `head` was sent to `csvlook` for processing. Piping and redirection (more on that later) are two of the most important concepts to keep in mind when using command line tools. Because most commands use text as the interface, you can chain commands together to create simple and powerful data processing pipelines!


### Filtering Data from the Command Line

It looks like in order for us to make sense of the weather dataset, we're going to need to figure out what these station numbers mean. Let's grab the station dictionary from NOAA and take a look at it.

`curl -O https://www1.ncdc.noaa.gov/pub/data/ghcn/daily/ghcnd-stations.txt`

`head ghcnd-stations.txt`

Looks like the sation description might come in handy. We want to look at just the stations in Chicago.

`grep CHICAGO ghcnd-stations.txt | csvlook -H`

Let's pick OHARE as the station we'll use for now. Its ID is 'USW00094846'

Let's take a look at just the ID column from the weather file. We can do this using `cut`.

`cut -f 1 2016.csv`

Looks like `cut` isn't smart enough to know that we're using a csv. We can either use csvcut, or pass a delimiter argument that specifies comma.

`cut -d , -f 1 2016.csv | head`

Now let's filter out just the oberservations from OHARE.

`cut -d , -f 1 2016.csv | grep USW00094846 | head`

Another powerful tool that can do filtering (and much more) is `awk`. `awk` treats every file as a set of row-based records and allows you to create contition/{action} pairs for the records in the file. The default {action} in `awk` is to print the records that meet the condition. Let's try reproducing the above statement using `awk`.

`cut -d , -f 1 2016.csv | awk '/USW00094846/' | head`

`awk` requires familiarity with regular expressions for contitions and has its own language for actions, so `man` and stack overflow will be your friends if you want to go deep with `awk`.

### Editing and Transforming Data
Let's say we want to replace values in the files. PRCP is confusing. Let's change PRCP to RAIN.

To do this, we use `sed`. `sed` stands for streaming editor, and is very useful for editing large text files because it doesn't have to load all the data into memory to make changes. Here's how we can use `sed` to replace a string.

`sed s/PRCP/RAIN/ 2016.csv | head`

Notice the strings have changed!

But when we look at the source file

`head 2016.csv`

Noting has changed. That's because we didn't write it to a file. In fact, none of the changes we've made have.

`sed s/PRCP/RAIN/ 2016.csv > 2016_clean.csv`

`head 2016_clean.csv`

We can also use awk for subsitution, but this time, let's replace "WSFM" with "WINDSPEED" in all the weather files in the directory. Once again, stackoverflow is your friend here.

`ls -la > files.txt`

`awk '$9 ~/2016*/ {gsub(/WSFM/, "WINDSPEED"); print;}' files.txt`

## Group Challenges

For group challenges, log onto the `training` ec2 instance and change directories to /mnt/data/training/yourusername. This should be your working directory for all the excercises.

1) Create a final weather file that just has weather data from OHARE airport for days when it rained, and change PRCP to RAIN. Save the sequence of commands to a shell script so it's replicable by your teammate and push to a training repository you've created on github.

2) Create a separate file with just the weather from OHARE for days when the tempurature was above 70 degrees F. (hint: try using csvgrep to filter a specific column on a range of values)

3) Get ready to explore the relationship between weather and crime in Chicago. Using crime data from 2016 (below), parse the json and convert it to a csv. Explore the fields and cut the dataset down to just day, location, and crime type. Then subset the dataset to just homicides and save as a new file.

`https://data.cityofchicago.org/resource/6zsd-86xi.json`

4) Using just command line tools, can you use the lat and long coordinates of the weather stations to rapidly identify which weather station is closest to the DSSG building?

## Cheat Sheet

We're going to cover a variety of command line tools that help us obtain, parse, scrub, and explore your data. (The first few steps toward being an [OSEMN](http://www.dataists.com/2010/09/a-taxonomy-of-data-science/) data scientist). Here's a list of commands and concepts we'll cover:

- Getting to know you: navigating files and directories in the command line
	- cd
	- mkdir
	- ls
	- file
	- mv
	- cp
	- rm
	- findit (bonus)

- Getting, unpacking, and parsing Data
	- curl
	- wget (bonus)
	- gunzip
	- tar (bonus)
	- in2csv
	- json2csv (bonus)

- Exploring Data
	- wc
	- cat
	- less
	- head
	- tail
	- csvlook

- Filtering, Slicing, and Transforming
	- grep
	- cut
	- sed
	- awk
	- csvgrep
	- csvcut
	- csvjoin (bonus)
	- jq (bonus; sed for JSON)

- Exploring & Summarizing
	- csvstat

- Writing shell scripts

## Further Resources

Jeroen Janssens wrote the book [literally](http://datascienceatthecommandline.com/) on data science in the command line. Also, check out his [post](http://jeroenjanssens.com/2013/09/19/seven-command-line-tools-for-data-science.html) on 7 essential command line tools for data scientists.

For command line basics, [Learning CLI the Hard Way](http://cli.learncodethehardway.org/book/) is, as always, a great resource.

## Potential Teachouts

- `tmux`: Getting your command line organized
	- `tmux` is a great way to manage many environments at once. Give it a shot!
