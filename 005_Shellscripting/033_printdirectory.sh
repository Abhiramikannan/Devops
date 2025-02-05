#!/bin/bash
# purpose: print the size of a directory

print_size(){
    local directory="$1"
    local size
    local du_out

    # Get the size of the directory using du
    size=$(du -sh "$directory" 2>/dev/null | cut -f1)
    if [ -z "$size" ]; then
        echo "Directory not found or inaccessible"
        return
    fi

    # Get the disk usage of the directory using du
    du_out=$(du -h "$directory" 2>/dev/null)

    echo "Size of directory: $size"
    echo "Disk usage:"
    echo "$du_out"
}

echo "Please enter directory path:"
read -r directory

print_size "$directory"