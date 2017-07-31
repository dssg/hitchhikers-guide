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

