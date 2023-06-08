#Simple script for looking and finding certain values in CSV and then exporting the results. 
#Use at your own risk be mindful of what you are working on/in.
#Created by Christopher Yett


#Here set the values you want it to search for
$V1 = "PAN"
$V2 = "BSQ"
$V3 = "COMMS"
$V4 = "GITM"
$V5 = "LAB"


#This imports the CSV you want to help filter
$csv = Import-Csv .\testcsv.csv 
clear

#The actual filter/matches that will output a table and tell you how many machines or results you have
$check = $csv | Where-Object {($_.location -match $V1) -or ($_.location -match $V2)-or ($_.location -match $V3)-or ($_.location -match $V4)-or ($_.location -match $V5)} 
write-host "There are " $check.count "machines" 
$check | Format-Table -AutoSize

#Asks for input to check if you actually want to export the results and either exports the results or exits the script.
$q1 = read-host -Prompt "Do you want to export the results? (Y or N) "

 if($q1 -eq "Y" -or "y" -or "Yes" -or "yes")
 {
 $check | export-csv -Path C:\Users\Chris\Desktop\exporttest.csv -NoTypeInformation 
 }

 else
 {
 exit 
 }
