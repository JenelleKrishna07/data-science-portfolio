# Task: Triathlon award calculator

# Get user input for each event time and convert to integers
swimming_time = int(input("Enter swimming time (in minutes): "))
cycling_time = int(input("Enter cycling time (in minutes): "))
running_time = int(input("Enter running time (in minutes): "))

# Calculate total time
total_time = swimming_time + cycling_time + running_time

# Print total time
print(f"Total time taken for the triathlon: {total_time} minutes")

# Determine the award based on total time
if total_time <= 100:
    print("Award: Provincial colours")
elif total_time <= 105:
    print("Award: Provincial half colours")
elif total_time <= 110:
    print("Award: Provincial scroll")
else:
    print("Award: No award")
