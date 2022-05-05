
## Installing DSSG Prerequisites on Windows 10/11

We would do the following in this guide

1. Generate an SSH keypair
2. Install Git and setup a Github profile if you don't already have one
3. Install Python
4. Install pyenv + virtualenv to help manage different versions of Python and python packages on your machine
5. Install several necessary python packages
6. Install VSCode, a text editor that can help you edit code on your machine and on the server directly
7. Install DBeaver, a GUI based DB explorer
8. How to use command line tools on windows


In addition, we'll recommend a few other pieces of software that we recommend that you install, but not absolutely critical. 


### Windows Subsystem for Linux (WSL)

Before we get to the specific software installations, let's explore a feature from newer versions of windows have the option of running a linux environment directly on windows. You can [learn more about WSL here](https://docs.microsoft.com/en-us/windows/wsl/about).

Today we'll show you how to use command line tools on both Windows Power Shell, and on WSL.

First we have to install WSL on Windows. We'll give you the quick installation guide, if you want to customize things, please refer the [detailed installation guide](https://docs.microsoft.com/en-us/windows/wsl/install).

First, open a PowerShell or a Command Prompt Window as an Administrator. Next, we can see the available Linux distributions for install by using:

```
wsl --list --online
```

Then, you can install the version of Linux you would like to install. We recommend picking one of the Ubuntu distributions (because it's the most popular) and our guide will assume Ubuntu installation for WSL. 

We can install Ubuntu 20.04 by:

```
wsl --install -d Ubuntu-20.04
```

This will take a few minutes, and will prompt you to provide a UNIX username and a password. Please note that you might have to restart your computer at some point during the installation for things to take full effect. 

Now, you can use Linux from within your Windows machine. You should have a shortcut in your start menu to launch WSL, and when you launch it should open up a CLI. 

 Note that this will have no GUI and you'll have to rely on the CLI. If you need to access the file system of WSL through the Windows File Explorer, you can type the following in the address bar of the File Explorer. 

```
\\wsl.localhost\Ubuntu-20.04
```

This will take you to the root folder of the linux file system. 

_Note - Appending `\home\<username>` to the above command will take you to your home directory._

For the next few pieces of software, we'll provide you instructions on how to run things on both WSL and on 'pure' Windows. 



### SSH Keys

SSH helps you access the remote servers using your laptop. For this to work, we generate a key-pair that consists of a Public Key (something that you would share with the server admin), and a private key (something that you would NEVER share with anyone!).

**Option A - WSL**

Inside WSL, we can use the same process as a UNIX system to generate keys. 

```
ssh-keygen
```

This will prompt you to select a location for storing the key, and give you the option to add a passphrase to the key. If you want to use the default locaion (Recommended!) and not use a passphrase, you just have to hit return. 

Then, your keys will be stored in the place your specified. By default, 
- there'll be a `.ssh` folder in your home directory
- private key would be named `id_rsa`
- public key would be named `id_rsa.pub`

You've successfully generated the Keys!


**Option B - Windows**

Luckily, Windows 10/11 have OpenSSH already installed, and we don't need to use Putty anymore 🥳.

Just to make sure that it's installed, open up a Powershell window and enter `ssh`. When you hit return you should see an output like this. 

```
usage: ssh [-46AaCfGgKkMNnqsTtVvXxYy] [-B bind_interface]
           [-b bind_address] [-c cipher_spec] [-D [bind_address:]port]
           [-E log_file] [-e escape_char] [-F configfile] [-I pkcs11]
           [-i identity_file] [-J [user@]host[:port]] [-L address]
           [-l login_name] [-m mac_spec] [-O ctl_cmd] [-o option] [-p port]
           [-Q query_option] [-R address] [-S ctl_path] [-W host:port]
           [-w local_tun[:remote_tun]] destination [command]
```

If you do not see this output, you can [use this guide to install OpenSSH](https://docs.microsoft.com/en-us/windows-server/administration/openssh/openssh_install_firstuse). 


Once you have OpenSSH, you can use the same command as WSL to generate the Keys on a Powershell Window. As with WSL, you would be prompted to select the location to store the keys, and then the option to add a passphrase. You can just hit return to use the default location (recommended!) and not have a passphrase. 

By default, the keys will be stored in `C:\<windows_username>/.ssh/` and the file names would be as same as the WSL one. 


















