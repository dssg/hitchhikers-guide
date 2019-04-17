-- All this code is taken from "Spatial Analysis with PostGIS", Leo Hsu and Regina Obe, PGCon2009
-- URL: https://www.pgcon.org/2009/schedule/events/174.en.html


-- Insert buildings
INSERT INTO buildings(bldg_name, bldg_type, the_geom)
SELECT pid, land_type,
ST_Multi(ST_Buffer(ST_ConvexHull(ST_Collect(ST_PointOnSurface(the_geom),
ST_Centroid(ST_MinimumBoundingCircle(the_geom, 1 + mod(CAST(ST_Ymin(the_geom) As
integer),4))))), (ST_XMax(the_geom) - ST_XMin(the_geom))/(5 + random()*10),1))
FROM  land
WHERE land_type NOT IN('vacant land', 'government');

-- Insert residents
INSERT INTO residents(pid , income_level, num_adults, num_children_b12, num_children_a12 )
SELECT pid,
CASE WHEN ST_Area(the_geom)/max_res > 5000 THEN 20000 + random()*100000
WHEN ST_Area(the_geom)/max_res > 3000 THEN 10000 + random()*70000 ELSE random()*50000
END,
1 + CAST(random()*4 As integer), CAST(random()*12 As integer), CAST(random()*5 As
integer)
FROM (SELECT pid, the_geom, land_type, CASE land_type WHEN '3 family' THEN 3 WHEN '2
family' THEN 2 ELSE 1 END  As max_res
FROM land) As l CROSS JOIN generate_series(1,3) As n
WHERE land_type LIKE '%family' or land_type LIKE '%residential%'
AND n <= max_res ;
