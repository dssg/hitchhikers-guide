# Living in command land, or:<br/>how I learned to stop worrying and love the terminal

## Where to start?
### Navigating online (stackoverflow) and offline (--help & the man pages).

Terminal land is vast and may appear nebulous to the unseasoned scripter. Where do we start? Let search engines light the way, and manual pages hold your hand.  

Adding "bash" or "in terminal" to search terms like "replace whitespaces" or "filesize" will point you in the right direction.

"My internet is down!"  
man pages are stored on your computer, so you can reference the documentation even when you are outside the internet!  

For example...  
Search: "replace whitespaces in filename in bash"  
Tip! The search engine [DuckDuckGo](https://duckduckgo.com/) returns StackOverflow answers as the first-hit-preview ;)  
```
find -name "* *" -type d | rename 's/ /_/g'
find -name "* *" -type f | rename 's/ /_/g'
```

So what else can we do with `rename`?  

```
$ man rename
> ...
       -n, -nono
               No action: print names of files to be renamed, but don't rename.
```
This is helpful when you're not too confident about what your command will do.  
... use `/<keyword>` to search for `<keyword>` in the manual.  

## Command Line 101
### Mind the command
The first rule of command line is "be careful what you wish for". The computer will do exactly what you say, but human's may have trouble speaking the computer's language. This can be dangerous when you're running commands like `rm` (remove), or `mv` (move, also used for renaming files). You can "echo" your commands to just print the command text without actually running the command. This can save your files and sometimes even your jorb! (Tip! Don't delete all your data with a misplaced `mv`)  

You can create dummy files to use for this tutorial sing the `touch` command, in case you don't want to operate on real files until you're comfortable with these commands. Let's start by creating a file with space bars in the name.  

`touch space\ bars\ .txt`

Note the use of the escape character `\` to signal that we intend to use the space bar as a character in our filename string. Without the backslashes, the command is interepreted as `touch` with several separate arguments, so in fact...  

`touch space bars .txt`  

...will create 3 files seperate files! `space`, `bars`, and `.txt`.

### Where am I?
`pwd` prints the name of the current working directory  
`cd ..` changes directory to one level/folder up  
`cd ~/` goes to the home directory  

### What's in my folder?
`ls` lists the contents in your current dictory.  
`ls -l` "long listing" format (`-l`) shows the filesize, date of last change, and file permissions  
`tree` lists the contents of the current directory and all sub-directories as a tree structure (great for peeking into folder structures!)  
`tree -L 2` limits the tree expansion to 2 levels  
`tree -hs` shows file sizes (`-s`) in human-readable format (`-h`)  

### What's in my file?  
`head -n10 $f` shows the "head" of the file, in this case the top 10 lines  
`tail -n10 $f` shows the "tail" of the file  
`tail -n10 $f | watch -n1` watches the tail of the file for any changes every second (`-n1`)  
`tail -f -n10 $f` follows (`-f`) the tail of the file every time it changes, useful if you are checking the log of a running program  
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

### Caveats for git users
Moving files around on your computer can confuse git. If you are git-tracking a file, make sure to use the following alternatives so git knows what's going on.

`git mv /source/path/$move_me /destination/path/$move_me`  
`git rm $remove_me`  

## Data structures
Variables are declared with a single "=" and no spaces.

`location="Lisbon"`  

Arrays are enclosed in brackets.  
`array=(abc 123 doremi)`  
If you echo the array, you will get the first element.  
```
$ echo $array
> abc
```
To echo the full array, expand the array with @:  
```
$ echo ${array[@]}
> abc 123 doremi
```

## Control flow and logic
Every bash statement is separated by a semicolon. This allows us to write one-liners that would normally be spread out over multiple lines.

So a for loop...  
```
for i in {a..z}; do
  echo $i;
