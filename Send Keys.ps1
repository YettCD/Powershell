
## This function allows you to pull the Window Titles of all winodws on the PC 

function WINDOW {
get-process |Where{$_.MainWindowTitle} | sort MainWindowTitle |select MainWindowTitle}


#This is the old version would not work recently??
#Get-Process | Select MainWindowTitle,ProcessName,Id | where{$_.MainWindowTitle -ne ""}}

##This changes the title of the window/POwershell that is running this script to SendKeys so you can filter that from your results
$Title = "SendKeys"
$host.UI.RawUI.WindowTitle = $Title

##Clears screen and outputs the list of windows 
cls
Write-host "Here are all windows in use" | WINDOW | Out-Host
$WINWIN = read-host -Prompt "What window do you want to point to? "



do{
 


Write-Host @"
================================================================================
Please Make a selection from below
================================================================================

1 - Input Keys plaintext
2 - Send keys to specified window
3 - Pick New Window
Q  

**NOTE if you choice 1 and then 2 or vice versa it will be overwritten by the most recent choice and input***

"@

$input = Read-Host -Prompt "Choice: "

switch ($input){

1 {$RKEYS = Read-Host -Prompt "Enter your keys/String not securly: "
    $RKEYS = $RKEYS.Replace('$', '{$}').Replace('&','{&}').Replace(')','{)}') }

2 {$wshell = New-Object -ComObject wscript.shell;
$wshell.AppActivate($WINWIN)
Sleep 1
$wshell.SendKeys($RKEYS)
$wshell.SendKeys('~') }

3 {Write-host "Here are all windows in use" | WINDOW | Out-Host
$WINWIN = read-host -Prompt "What window do you want to point to? "
}

}


}until($input -eq "q")
