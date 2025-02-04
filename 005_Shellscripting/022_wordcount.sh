#!/bin/bash
#Write a script to count the number of words in a given string.

echo "enter the string"
read -r str
echo $str | wc -w