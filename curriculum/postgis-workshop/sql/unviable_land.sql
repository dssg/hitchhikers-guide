-- All this code is taken from "Spatial Analysis with PostGIS", Leo Hsu and Regina Obe, PGCon2009
-- URL: https://www.pgcon.org/2009/schedule/events/174.en.html

-- Delete all land that gets in the way of our roads, water and water ways
DELETE FROM land
WHERE EXISTS (
SELECT h.gid FROM hydrology As h WHERE ST_Intersects(h.the_geom, land.the_geom)
);

DELETE FROM land
WHERE EXISTS (
SELECT r.gid FROM roads As r WHERE ST_Intersects(r.the_geom, land.the_geom)
);

-- Delete all land that is not close enough to a road or water way
DELETE FROM land
WHERE NOT EXISTS (
SELECT h.gid FROM hydrology As h WHERE ST_DWithin(h.the_geom,land.the_geom, 25000)
);

DELETE FROM land
WHERE NOT EXISTS (
SELECT r.gid FROM roads As r WHERE ST_DWithin(r.the_geom,land.the_geom, 3000)
);
