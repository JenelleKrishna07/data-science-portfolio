# alternative.py
# This script handles string manipulation in two parts:
# Part 1: Alternating character casing
# Part 2: Alternating word casing

# === Part 1: Alternate character casing ===
user_input = input("Enter a string: ")

# Store result
alternating_chars = ""

# Loop through each character by index
for index, char in enumerate(user_input):
    if index % 2 == 0:
        alternating_chars += char.upper()
    else:
        alternating_chars += char.lower()

print("Output with alternating characters:")
print(alternating_chars)

# === Part 2: Alternate word casing ===
# Split the input into a list of words
words = user_input.split()

# Store modified words
alternating_words = []

# Loop through each word by index
for index, word in enumerate(words):
    if index % 2 == 0:
        alternating_words.append(word.lower())
    else:
        alternating_words.append(word.upper())

# Join the words back into a string
result_words = " ".join(alternating_words)

print("Output with alternating words:")
print(result_words)
