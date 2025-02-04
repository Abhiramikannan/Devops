#to check whether our current user is administrator or not?

# Step 1: Create a WindowsIdentity object that represents the current user's identity.
# This object provides information about the user and their security context.
try{
$CurrentUser = [Security.Principal.WindowsIdentity]::GetCurrent()

# Step 2: Create a WindowsPrincipal object based on the current user's identity.
# A WindowsPrincipal object allows you to check if the current user belongs to specific roles, such as Administrator.
$Principal = New-Object Security.Principal.WindowsPrincipal($CurrentUser)

# Step 3: Check if the current user is a member of the Administrators group
# The IsInRole method checks if the user is a member of a specific role.
# Here, we are checking if the current user is a member of the Administrator role.
$IsAdmin = $Principal.IsInRole([Security.Principal.WindowsBuiltInRole]::Administrator)

# Step 4: Display the result based on the value of $IsAdmin
if ($IsAdmin) {
    # If the user is an Administrator, display this message
    Write-Host "The current user is an Administrator."
} else {
    # If the user is NOT an Administrator, display this message
    Write-Host "The current user is NOT an Administrator."
}
}
catch{
    Write-Host "Error occurred: $_"
}