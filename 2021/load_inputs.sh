#!bin/bash

session_id=your_session_id

for i in {1..25}
do  
  curl https://adventofcode.com/2021/day/$i/input --cookie "session=$session_id" --output src/main/resources/inputs/day$i.in
done
