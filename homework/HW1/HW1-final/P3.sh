#!/bin/bash
grep -c [0-9] apollo13.txt > apollo_out.txt
grep --help | grep '\-\-count'
find -type f -name "*.py" | wc -l
find . -type f ! -perm -o=rw | wc -l
find . -maxdepth 1 ! -perm -o=rw | wc -l
