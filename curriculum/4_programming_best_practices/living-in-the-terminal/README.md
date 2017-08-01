# Living in command land, or:<br/>how I learned to stop worrying and love the terminal

## Where to start?
### Navigating online (stackoverflow) and offline (--help & the man pages).

Terminal land is vast and may appear nebulous to the unseasoned scripter. Where do we start? Let search engines light the way, and manual pages hold your hand.  

The UNIX operating system Adding "bash" or "in terminal" to search terms like "replace whitespaces" or "filesize" will point you in the right direction.

"My internet is down!"  
man pages are stored on your computer, so you can reference the documentation even when you are outside the internet!  

For example...  
Search: "replace whitespaces in filename in bash"  
Tip! The search engine DuckDuckGo returns StackOverflow answers as the first-hit-preview ;)  
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

In fact, the first rule of command line is "be careful what you wish for". The computer will do exactly what you say, but human's may have trouble speaking the computer's language. This can be dangerous when youre running commands like `rm` (remove), or `mv` (move, also used for renaming files). You can "echo" your commands to just print the command text without actually running the command. This can save your files and sometimes even your jorb! (Tip! Don't delete all your data with a misplaced `mv`)  


## Basic commands
`mv /source/path/$move_me /destination/path/$move_me`  
`rm $remove_me`  

### Caveats for git users
Moving files around on your computer can confuse git. If you are git-tracking a file, make sure to use the following alternatives so git knows what's going on.

`git mv /source/path/$move_me /destination/path/$move_me`  
`git rm $remove_me`  

### What's in my folder?
`ls`  
`ls -l`  
`tree`  
`tree -L 2`  
`tree -hs`  

### What's in my file?
`head -n10 $f`  
`tail -n10 $f`  
`tail -n10 $f | watch -n1`  
`tail -f -n10 $f`  

Counting words and lines (`wc` == "word count")...  
`wc $f`  

### Where is my file?
`find -name "<lost_file_name>" -type f`  
`find -name "<lost_dir_name>" -type d`  


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
# Rename the current window
Ctrl+b+,
# Kill the current pane
Ctrl+b+x
# Create a new pane
Ctrl+b+c
# Split windows horizontally into two
Ctrl+b+"
# Split windows vertically into two 
Ctrl+b+%
# Toggle between horizontal/vertical splits
Ctrl+b+space
```
Tmux can easily be configured by editing the tmux configuration file at ~/.tmux.conf

If you search "tmux cheatsheet" on (DuckDuckGo.com)[https://duckduckgo.com], the preview search result reveals some more useful commands [:

# VIM (Vi iMproved) - text editor 
Why bother?  
Vim is a powerful, lightweight, open-source, cross-platform text editor, that comes pre-installed on Unix systems. Vi was written in 1976 by Bill Joy at Sun Microsystems, and has been improved in 1991 to Vim.

Vim was designed for maximum efficiency and minimum bandwidth when working on old modems. It does not require use of the mouse or arrow keys. Much of learning Vim is just habit and muscle memory, in the first place this can be frustrating, but soon becomes second nature. 

But I'm scared?  
Don't worry here are some useful hints, tips, and tricks for using vim. 

Pleas note if at any point during this session you feel bewildered, nauseous, or perhaps euphoric, remain calm and press the `Esc` key to get back to normal.

Where should I start?  
A comprehensive although slightly dry start point for learning vim is through the `vimtutor` document available as standard with vim (just type `vimtutor` and hit Enter).

A more fun way to get used to moving in vim is playing this fun maze game.
https://vim-adventures.com/

A useful cheatsheet:
https://vim.rtorr.com/

The essentials:

Vim has three modes:
    1. Normal: this is for normal movement through a file (press I for Insert, or V for visual)
    2. Insert: this is for editing files and adding text (press Esc to get back to Normal)
    3. Visual: this is for highlighting lines in files (press Esc to get back to Normal)

## Navigation:
 * Movement is through `h`, `j`, `k`, and `l`
 * go to the top of the file with `gg`
 * go to the end of the file with `G`
 * go to line ten `10G`
 * move forward 1 word `w`
 * move forward 10 words `10w`
 * move back 1 word `b`
 * move back 10 words `10b`
 * jump to the start of the line ``
 * jump to the end of the line `$`

##Editing:
 * delete a character `x`
 * delete a line `dd`
 * delete 10 lines `10dd`
 * change a word `cw`
 * undo a change `u`
 * redo a change `Ctrl+r'
 * go to the end of the file with `G`
 * go to line ten `10G`
 * move forward 1 word `w`
 * move forward 10 words `10w`
 * move back 1 word `b`
 * move back 10 words `10b`
 * jump to the start of the line ``
 * jump to the end of the line `$`
 * start editing on line below `o`
 * start editing at end of line `A`

## Highlighting (visual mode):
 * select a line `V`
 * select 8 lines `8V`
 * yank or copy `y`
 * paste `p`
 * search `/pattern`
     * see next search match `n`
     * see previous search match `N`

Okay enough, get me out of here:
 * quit a  file `:q` 
 * write changes to a file `:w` (normal humanoids call this saving a file)
 * no, really get me out of here, I don't care about saving `:q!` 

The stuff they don't teach:
 * `:%s/old/new/gc` substitute old pattern for new globally but check each (commonly humanoids refer to this as find and replace)
 * `:10,20s/old/new/g` substitute the old pattern for the new only between lines 10 and 20
 * select a column of text `Ctrl+V+j+j+j+j`
 * comment a column of text `Ctrl+V+j+j+j+j+#`
 * go to file explorer `:Ex`
 * open a file on my remote `vim scp://path/to/file/`
 * change your `~/.vimrc` 
     * `set nu` add numbering
     * `set hlsearch` highlight search results

If you are convinced and want to go one step further you can configure vim as an  IDE for python development here
  https://realpython.com/blog/python/vim-and-python-a-match-made-in-heaven/

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

NUM_JOBS=16
parallel -j=$NUM_JOBS --dry-run <script.sh>

Remove dry-run to actually run the script ;) dry-run shows you what will happen without actually running any code - it's a good way to double-check the expected behaviour of your script before.



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
