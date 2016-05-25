# Software Setup

## Motivation
Not everybody will have installed all the necessary packages.

## Potential Teachouts
OK, this one really might not have any. Windows?

## Content
Make sure everyone can run Python, connect to database, and SSH (keys are set up). Have everyone run a script on an IPython notebook with imports, if anything gives an error troubleshoot installation. Go to command line, run a psql script, does it work. 

### SSH Key Setup

Everybody should have already generated a SSH key pair. To do this, follow the instructions on [https://help.github.com/articles/generating-a-new-ssh-key-and-adding-it-to-the-ssh-agent/](GitHub), namely 'Generating a new SSH key' and 'Adding your SSH key to ssh-agent'.

The steps in 'Generating a new SSH key' create two new files (by default in `~/.ssh/`: One without a file extension (by default, it's called `id_rsa`), and one with the extension `.pub`. The latter one is your _pub_lic key, which you will share with your project server, so that it can recognize you; the former is your private key, which you must not share with anybody, as it will let you access your project server.

After having generated the key pair, you should set the correct file permissions for your _private_ key: SSH requires that only you, the owner, are able to read/write it, and will give you an error otherwise. You can set the right permissions with this command: `chmod 600 ~/.ssh/nameofyourprivatekey` (where you'll have substitute in the path/name of your private key that you chose during key generation).

## Cheat Sheet

## Further Resources

## Discussion Notes
