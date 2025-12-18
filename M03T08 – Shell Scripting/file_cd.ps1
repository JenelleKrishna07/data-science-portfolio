# file_cd.ps1
# Step 1: Create three top-level folders
New-Item -ItemType Directory -Path "FolderA" -Force | Out-Null
New-Item -ItemType Directory -Path "FolderB" -Force | Out-Null
New-Item -ItemType Directory -Path "FolderC" -Force | Out-Null

# Step 2: Navigate into one folder (FolderA)
Set-Location -Path "./FolderA"

# Step 3: Create three subfolders
New-Item -ItemType Directory -Path "Sub1" -Force | Out-Null
New-Item -ItemType Directory -Path "Sub2" -Force | Out-Null
New-Item -ItemType Directory -Path "Sub3" -Force | Out-Null

# Step 4: Remove two of the subfolders
Remove-Item -Recurse -Force "./Sub1"
Remove-Item -Recurse -Force "./Sub2"
