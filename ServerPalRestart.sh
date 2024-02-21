#!/bin/sh

echo "Checking to see if Server is running or nah."

ServerCheck(){ top -b -n 1 | grep PalServ* ;}

ServerCheck

check=$? 

echo "$check"

case $check in

    0)

        echo "Server is running" 
        sleep 2
        ;;
    
    1)
        echo "Server is not running"
        sleep 2
        ;;

esac