#!/bin/bash
# coder: Yilan Wang, contributor: Max Li, DLS
#file_list=$(echo "$( ls )")
#for f in $file_list; do
for f in $( ls ); do
	if [ -x $f ]; then
		echo $f
	fi
done
