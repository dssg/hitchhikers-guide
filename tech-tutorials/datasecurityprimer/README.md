:title: Data Security 
:author: redshiftzero
:description: Keeping Data Safe 101 
:keywords: security, privacy
:css: superstyle.css 

----

Data Security Primer
====================

.. image:: images/gandalf.jpg

----

Why this is important
=====================

* We have a lot of sensitive information

* Much of it is private data about individuals

* Legal agreements in place with partners to keep data safe

----

Security 101
============

* No such thing as absolute security

  - Consider your home

  - Can a dedicated attacker break in to your home? 

  - Do you lock your door? 

* Goal: Reduce risk of disclosure

----

What We Care About
==================

* Confidentiality of project data

* Login credentials to the servers and databases (and places where these credentials are stored)

----

Common DSSG Challenges
======================

* Avoid: Committing database credentials, API keys, SSH keys, etc. to Github repos

* Maintain awareness: IPython notebooks with exploratory data analysis with confidential data in them (talk with your team about this)

----

Commit with Confidence!
=======================

* Use ``git add filename`` to stage files individually

* Before you commit, ``git diff --cached`` to verify what you have staged is what you expect

* If you have files that you want to make sure that you do not commit, add them to your `.gitignore`

----

Authentication
==============

* Use unique, strong passwords

* Use a password manager e.g. KeePass, LastPass, 1Password

* Use two factor authentication when available (e.g. on Github)

----

Database: Don't
===============

Don't commit the following:

.. code:: python

    from sqlalchemy import create_engine
    engine = create_engine('postgresql://dbpro:ayylmao@dssg.example.com:5432/mydatabase')

----

Database: Do
============

Store these credentials in a separate file ``dbcreds.py``:

.. code:: python

    host='dssg.example.com'
    user='dbpro'
    database='mydatabase'
    password='ayylmao'

Add this file to your `.gitignore` to ensure that you don't commit it (``https://help.github.com/articles/ignoring-files/``)

----

You can commit an example file to your repo ``dbcreds.example``:

.. code:: python

    host=''
    user=''
    database=''
    password=''

----

Database: Do
============

.. code:: python

    import dbcreds

    engine = sqlalchemy.create_engine(('postgresql://{conf.user}:'
    '{conf.password}@{conf.host}:5432/{conf.database}').format( 
    conf=dbcreds))

----

Database: Do
============

Commit an even simpler config file `dbcreds.py`:

.. code:: python

    config = {'sqlalchemy.url': 'postgres://dbpro:ayylmao@dssg.example.com/mydatabase'}

And then connect:

.. code:: python

    import sqlalchemy
    from dbcreds import config

    engine = sqlalchemy.engine_from_config(config)

----

Beyond Content
==============

* Consider whether your project partner would want the names of tables disclosed

* Example: ``https://github.com/dssg/police-eis/blob/master/example_police_dept.yaml``

----

Cleaning Repos
==============

* Search for passwords/data leaks in a folder: ``https://github.com/dssg/repo-scraper``

* Instead of ``git-filter-branch`` to remove secret things from your git repository: ``https://github.com/rtyley/bfg-repo-cleaner``

----

Mistakes Happen
===============

* Avoid cleaning by not putting sensitive data in your repos

----

Web Applications
================

If you end up creating a web application, be aware of security best practices: 

* OWASP Secure Coding Practices: ``https://www.owasp.org/images/0/08/OWASP_SCP_Quick_Reference_Guide_v2.pdf`` 

