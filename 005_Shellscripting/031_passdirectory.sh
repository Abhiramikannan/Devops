#!/bin/bash
#Author: Abhirami Kannan
#purpose:find size of directory

#!/bin/bash
# purpose: write a shell script to print fun and find the size of a directory

print(){
    local message="$1"
    echo "$message"
}

# Function to print the size of a directory
print_directory_size(){
    local dir="$1"
    local size=$(du -sh "$dir" 2>/dev/null | cut -f1)
    if [ -z "$size" ]; then
        echo "Directory not found or inaccessible"
    else
        echo "Size of directory '$dir': $size"
    fi
}

echo "enter the msg to be passed"
read -r message
print "$message"

echo "enter the directory to find its size"
read -r directory
print_directory_size "$directory"