#!/bin/bash

trap "exit" INT

arrayPY=($(ls *.py))

for var in "${arrayPY[@]}"; do
  echo " ---" $var
  pylint $var
  if [ "$1" = "run" ]; then
    echo 75 | python $var
  fi
done