done
```  
...can be written as a one-liner:  
```
for i in {a..z}; do echo $i; done
```


## Tricks
Brace expansion allows you to iterate over a range of possible variables.  
```
$ echo {0..9}
> 0 1 2 3 4 5 6 7 8 9
$ echo {0..9..2}
> 0 2 4 8
$ echo happy_birthday.{wav,mp3,flac}
> happy_birthday.wav happy_birthday.mp3 happy_birthday.flac
```

## Functions
We can write functions in shell scripts as well!
The syntax looks like this...
```
function_name(args) {
    function_body
}
```

You can even define shell functions inside your ~/.bashrc profile when a simple alias just won't do...
For example, run a jupyter notebook remotely through an SSH tunnel and forward the connection to your localhost:
`jupyter_local() { ssh -i ~/.ssh/<key>.pem -NfL "$1":localhost:"$2" <user>@<host>; }`

Then we can just write...
`jupyter_local 8888 8889`
...to run a jupyter server on `<host>` (@ port 8888) and view it on our local machine (@port 8889)


## Surfing the net
You can send HTTP requests to URLs from the command line.  

You can retrieve a page by sending a GET request:  
`curl -iX GET https://duckduckgo.com`

Or just the response header:
`curl -I https://duckduckgo.com`

From which you can parse out the status code, which is useful to see if the page is responding (200 OK) or non-existinent (404 File Not Found), etc.  
`curl -I https://duckduckgo.com 2>/dev/null | head -n 1 | cut -d$' ' -f2`
where...
`2>/dev/null` redirects the stderr to oblivion
`head -n 1` reads the top line only
`cut -d$' ' -f2` separates the line by the divider (spacebar) and takes the 2nd field (which is the numerical HTTP response status code).


## Working remotely via SSH
When working via SSH, a connection interruption can terminate your running scripts, lose your environment varaibles and lose your command history! D: There's a way to avoid this. Actually there's two: `screen` and `tmux` are two programs that allow you to run a terminal session remotely on a remote server which you can interact with from your own machine via SSH. So if you ever lose connection to the server, your terminal session is still running - you just have to log back into it. You can also run multiple independent terminal sessions on the same server this way.

### tmux<br/>(aka: terminal multiplexer)
```
# "Ping" the server to check if it's reachable (it "pongs" back... get it?)
ping <server>
# ssh into the server
ssh <user>@<server>
# Open a tmux session
tmux
# List existing sessions
tmux ls
# Attach (a) to a target session (-t #)
tmux a -t 1
# Create a new pane
Ctrl+b+c
# Rename the current pane
Ctrl+b+,
# Kill the current pane
Ctrl+b+x
```

If you search "tmux cheatsheet" on (DuckDuckGo.com)[https://duckduckgo.com], the preview search result reveals some more useful commands [:


## Bonus points
### Rogue terminals
We all make mistakes. Sometimes we make mistakes in infinite loops.
What do we do when "Ctrl+C" is not enough?
`top` or `htop` allow us to see what processes are running on our computer. (cf. System Monitor @ Mac)
Every process has an ID (`pid`) which we can use to send a `kill` command to it.

```
ps -ef | grep badprocess | awk '{print $2}' | kill `xargs $1`
```

Sometimes badprocess spawns other badprocess processes... so we can loop over them all.
```
ps -ef | grep badprocess | awk '{print $2}' | for f in `xargs $1`; do kill $f; done
```

### Parallel programming (sort of)
Run parallel processes on a multi-core system using GNU parallel. Typically, High-Performance Computing clusters have multi-cores (think quad-quad-quad-core), but running your script on the HPC is not enough to exploit it. What if you could run your script multiple times across each of the cores?

```
NUM_JOBS=16
parallel -j=$NUM_JOBS --dry-run <script.sh>
```

Remove `--dry-run` to actually run the script ;) dry-run shows you what will happen without actually running any code - it's a good way to double-check the expected behaviour of your script before.



### Custom prompts
You can customise your command prompt by changing the $PS1 variable.

### Motivational cow
If you need a little inspiration, let the `fortune` package brighten up your day! Even better, let an ASCII cow lighten up your day!

```
# Install the fortune and cowsay packages
sudo apt-get install cowsay fortune
# "Pipe" the output of fortune into the cowsay command
fortune | cowthink

 _______________________________
/ Don't Worry, Be Happy.        \
\                 -- Meher Baba /
 -------------------------------
        O   ^__^
         o  (oo)\_______
            (__)\       )\/\
                ||----w |
                ||     ||
```
