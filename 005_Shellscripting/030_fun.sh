#!/bin/bash
# purpose: write a shell script to print fun

print(){
    local message="$1"
    echo "$message"
}

echo "enter the msg to be passed"
read -r message
print "$message"