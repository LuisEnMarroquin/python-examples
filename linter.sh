arrayPY=($(ls *.py))

for var in "${arrayPY[@]}"; do
  echo " ---" $var
  pylint $var
done
