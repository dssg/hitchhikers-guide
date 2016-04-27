# Installing DSSG pre-requirements on OS X

## Step 1. Install Homebrew

[Homebrew](http://brew.sh/) is a package manager for OS X that will make your life a lot easier...

To install, open Terminal.app and execute the following:

```bash
/usr/bin/ruby -e "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install)"
```

Now you can do:

```bash
brew install anything
```

Awesome!

## Step 2. Install tools

#### Minimum pre-requisites

1.  SSH - this comes already installed with OS X
2.  Git - this comes already installed with OS X
3.  R - `brew install r `
4.  Rstudio - `brew cask install rstudio`
5.  psql (PostgreSQL CLI) - `brew install postgresql`
6.  DBeaver - `brew tap caskroom/versions; brew cask install dbeaver-community`

### Other useful tools

Text editors:

*   Sublime Text - `brew cask install sublime-text`
*   Atom - `brew cask install atom`

**Note:** applications installed via `brew cask install` will be available in `~/Applications`

## Step 3. Install Python tools

For managing your python environments and packages, we recommend to use `conda`, but you can also use `virtualenv`and `pip`.

#### Option A - Install Anaconda (recommended for beginners)

#### Option B - Install miniconda

#### Option C - Install `pip` and `virtualenv`

# How to ask for help?

#### Check closed issues

#### Open an issue

#### Contact

