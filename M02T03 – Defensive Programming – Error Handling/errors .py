# Fixed and commented version of errors.py

# Syntax Error: Missing parentheses around print function
print("Welcome to the error program")
print("\n")  # Syntax Error fixed: Indentation removed and parentheses added

# Variables declaring the user's age
# Runtime Error: Used '==' instead of '=' for assignment
age_Str = "24"  # Fixed syntax and logic: removed " years old" and corrected assignment

# Runtime Error: Cannot concatenate int and str directly
age = int(age_Str)
print("I'm " + str(age) + " years old.")  # Fixed by converting int to str

# Runtime Error: Adding string and int without conversion
years_from_now = 3  # Fixed logic: changed from str to int
total_years = age + years_from_now

print("The total number of years: " + str(total_years))  # Fixed variable reference and casting

# Logic Error: variable 'total' was never defined
total_months = total_years * 12  # Fixed logic: replaced 'total' with 'total_years'
print("In 3 years and 6 months, I'll be " + str(total_months + 6) + " months old")  # Added 6 months
