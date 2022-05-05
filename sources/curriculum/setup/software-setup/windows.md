
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

First, open a PowerShell or a Command Prompt Window as an Administrator. Then, type the following command in

```
wsl --install
```

This will install the default linux distribution (Ubuntu) on your machine. We'll assume that you are using this for the rest of the guide. 












