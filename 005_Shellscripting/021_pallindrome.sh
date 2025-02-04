#!/bin/bash
#Write a script to check if a string is a palindrome.



echo "Enter the string:"
read -r str

# Function to reverse the string
reverse_str() {
    local input=$1
    local length=${#input}
    local reversed=""
    for (( i=$length-1; i>=0; i-- )); do
        reversed="$reversed${input:$i:1}"
    done
    echo "$reversed"
}

# Get the reversed string
reversed_str=$(reverse_str "$str")

# Check if the original string is equal to the reversed string
if [[ "$str" == "$reversed_str" ]]; then
    echo "$str is a palindrome"
else
    echo "$str is not a palindrome"
fi