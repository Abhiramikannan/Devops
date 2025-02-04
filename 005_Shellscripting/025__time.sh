#!/bin/bash
#Author: Abhirami Kannan
#purpose: printing the goodmorning,goodafternoon,goodevening,goodnight messageges
#usage: ./time.sh

time1=$(date +%H)
if [ $time1 -lt 12 ]
then
    echo "Good Morning"
elif [ $time1 -lt 16 ]
then
    echo "Good Afternoon"
elif [ $time1 -lt 20 ]
then
    echo "Good Evening"
else
    echo "Good Night"
fi
