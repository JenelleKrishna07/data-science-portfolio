# Challenge 2: Casting string to int

# Take user inputs
string_fav = input("Enter your favourite restaurant: ")
int_fav = int(input("Enter your favourite number: "))

# Print values
print("Favourite restaurant:", string_fav)
print("Favourite number:", int_fav)

# Attempt to cast string_fav to integer
# This will cause an error unless the string is numeric
# Uncomment the next line to see the error:
# print(int(string_fav))

# Explanation:
# You can't convert a non-numeric string to an integer.
# For example, int("Pizza Palace") will raise a ValueError.
