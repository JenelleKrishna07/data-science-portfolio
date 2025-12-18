# Challenge 1: Calculate area of a triangle

import math

# Get side lengths from user
side1 = float(input("Enter side 1: "))
side2 = float(input("Enter side 2: "))
side3 = float(input("Enter side 3: "))

# Calculate semi-perimeter
s = (side1 + side2 + side3) / 2

# Calculate area using Heron's formula
area = math.sqrt(s * (s - side1) * (s - side2) * (s - side3))

# Print area
print("Area of the triangle is:", area)
