Function WriteLog
{
    param(
    [string]$LogFileName,
    [string]$LogContent
    )
    Add-Content $LogFileName -Value $(Get-Date -Format "yyyy-MM-dd HH:mm:ss")" "$LogContent
}
try
{
    # Load WinSCP .NET assembly
    Add-Type -Path "WinSCPnet.dll"

    $LogFileName = "C:\temp\sftp\log"

    # Setup session options
    $sessionOptions = New-Object WinSCP.SessionOptions -Property @{
        Protocol = [WinSCP.Protocol]::Sftp
        HostName = "example.com"
        UserName = "user"
        Password = "mypassword"
        SshPrivatekeyPath = "C:\temp\sftp\.ssh\id_rsa.ppk"
        SshHostKeyFingerprint = "ssh-rsa 2048 xxxxxxxxxxx...="
    }

    $session = New-Object WinSCP.Session

    try
    {
        # Connect
        $session.Open($sessionOptions)

        # Upload files with wildcard
        $transferOptions = New-Object WinSCP.TransferOptions
        $transferOptions.TransferMode = [WinSCP.TransferMode]::Binary

        $targetFiles = "c:\temp\sftp\wildcard*.csv"
        $remotePath = "/home/user/recv"

        $transferResult = $session.PutFiles($targetFiles, $remotePath, $False, $transferOptions)

        # Throw on any error
        $transferResult.Check()

        # Print results
        foreach ($transfer in $transferResult.Transfers)
        {
            WriteLog $LogFileName, "Upload of "$line" successed"
#            Write-Host "Upload of $($transfer.FileName) succeeded"
        }

        # Upload files in a list
        $lines = Get-Content "list.txt"
        foreach ($line in $lines)
        {
            WriteLog $LogFileName, $line
#            Write-Host "Upload $line ..."
            $session.PutFiles($line, $remotePath).Check()
        }


        # Download files when done file is exist
        $localPath = "C:\temp\sftp"

        $files = $session.EnumerateRemoteFiles($remotePath, "*.done", [WinSCP.EnumerationOptions]::None)
        foreach ($fileInfo in $files)
        {
            # Resolve actual file name by removing the .done extension
            $remoteFilePath = $fileInfo.FullName -replace ".done$", ""
            WriteLog $LogFileName, "Downloading "$remoteFilePath"..."
#            Write-Host "Downloading $remoteFilePath ..."
            # Download and delete
            $session.GetFiles([WinSCP.RemotePath]::EscapeFileMask($remoteFilePath), $localPath + "\*", $True).Check()
            # Delete ".done" file
            $session.RemoveFiles([WinSCP.RemotePath]::EscapeFileMask($fileInfo.FullName)).Check()
        }
    }
    finally
    {
        # Disconnect, clean up
        $session.Dispose()
    }

    exit 0
}
catch
{
    WriteLog($LogFileName, "Error: $($_.Exception.Message)")
#    Write-Host "Error: $($_.Exception.Message)"
    exit 1
}