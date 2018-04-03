#!/bin/bash
set -e

# create directory to hold outputs
mkdir -p preprocessed

# download and process ncdoc data in parallel
parallel './ncdoc_des2csv.sh {}' ::: OFNT3AA1.zip APPT7AA1.zip APPT9BJ1.zip INMT4AA1.zip INMT4BB1.zip INMT4CA1.zip INMT9CF1.zip OFNT1BA1.zip OFNT3BB1.zip OFNT3CE1.zip OFNT3DE1.zip OFNT9BE1.zip
