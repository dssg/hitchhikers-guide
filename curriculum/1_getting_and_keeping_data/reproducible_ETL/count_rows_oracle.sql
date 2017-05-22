/* Run this code to create a table with the number of rows and columns in the
   Oracle origin database. You can export this table as a text file so we can
   ensure that everything transferred. */ 

CREATE TABLE tmp_overview_[database user] AS --replace with owner
  SELECT
    col.table_name,
    col.col_cnt AS column_count,
    rc.row_cnt  AS row_count
  FROM
    (
      /* number of columns */
      SELECT
        upper(table_name) table_name,
        COUNT(*)          col_cnt
      FROM dba_tab_columns
      WHERE owner = '[database user]' --replace with owner
      GROUP BY upper(table_name)
    ) col
    JOIN
    (
      /* number of rows */
      SELECT
        table_name,
        to_number(extractvalue(XMLType(sys.dbms_xmlgen.getxml('select count(*) c from  [database user].' --replace with owner
                                                              || table_name)), '/ROWSET/ROW/C')) AS row_cnt
      FROM dba_tables
      WHERE (iot_type != 'IOT_OVERFLOW'
             OR iot_type IS NULL)
            AND owner = ' [database user]' -- replace with owner
    ) rc
      ON upper(col.table_name) = upper(rc.table_name);