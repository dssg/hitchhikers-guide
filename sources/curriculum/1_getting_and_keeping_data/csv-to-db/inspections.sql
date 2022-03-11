SET ROLE training_write;

CREATE SCHEMA IF NOT EXISTS DSSG_schema;

DROP TABLE IF EXISTS DSSG_schema.inspections_table;

CREATE TABLE DSSG_schema.inspections_table (
        inspection_id DECIMAL,
        dba_name VARCHAR,
        aka_name VARCHAR,
        license_num DECIMAL,
        facility_type VARCHAR,
        risk VARCHAR,
        address VARCHAR,
        city VARCHAR,
        state VARCHAR,
        zip DECIMAL,
        inspection_date DATE,
        inspection_type VARCHAR,
        results VARCHAR,
        violations VARCHAR,
        latitude DECIMAL,
        longitude DECIMAL,
        location VARCHAR
);

\COPY DSSG_schema.inspections_table from 'inspections.csv' WITH CSV HEADER;
