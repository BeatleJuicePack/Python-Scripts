#!/bin/bash
input="/Desktop/words2.txt"
while IFS= read -r line
do
  echo "$line"
done < "$input"
