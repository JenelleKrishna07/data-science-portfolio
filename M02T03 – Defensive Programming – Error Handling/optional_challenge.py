# optional_challenge.py
# This file contains examples of syntax, runtime, and logical errors.

# --- Syntax Error 1: Missing colon in if statement ---
# if True
#     print("This will fail")

# --- Syntax Error 2: Incorrect indentation ---
#  print("Indented wrong")

# --- Runtime Error: Division by zero ---
# x = 10
# y = 0
# z = x / y  # This will raise ZeroDivisionError

# --- Logical Error: Wrong discount formula ---
original_price = 200
discount = 15  # 15 percent

# Logical error: Subtracts 15 directly instead of calculating 15% of 200
final_price = original_price - discount  # Should be original_price - (original_price * discount / 100)

print(f"Final price after discount is: {final_price}")
