#!/bin/bash
#Author: Abhirami Kannan
#purpose: Creating a variable
#usage: ./variable2.sh
var1=10
var2="hello"
myhostname=$(hostname)
date=`date`
#the following variable definitions are not allowed
1value=100
false@linux=false
echo "var1=$var1"
echo "var2=$var2"
echo "hostname=$myhostname"
echo "date=$date"
echo "1value=$1value"
echo "false@linux=$false@linux"

