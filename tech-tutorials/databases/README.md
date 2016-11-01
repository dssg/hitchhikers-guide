# Databases 101

## Background and Motivation

In the case of small data (you can load it all into memory), simple analysis (maps well to your statistical
package of 
choice), and no plans for you or anyone else to repeat your analysis (nor receive updated data), then keeping your data in text files, 
and using a scripting language like Python or R to work with it, is fine.

In the case that you have a large amount of diverse data (cannot all be loaded into memory) that may be updated, or if you want to share your data with others and let others easily reproduce your analysis, then use a DBMS (Database Management System). DBMS are 
important for storing, organizing, managing and analyzing data. They mitigate the scaling and complexity problem of increasing data
in volume and diversity. DBMS facilitate a *data model* that allows data to be stored, queried, and updated efficiently and concurrently
by multiple users. In general, as a data scientist your toolkit will involve using SQL (Structured Query Language) with a database and
something else--python, R, SAS, Stata, SPSS. This tutorial covers the basics of relational databases and NoSQL databases, the pros and cons 
of each type of database, and when to use which one.

