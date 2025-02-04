#!/bin/bash
#Author: Abhirami Kannan
#purpose: 
#usage: ./regular_expression

numString="123456789"
if [[ $numString =~ ^1 ]]; then
    echo "$numString starts with 1"
else
    echo "It is not a number"
fi

