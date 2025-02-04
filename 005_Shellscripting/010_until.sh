#!/bin/sh
#Author: Abhirami Kannan
#purpose: Learning until
#usage: ./until.sh

echo -e "pls enter the ip address to ping\c"
read -r ip
until ping $ip
do
    echo "host in $ip is down"
    sleep 1 #make 1sec delay after printing the message
done
echo "host in $ip is up"