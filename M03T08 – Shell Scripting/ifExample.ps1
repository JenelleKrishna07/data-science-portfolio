# ifExample.ps1
# Step 1: if statement to check for new_folder
if (Test-Path "new_folder") {
    New-Item -ItemType Directory -Path "if_folder" -Force | Out-Null
}

# Step 2: if-else to check for if_folder and create conditional folder
if (Test-Path "if_folder") {
    New-Item -ItemType Directory -Path "hyperionDev" -Force | Out-Null
} else {
    New-Item -ItemType Directory -Path "new-projects" -Force | Out-Null
}
