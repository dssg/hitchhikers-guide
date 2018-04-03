#!/bin/bash
set -e

# download the raw file, unzip and process
#
# raw files are fixed width and come with definition files.
# convert those definition files into in2csv format then
# run in2csv to save in csv format.

ZIPFILE=$1
FILE_NO_EXTENSION="${ZIPFILE%.zip}"
URL="http://www.doc.state.nc.us/offenders"

# download the file
wget -N \
     -P preprocessed/ \
     "$URL"/"$ZIPFILE"

# unzip
unzip -o \
      -d preprocessed/ \
      preprocessed/"$ZIPFILE"

# create schema file
echo 'column,start,length' > preprocessed/"$FILE_NO_EXTENSION"_schema.csv
sed -E 's/[ ]{2,}/,/g' preprocessed/"$FILE_NO_EXTENSION".des | \
grep -vE "^Name," | \
cut -d',' -f1,4-5 >> preprocessed/"$FILE_NO_EXTENSION"_schema.csv

# do the conversion 
in2csv -s preprocessed/"$FILE_NO_EXTENSION"_schema.csv \
       preprocessed/"$FILE_NO_EXTENSION".dat | \
tr -d '?' > preprocessed/"$FILE_NO_EXTENSION".csv

