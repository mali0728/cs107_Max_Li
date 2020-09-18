#!/bin/bash
for file in $(find -type f); do
	count=$(cat $file | wc -l)
	echo "$file $count"
done
