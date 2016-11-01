-- All this code is taken from "Spatial Analysis with PostGIS", Leo Hsu and Regina Obe, PGCon2009
-- URL: https://www.pgcon.org/2009/schedule/events/174.en.html

create schema if not exists tutorial;
alter database gis set search_path to tutorial, public;

-- land
create table if not exists land(pid varchar(10) primary key, land_name varchar(150), land_type varchar(150));
select addgeometrycolumn('land', 'the_geom', 26986, 'multipolygon', 2);
create index assets_land_idx_the_geom on land using gist(the_geom);

-- buildings
create table if not exists buildings(gid serial primary key, bldg_name varchar(150), bldg_type varchar(150));
select addgeometrycolumn('buildings', 'the_geom', 26986, 'multipolygon', 2);
create index assets_building_idx_the_geom on buildings using gist(the_geom);

-- residents
create table if not exists residents(resid serial primary key, pid varchar(10), income_level integer, num_adults integer, num_children_b12 integer, num_children_a12 integer);
alter table residents add constraint assets_residents_fk_land foreign key (pid) references land (pid) on update cascade on delete restrict;
create index assets_residents_fki_land on residents using btree(pid);

-- hydrology
create table if not exists hydrology(gid serial primary key, hyd_name varchar(150), hyd_type varchar(150));
select addgeometrycolumn('hydrology', 'the_geom', 26986, 'polygon', 2);
create index assets_hydrology_idx_the_geom on hydrology using gist(the_geom);

-- roads
create table if not exists roads(gid serial primary key, road_name varchar(150), road_type varchar(150), nstart integer, nend integer);
select addgeometrycolumn('roads', 'the_geom', 26986, 'linestring', 2);
create index assets_roads_idx_the_geom on roads using gist(the_geom);

-- insert some roads
insert into roads(road_name, road_type, the_geom, nstart, nend)
values
('main rd', 'major', st_geomfromtext('linestring (247917 899350, 253267
900217.7491572206, 255591 899424, 256791 897948,258359 897155, 259281
897782, 259281 899738, 259392 900715, 253599 901564)', 26986), 1,
1000),
('curvy st', 'minor',
st_geomfromtext(st_astext(st_curvetoline('circularstring(257270
897671,257224 897667,257178 897665,256695 897863,256489 898341)')),
26986), 1, 100),
('elephantine rd', 'major',
st_setsrid(st_translate(st_scale(st_geomfromtext('linestring(328 -8.5,
323.5 -28.4, 328.1 -36.4, 320.7 -54.6, 331 -61, 340 -74, 340 -98, 361
-103, 377 -99, 389.5 -98, 388.4 -89, 379 -88, 374 -68, 357 -46, 336
-49,333 -36.4, 358 -31, 356 -5.6, 354 -7.9)'), 200,100), 190000,
907000),26986), 1, 200000);

-- insert hydrology (rivers, lakes, etc)
insert into hydrology(hyd_name, hyd_type, the_geom)
values
('lake 1', 'lake', st_geomfromtext('polygon ((254100 899740, 252280 898880,
253080 898920, 254100 899740))', 26986)),
('elephantine youth', 'reservoir', st_geomfromtext('polygon ((260298 900275,
260969 897727, 264454 897995, 260298 900275))', 26986)),
('river 1', 'river', st_buffer(st_geomfromtext('linestring (254580 899820,
253950.4022864219 899009.0145298447, 254480 898680, 254842.99706756207
898301.1125329993, 254352.08176504684 898166.4503003974, 253960 898440,
253020 898380, 253160 898120)', 26986), 20) ),
('bigger river', 'river', st_buffer(st_geomfromtext('linestring (247752
897838, 250869.32813777245 901306, 251275 900439, 253895 900827, 256053
899424, 257898 898336, 258839 898521)', 26986), 15));

-- insert land
-- generates several geometries at random
insert into land(pid, land_type, land_name, the_geom)
with recursive
p(pkey, atype, the_geom) as
(
values (1, 'historical', st_multi(st_buffer(st_transform(st_geomfromtext('polygon((-70.93052 42.31830,-70.93053 42.31840,-70.93053 42.31841,-70.93054 42.31838,-70.93052 42.31830))',4326), 26986),100,1 ) ))
union all
select pkey + 1, 'historical', st_multi(st_translate(the_geom, (st_xmax(the_geom) - st_xmin(the_geom)), (st_ymax(the_geom) - st_ymin(the_geom))))
from p where pkey < 20
),
p2(pkey,atype,the_geom) as
(select lpad(cast(p.pkey + cast(random()*100000 as integer) as text),9, '0') , (array['1 family', 'condo', '2 family', '3 family','commercial', 'government', 'hospital', 'police station', 'college', 'park', 'elementary school', 'highschool', 'vacant land'])[cast(random()*12 as integer) + 1],
st_multi(st_buffer(st_translate(p.the_geom,x*i, 2*pi()*sin(i/y) + (st_ymax(the_geom) - st_ymin(the_geom))) ,0,  mod(i,p.pkey) ))
from p cross join (select max(cast(st_xmax(the_geom) - st_xmin(the_geom) as integer)) as
x from p ) as x cross join (select max(cast(st_ymax(the_geom) - st_ymin(the_geom) as integer)) as y from p) as y
cross join (select cast(2*n*sin(n*2/360.0) as integer) from generate_series(1,250) as n
where sin(n/360.0) <> 0) as i(i)
where mod(i, p.pkey) between 1 and 4
)
select pkey as pid, min(atype), min(atype) || pkey, max(the_geom)
from p2
where st_isvalid(the_geom)
group by pkey;
