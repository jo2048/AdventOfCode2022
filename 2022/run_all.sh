#!bin/bash

for i in {1..25}; do 
    if test -f day$i.py; then
        echo $'\n'DAY$i$'\n'-----
        python day$i.py 
    fi
done
