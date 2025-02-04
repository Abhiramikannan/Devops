$desktopPath = [System.Environment]::GetFolderPath("Desktop")

if (Test-Path $desktopPath) {
    Write-Host "Desktop folder exists at: $desktopPath"
} else {
    Write-Host "Desktop folder does not exist."
}
