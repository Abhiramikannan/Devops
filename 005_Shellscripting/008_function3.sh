#!/bin/bash
#Author: Abhirami Kannan
#purpose: Learning function with parameter
#usage: ./function3.sh

function sum {
    local total=$(( $1 + $2 ))
    echo $total
    
}
sum 6 9
result=$(sum 5 8)
echo $result
echo "the result is $result"