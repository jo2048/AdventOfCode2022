#!bin/bash

for i in $(seq -f "%02g" 0 25); do 
    if test -f day$i.py; then
        echo $'\n'DAY $i$'\n'-----
        python day$i.py 
    fi
done
