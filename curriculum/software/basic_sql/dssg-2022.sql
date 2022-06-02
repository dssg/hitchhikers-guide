








--  Intro to SQL
--  
--  Kasun / Adolfo / all of you! 



















select                             -- Operation: select, insert, update, delete 
*                                  -- columns (attributes)
from 
clean.food_facilities              -- Data source (a table in this case) 
limit 10;                          -- How many rows (observations)?
















-- That's a lot of attributes that (maybe)
-- we don't want to see, let's change that


select                         -- Operation: select, insert, update, delete
id, 
facility_name                  -- columns (attributes)
city,
municipal,
zip,
category_cd,
description,
p_code,
bus_st_date as open_since,     -- We can change the name of an attribute in the result
seat_count,
location                       -- This a geographical object
from 
clean.food_facilities              -- Data source (a table in this case) 
limit 10;                          -- How many rows (observations)?







-- You can filter the resulting table using predicates
-- e.g. just the 'Chain Restaurant without Liquor'

select                         -- Operation: select, insert, update, delete
id, 
facility_name                  -- columns (attributes)
city,
municipal,
zip,
category_cd,
description,
p_code,
bus_st_date as open_since,     -- We can change the name of an attribute in the result
seat_count,
location                       -- This a geographical object
from 
clean.food_facilities              -- Data source (a table in this case) 
where category_cd = 212
limit 10;                          -- How many rows (observations)?









-- You can check some fun facts from this table, you can apply 
-- functions to some columns (more on this later)

select 
count(*) as "number of facilities",
min(bus_st_date) as "earliest date on the data",
max(bus_st_date) as "last date on the data"
from 
clean.food_facilities;












-- Going back to predicates (the where clause)
-- Let's get a list of the newest restaurants 
select                         -- Operation: select, insert, update, delete
id, 
facility_name                  -- columns (attributes)
city,
municipal,
zip,
category_cd,
description,
p_code,
bus_st_date as open_since,     -- We can change the name of an attribute in the result
seat_count,
location                       -- This a geographical object
from 
clean.food_facilities              -- Data source (a table in this case) 
where 
bus_st_date >= '2022-01-01';









-- Ok, a long list... let's solve some questions 
-- Which categories do we have?

select 
distinct category_cd, description   -- unique combinations
from clean.food_facilities
order by category_cd asc;           -- order the resulting table ascending order






















-- How many facilities are in each category?
select
category_cd, description,
count(*) as "how many?"
from clean.food_facilities 
group by category_cd, description   -- Same columns!
order by "how many?" desc;















-- The group by is an *aggregation* operation, it takes 
-- many observations and "aggregates" them using an operation
-- like sum, count, stdev, avg, etc ...























-- Let's refine that to the top 5 categories


select
category_cd, description,
count(*) as "how many?"
from clean.food_facilities 
group by category_cd, description   -- Same columns!
order by "how many?" desc
limit 5;















-- Ok, but what if we want to have all the categories with
-- more than 1000 facilities?

select
category_cd, description,
count(*) as "how many?"
from clean.food_facilities 
group by category_cd, description   -- Same columns!
having count(*) >= 1000           
order by "how many?" desc;



















-- NOTE: having and where are different.
-- where filters the result *before* the aggegation
-- having filters the result *after* the aggregation



















-- Average number of seats per category

select 
category_cd, description,
count(*) as "number of facilities",
avg(seat_count) as average_seats,
sum(seat_count)as seat_capacity
from clean.food_facilities
group by category_cd, description 
order by average_seats desc;















-- Ugh awful, let's clean that


select 
category_cd, description,
count(*) as "number of facilities",
round(avg(seat_count),0) as average_seats,
round(sum(seat_count),0) as seat_capacity
from clean.food_facilities
group by category_cd, description 
order by seat_capacity desc nulls last
limit 10;












-- How about last year?


select 
category_cd, description,
count(*) as "number of facilities",
round(avg(seat_count),0) as average_seats,
round(sum(seat_count),0) as seat_capacity
from clean.food_facilities
where bus_st_date >= '2022-01-01'
group by category_cd, description 
order by seat_capacity desc nulls last
limit 10;








-- We have another two tables: inspections and violations detected on a 
-- particular inspection,

-- Let's find some basics from each table

select 
count(*) as "number of inspections",
count(distinct id) as "number of facilities",
min(bus_st_date) as "earliest date on the data",
max(bus_st_date) as "last date on the data"
from 
clean.inspections;


select 
count(*) as "number of violations",
count(distinct encounter) as "number of inspections",
count(distinct id) as "number of facilities",
min(bus_st_date) as "earliest date on the data",
max(bus_st_date) as "last date on the data"
from 
clean.violations;













-- Not all the restaurants have been inspected, 
-- Not all the inspections had violations




















-- It will be nice to have a unique table 
-- with all the inspections *and* their violations (if any)

-- All the inspections in a particular restaurant
select * 
from clean.inspections 
where id = 10 
order by inspect_dt asc;


















-- Which violations were detected in the inspection 201807090034?
select * from clean.inspections where encounter = 201807090034;

select * from clean.violations where encounter = 201807090034;














-- the way of "merge" this to tables is with the JOIN clause
-- We will use "LEFT JOIN" because we want ALL the inspections
-- even if they didn't find a violation 

-- Let's do a little test first, just check for the facility id 10

select 
 i.id, i.facility_name, i.category_cd, i.description, i.zip, i.municipal,
 i.encounter, i.placard_desc, i.inspect_dt,  i.ispt_purpose, i.purpose, 
 reispt_cd, reispt_dt, status,
 rating, low, medium, high, url
from 
 clean.inspections i
left join clean.violations v     -- Here we are "merging" both tables
using(encounter)                 -- using the column encounter
where i.id=10;










-- Let's use this "table" for further querying

with inspections as (
    select 
     i.id, i.facility_name, i.category_cd, i.description, i.zip, i.municipal,
     i.encounter, i.placard_desc, i.inspect_dt,  i.ispt_purpose, i.purpose, 
     reispt_cd, reispt_dt, status,
     rating, low, medium, high, url
    from 
     clean.inspections i
    left join clean.violations v 
    using(encounter)
    where i.id=10
)
select count(*) from inspections;

















-- this is a CTE ("Common Table Expressions"), we will use 
-- it for clarity 













with inspections as (
    select 
     i.id, i.facility_name, i.category_cd, i.description, i.zip, i.municipal,
     i.encounter, i.placard_desc, i.inspect_dt,  i.ispt_purpose, i.purpose, 
     reispt_cd, reispt_dt, status,
     rating, low, medium, high, url
    from 
     clean.inspections i
    left join clean.violations v 
    using(encounter)
)
select 
id, facility_name                                    -- all the columns from the CTE
, count(*)   as "num. of inspections"
, count(*) filter (where high = 'T') as "num. of high risk violations"
, count(*) filter (where medium = 'T') as "num. of medium risk violations"
, count(*) filter (where low = 'T') as "num. of low risk violations"
, count(*) filter (where high is null and medium is null and low is null) as "num. of inspections w/o violations"
from inspections
group by id, facility_name;











-- The end
-- Thanks!











