# finance_calculators.py
# Fixed and submission-ready version

import math

# Display options
print("Investment - to calculate the amount of interest you'll earn on your investment.")
print("Bond       - to calculate the amount you'll have to pay on a home loan.\n")

# Get user choice (fixed smart quotes)
user_choice = input("Enter either 'investment' or 'bond' from the menu above to proceed: ").lower()

# Handle investment option
if user_choice == "investment":
    try:
        deposit = float(input("Enter the amount of money you are depositing: "))
        interest_rate = float(input("Enter the interest rate (only the number, e.g., 8 for 8%): "))
        years = int(input("Enter the number of years you plan to invest: "))
        interest = input("Enter the type of interest (simple or compound): ").lower()
    except ValueError:
        print("Please enter valid numeric inputs.")
        exit()

    r = interest_rate / 100  # Convert to decimal

    if interest == "simple":
        total_amount = deposit * (1 + r * years)
        print(f"Total amount after {years} years with simple interest: {round(total_amount, 2)}")
    elif interest == "compound":
        total_amount = deposit * math.pow((1 + r), years)
        print(f"Total amount after {years} years with compound interest: {round(total_amount, 2)}")
    else:
        print("Invalid interest type selected. Please choose either 'simple' or 'compound'.")

# Handle bond option
elif user_choice == "bond":
    try:
        present_value = float(input("Enter the present value of the house: "))
        interest_rate = float(input("Enter the annual interest rate (e.g., 7): "))
        months = int(input("Enter the number of months you plan to repay the bond: "))
    except ValueError:
        print("Please enter valid numeric inputs.")
        exit()

    i = (interest_rate / 100) / 12  # Monthly interest rate
    repayment = (i * present_value) / (1 - (1 + i) ** (-months))
    print(f"Monthly repayment: {round(repayment, 2)}")

# Invalid input
else:
    print("Invalid entry. Please enter either 'investment' or 'bond'.")
