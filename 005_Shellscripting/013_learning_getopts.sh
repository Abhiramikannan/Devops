#!/bin/bash
#Author: Abhirami Kannan
#purpose: Learning gettopts
#usage: ./learning_getopts.sh
#read input variable from commant line and automatically  assign to a variable OPTARG
#instead of flag i can use any variable 

while getopts ":a:b:" flag; do
    case $flag in
        a) ab=$OPTARG;;  #first value assigned to this variable
        b) bc=$OPTARG;;   #second value assigned to this variable
        ?) echo "I dont understand ths values";;
    esac
done

echo "first value: $ab"
echo "second value: $bc"
