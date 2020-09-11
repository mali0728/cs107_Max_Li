#!/bin/bash
# coder: Yilan Wang, contributor: Max Li
read -p "Enter the file: " file
echo $file
git add $file
git status
read -p "Do you want to continue: " answer
if [ $answer = "Y" ]; then
	read -p "Type the commit message: " msg
	git commit -m "$msg"
	git status
	read -p "Do you wish to continue? " answer2
	if [ $answer2 = "Y" ]; then
		git push
	elif [ $answer2 = "N" ]; then
		exit 1
	else
		echo "answer in Y or N"
	fi
elif [ $answer = "N" ]; then
	exit 1
else
	echo "answer in Y or N"
fi
