#!/bin/bash
#Author: Abhirami Kannan
#purpose:find size of directory

echo "enter the directory name"
read -r directory

# size=$(du -h "$directory")
# echo "the size of the directory is: $size"

du -h "$directory"