# Recursive Touch Command in PowerShell

I could not find any direct substitute for the UNIX `touch` command in Windows Powershell. Though there are different workarounds to do all of the different things that it does. To mark all the files inside a directory as modified, we can run the following command

```powershell
dir <folder> -R | foreach { $_.LastWriteTime = [System.DateTime]::Now }
```

Source: [Recursive Touch Command in Windows with PowerShell](https://medium.com/plusinfinite/recursive-touch-command-in-windows-with-powershell-d43c3fca6ff3)
