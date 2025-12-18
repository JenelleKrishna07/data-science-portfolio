# logic.py
# This program calculates a discount but has a logical error.

price = 100
discount_percent = 20

# Logical Error: subtracts discount_percent directly instead of converting to percentage
final_price = price - discount_percent  # Logical error: should use price * discount_percent / 100

print(f"The final price after discount is: {final_price}")
