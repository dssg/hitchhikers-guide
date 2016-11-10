DROP TABLE IF EXISTS jwalsh_schema.jwalsh_table;

CREATE TABLE jwalsh_schema.jwalsh_table (
    station VARCHAR(11) NOT NULL, 
    date DATE NOT NULL, 
    value_type VARCHAR(4) NOT NULL, 
    value INTEGER NOT NULL, 
    measurement_flag VARCHAR(4), 
    quality_flag VARCHAR(4), 
    source_flag VARCHAR(1) NOT NULL, 
    time VARCHAR(4)
);

\COPY jwalsh_schema.jwalsh_table from '/mnt/data/training/jwalsh/2016.csv' CSV;
