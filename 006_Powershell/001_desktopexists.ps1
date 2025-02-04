try {
    # Get the path to the Desktop folder
    $Path = [Environment]::GetFolderPath("Desktop")
    
    # Print the path to the console
    echo $Path

    # Check if the path exists and is a directory
    if (Test-Path $Path -PathType Container) {
        # Print a message indicating the desktop folder exists
        "desktop folder exists"
        
        # List all files in the Desktop folder
        Get-ChildItem -path $Path -file
    }
    else {
        # Print a message indicating the folder doesn't exist
        "folder doesn't exist"
    }
}
catch {
    # Print an error message with the line number and error details
    "error in line number $($_.InvocationInfo.ScriptLineNumber) : $($Error[0])"
}