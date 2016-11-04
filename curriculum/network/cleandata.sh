#!/bin/bash
#clean data of the gml file

keywords="graph node edge"

for key in $keywords
do
echo "key: $key"

sed -i "s/${key}/${key} \[/g" karate.gml
sed -i "/  \[/d" karate.gml

done
