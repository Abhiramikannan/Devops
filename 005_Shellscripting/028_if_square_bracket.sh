#!/bin/bash
#Author: Abhirami Kannan
#purpose: Read the input
#usage: ./inputvariable.sh

file=$1
if [ -f "$file" ]; then
      echo "file access $file"
else  
     echo "file doesnt exist"
fi

file=$1
if [[ -f $file ]]; then
      echo "file access $file"
else  
     echo "file doesnt exist"
fi
