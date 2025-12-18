# Task 2: Manipulate a user-entered string

# Get user input
str_manip = input("Enter a sentence: ")

# Print length of the sentence
print("Length of input:", len(str_manip))

# Get the last letter
last_letter = str_manip[-1]

# Replace every occurrence of last_letter with '@'
replaced = str_manip.replace(last_letter, "@")
print("After replacement:", replaced)

# Print the last 3 characters in reverse
print("Last 3 characters in reverse:", str_manip[-3:][::-1])

# Create a five-letter word from the first 3 and last 2 characters
new_word = str_manip[:3] + str_manip[-2:]
print("Five-letter word:", new_word)
