#!/bin/bash
#Author: Abhirami Kannan
#purpose: Learning for loop
#usage: ./for.sh
#fruit ->variable
#based on indexing
 
fruits=("apple" "banana" "cherry" "jackfruit") #array created here
for i in "${!fruits[@]}"; do
  	if [ $(expr $i % 2) -eq 0 ]; then     #condition for even
		echo "i like this fruit ${fruits[$i]}"
	else
		echo "i dont like this fruit ${fruits[$i]}"
        fi
done 

