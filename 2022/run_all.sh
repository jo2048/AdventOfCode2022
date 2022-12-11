#!bin/bash

for i in {1..11}
do 
  echo $'\n'DAY$i$'\n'-----
  python day$i.py 
done
