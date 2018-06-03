# Intro to SQL

You've already used databases. Excel spreadsheets are a simple example. But those databases have many problems, such as 

* size of data you can use is limited by RAM
* cannot handle complex data (there are databases to handle more complex data types, e.g. documents)
* difficult to use data from multiple tables/sheets
* no data integrity guarantees (you can accidentally put a letter in a numeric column and the entire column will become a character column)
* it's difficult for multiple people to use the spreadsheet at the same time. If one person updates sheet A and another person updates sheet B, integrating both updates gets ugly.


Things to cover:

* `select`
* `from`
* `limit` (Postgres)
* `where`
* `group by`
* `order by`
* joins
