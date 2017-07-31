# Living in command land, or:<br/>how I learned to stop worrying and love the terminal

## Where to start?
Navigating online (stackoverflow) and offline (--help & the man pages).

## Basic commands
mv <move_me>
rm <remove_me>

### Caveats for git users
git mv
git rm

### What's in my folder?
ls
ls -l
tree
tree -L 2
tree -hs

### What's in my file?
head -n10 $f
tail -n10 $f
tail -n10 $f | watch -n1
tail -f -n10 $f

Counting words and lines (`wc` == "word count")...
wc $f

### Where is my file?
find -name "<lost_file_name>" -type f
find -name "<lost_dir_name>" -type d

## Functions
We can write functions in shell scripts as well!
The syntax looks like this...
function_name(args) {
    function_body
}

You can even define shell functions inside your ~/.bashrc profile when a simple alias just won't do...
For example, run a jupyter notebook remotely through an SSH tunnel and forward the connection to your localhost:
jupyter_local() { ssh -i ~/.ssh/<key>.pem -NfL "$1":localhost:"$2" <user>@<host>; }

Then we can just write...
jupyter_local 8888 8889
...to run a jupyter server on <host> (@ port 8888) and view it on our local machine (@port 8889)
