#!/bin/bash
#Author: Abhirami Kannan
#purpose: 
#usage: ./marks.sh
#Any 3 marks is less than 30 then fail
#if above 30 cal avg > 80 distinct
#>60 first class

echo "enter the marks of 3 subjects"
read -r m1 m2 m3
if [[ $m1 -le 30  || $m2 -le 30 || $m3 -le 30 ]]; then
    echo "fail"

    else
     total=$(($m1+$m2+$m3))
     avg=$(($total/3))
     echo "avg is $avg"


    if [[ $avg -gt 80 ]]; then
        echo "distinct"
    elif [[ $avg -gt 60 ]]; then 
        echo "first class"
    else
        echo "pass"
    fi
fi