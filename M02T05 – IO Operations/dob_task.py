# dob_task.py
# Reads DOB.txt and prints names and birthdates in two separate blocks

# Open and read the file
with open("DOB.txt", "r") as file:
    lines = file.readlines()

# Initialize name and birthdate lists
names = []
birthdates = []

# Process each line
for line in lines:
    parts = line.strip().split()
    name = " ".join(parts[:2])
    birthdate = " ".join(parts[2:])
    names.append(name)
    birthdates.append(birthdate)

# Print names block
print("Name")
for name in names:
    print(name)

# Print birthdates block
print("\nBirthdate")
for birthdate in birthdates:
    print(birthdate)
