#!/bin/bash
#Author: Abhirami Kannan
#purpose: Learning for loop
#usage:./multiplication_while.sh

echo "pls enter the number" 
read -r num
echo "multiplication table of $num"
counter=1
while [ $counter -le 10 ]
do 
    mult=`expr $num \* $counter`
    echo "$num * $counter = $mult"
    counter=`expr $counter + 1`
    done
