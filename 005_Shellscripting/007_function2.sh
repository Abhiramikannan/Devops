#!/bin/bash
#Author: Abhirami Kannan
#purpose: Learning function with parameter
#usage: ./function2.sh


function sum {
    local total=$(( $1 + $2 ))
    echo "The sum of $1 and $2 is $total"
}
sum 10 20 