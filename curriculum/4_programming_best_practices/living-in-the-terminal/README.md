# Living in command land, or:<br/>how I learned to stop worrying and love the terminal

## Where to start?
Navigating online (stackoverflow) and offline (--help & the man pages).


Tip! The (DuckDuckGo.com)[https://duckduckgo.com] search engine returns StackOverflow answers as the first-hit-preview ;) 

## Basic commands
`mv /source/path/$move_me /destination/path/$move_me`  
`rm $remove_me`  

### Caveats for git users
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
```
 _______________________________
/ Don't Worry, Be Happy.        \
\                 -- Meher Baba /
 -------------------------------
        \   ^__^
         \  (oo)\_______
            (__)\       )\/\
                ||----w |
                ||     ||

