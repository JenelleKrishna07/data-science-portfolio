# while.py
# This program keeps asking the user for numbers until -1 is entered.
# It then calculates and prints the average of all valid numbers (excluding -1 and 0).

total = 0
count = 0

number = int(input("Enter a number (-1 to stop): "))

while number != -1:
    if number != 0:
        total += number
        count += 1
    number = int(input("Enter a number (-1 to stop): "))

if count > 0:
    average = total / count
    print(f"The average of the valid numbers entered is: {average}")
else:
    print("No valid numbers were entered.")
