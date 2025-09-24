function WINDOW {
    Get-Process | Where-Object { $_.MainWindowTitle } |
    Sort-Object MainWindowTitle |
    Select-Object MainWindowTitle
}

# Change this window title so it doesn't show up in the list
$Title = "SendKeys"
$host.UI.RawUI.WindowTitle = $Title

Clear-Host
Write-Host "Here are all windows in use" 
WINDOW | Out-Host
$WINWIN = Read-Host -Prompt "What window do you want to point to?"

do {
    Write-Host @"
================================================================================
Please Make a selection from below
================================================================================

1 - Input custom string
2 - Send stored string to specified window
3 - Pick new window
4 - Load secure credential (username/password)
5 - Send stored username
6 - Send stored password
7 - Send stored username + password
Q - Quit

**NOTE: If you choose 1, 5, 6, or 7, the most recent choice will overwrite the stored string**
"@

    $inputChoice = Read-Host -Prompt "Choice"

    switch ($inputChoice) {

        1 {
            $RKEYS = Read-Host -Prompt "Enter your custom string (not securely)"
            $RKEYS = $RKEYS.Replace('$','{$}').Replace('&','{&}').Replace(')','{)}')
        }

        2 {
            $wshell = New-Object -ComObject wscript.shell
            $wshell.AppActivate($WINWIN)
            Start-Sleep 1
            $wshell.SendKeys($RKEYS)
            $wshell.SendKeys('~')
        }

        3 {
            Write-Host "Here are all windows in use"
            WINDOW | Out-Host
            $WINWIN = Read-Host -Prompt "What window do you want to point to?"
        }

        4 {
            # Load secure credential from file
            $cred = Import-Clixml "$env:USERPROFILE\stig-creds.xml"
            Write-Host "Credential loaded successfully."
        }

        5 {
            if ($cred) {
                $RKEYS = $cred.UserName
                Write-Host "Username stored for sending."
            } else {
                Write-Host "No credential loaded. Choose option 4 first."
            }
        }

        6 {
            if ($cred) {
                $RKEYS = $cred.GetNetworkCredential().Password
                Write-Host "Password stored for sending."
            } else {
                Write-Host "No credential loaded. Choose option 4 first."
            }
        }

        7 {
            if ($cred) {
                $RKEYS = "$($cred.UserName) $($cred.GetNetworkCredential().Password)"
                Write-Host "Username + Password stored for sending."
            } else {
                Write-Host "No credential loaded. Choose option 4 first."
            }
        }
    }

} until ($inputChoice -eq "q")
