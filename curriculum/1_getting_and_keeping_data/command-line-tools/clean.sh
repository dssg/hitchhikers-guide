cd raw
find -name "* *" | while read f; do echo ${f}; new=$(echo $f | sed "s/ /_/g"); echo ${new}; mv -v "$f" $new; done
mkdir -v ./../staging
head -1 food_inspection_2018-01-01.csv| tr '[:upper:]' '[:lower:]' | sed -e "s/#//g" -e "s/ ,/,/g" -e "s/ /_/g" -e s"/^,//g" > header
cat header > all_inspections.csv
for f in food_inspection_2018-0*.csv; do echo ${f}; awk 'NR > 1 {print}' ${f} >> all_inspections.csv; done
mv -v all_inspections.csv ./../staging
