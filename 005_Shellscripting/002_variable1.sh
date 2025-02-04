#!/bin/bash
#Author: Abhirami Kannan
#purpose: Creating a variable
#usage: ./variable1.sh
var1=10
var2="hello"
echo "Today is $var1 day and $var2 from me today."
echo 'Is it time to have lunch after' $var1 'pm?'
echo "Is it time to have lunch after `date`?"
echo 'Is it time to have lunch after $var1 pm?'
