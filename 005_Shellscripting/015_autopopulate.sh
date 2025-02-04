#!/bin/bash
#Author: Abhirami Kannan
#purpose: to know running of auto populates
#usage: ./autopopulate.sh

echo "all arguments concat together $*"
echo "number of arguments  $#"
echo "first parameter $1"
echo "expands all the command line as seperate words $@"
echo "process id of current process $$"

sleep 400 &
echo "processid of recently background process $!" 
echo "file name of current program $0"

