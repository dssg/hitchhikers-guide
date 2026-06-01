# Getting and Keeping Data

Data comes in many forms, from many sources:
- you may get a database dump or backup directly from a project partner
- you may get a load of excel files
- you may get a set of CSVs
- you may need to scrape data from the web (see [Basic Web Scraping](basic-web-scraping/README.md)).

Regardless of what you get, once you've got your hands on some data, you'll need to bring it into a consolidated [database](databases/README.md), and start formatting it in such a way that you can use it for analysis. [Command Line Tools](../setup/command-line-tools/README.md) will start to come in handy here. If your data is in a format that resembles `CSV` [these instructions will be helpful](csv-to-db/README.md).
You'll definitely want to keep track of the steps you took to go from raw data to model-ready data ([Reproducible ETL](reproducible_ETL/README.md)) so you can incorporate that as part of your larger pipeline.

Often DSSG  projects will involve sensitive data, so it's important to be aware of some basic principles of data security:
[Data Security Primer](../get_data/data-security-primer/README.md) as well.
