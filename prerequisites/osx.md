# Installing DSSG pre-requisites on OS X

This guide will help you install all pre-requisites to be ready for the summer.



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



If that doesn't work, you need to add the following to your PATH:

```bash
export PATH=/usr/local/bin:/usr/local/sbin:$PATH
```

If you don't know how to do that, run this:

```bash
echo 'export PATH=/usr/local/bin:/usr/local/sbin:$PATH' >> ~/.profile
```

If still not working. [Ask for help](https://github.com/dssg/hitchhikers-guide/blob/master/prerequisites/osx.md#asking-for-help).



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

Anaconda includes Python, `conda` (a package and environment manager) and a bunch of [Python packages](https://docs.continuum.io/anaconda/pkg-docs). After installing Anaconda you'll have everything to get started, but it requires ~3GB of disk space.

*   [Installation guide](https://www.continuum.io/downloads#_macosx) (Use Anaconda with Python 2.7)
*   [Documentation](http://conda.pydata.org/docs/)


Once Anaconda is installed, run the following to install DSSG required Python packages:

```bash
curl https://raw.githubusercontent.com/dssg/hitchhikers-guide/master/prerequisites/requirements.txt -o dssg-requirements.txt
conda install --file dssg-requirements.txt
```

Note for advanced users: You can install anaconda using `brew`. Run `brew cask info anaconda` for details.

#### Option B - Install Miniconda

Miniconda is a light-weight version of Anaconda, it only includes Python and  `conda`, you can later install only the Python packages that you'll need.

*   [Installation guide](http://conda.pydata.org/docs/install/quick.html#os-x-miniconda-install) (Use Miniconda with Python 2.7)
*   [Documentation](http://conda.pydata.org/docs/)

Once Miniconda is installed, run the following to install DSSG required Python packages:

```bash
curl https://raw.githubusercontent.com/dssg/hitchhikers-guide/master/prerequisites/requirements.txt -o dssg-requirements.txt
conda install --file dssg-requirements.txt
```

Note for advanced users: You can install miniconda using `brew`. Run `brew cask info miniconda` for details.

#### Option C - Python manual installation + `pip ` + `virtualenv`

If you don't want to install Anaconda/Miniconda, you can install Python directly from homebrew and manage your packages with `pip` and virtual environments with `virtualenv`.

```bash
#To install Python 2 and pip
brew install python
#To install virtual env
pip install virtualenv
#To install dssg required python packages
curl https://raw.githubusercontent.com/dssg/hitchhikers-guide/master/prerequisites/requirements.txt -o dssg-requirements.txt
pip install -r dssg-requirements.txt
```

Nice guide to use [virtualenv](http://docs.python-guide.org/en/latest/starting/install/osx/).

*Note: The caveat of using `pip` directly instead of `conda`, is that `conda` will take care of external dependencies for you (some Python packages depend on non-Python packages to work). But you can install those with `brew`.*



# Asking for help

We just started this repo but we want the [issues section](https://github.com/dssg/hitchhikers-guide/issues) to be a knowledge base for common problems.

If you have any trouble installing anything check closed issues. If you don't find the answer, feel free to [open an issue](https://github.com/dssg/hitchhikers-guide/issues/new) and someone will help you.

*To open issues, you need to create a Github account (you'll need it for the summer anyway).*