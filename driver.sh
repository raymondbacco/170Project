#!/bin/bash
FILES=/home/jedi/170/170Project/phase_1_inputs/inputs/*
for f in $FILES
do
  chrlen=${#f}
  chrlen=$(($chrlen-3))
  SUBSTR=$(echo $f | cut -b 49-$chrlen)
  ./driver -f $SUBSTR
  
  echo $SUBSTR
done
