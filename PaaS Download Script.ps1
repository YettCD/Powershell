## This is for prep and download of all the information from GD


#appaend the key for PaaS updates to the end of each line in a text file
Get-Content C:\Users\1154687340C\Desktop\GDdownloads.txt | foreach {$_ + "sp=r&st=2022-09-21T15:21:32Z&se=2022-10-31T23:21:32Z&spr=https&sv=2021-06-08&sr=c&sig=R5ojX4cqLVwB8Py%2FdTcmVUU6nO46JQCTwXQsDstc2iQ%3D"} | Out-File -FilePath C:\Users\1154687340C\Desktop\GDdownload.txt


#take text file and starts to open a chrome tab for each download 
Get-Content C:\Users\1154687340C\Desktop\GDdownload.txt | foreach {Start chrome $_}

