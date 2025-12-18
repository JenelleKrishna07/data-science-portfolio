# Task: Age-based quiz using if-elif-else structure

# Get user input and convert to integer
age = int(input("Please enter your age: "))

# Output based on age value
if age > 100:
    print("Sorry, you're dead.")
elif age >= 65:
    print("Enjoy your retirement!")
elif age >= 40:
    print("You're over the hill.")
elif age == 21:
    print("Congrats on your 21st!")
elif age < 13:
    print("You qualify for the kiddie discount.")
else:
    print("Age is but a number.")
