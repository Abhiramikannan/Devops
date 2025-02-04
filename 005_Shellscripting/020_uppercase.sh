#!/bin/bash
#Write a script to convert a string to uppercase.

echo "enter the string "
read -r str
echo $str | tr 'a-z' 'A-Z'
