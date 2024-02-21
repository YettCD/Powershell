#!/bin/sh

echo  "Getting things going to start up PalServer and Check to make sure it is running"

ServerCheck(){ top -b -n 1 | grep PalServ* ;}

ServerCheck

check=$? 
echo "this is before the while: $check"

while [ "$check" = 1 ]
do
        ServerCheck 
        check=$?
        #echo "$check"

        echo "Server is running"
        
        sleep 2

done 
echo "Uh OH server is not running"
echo "Restarting Server"

bash ~/.steam/steam/steamapps/common/PalServer/PalServer.sh




