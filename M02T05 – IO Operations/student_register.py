# student_register.py
# Takes student registrations and writes each to a file with a signature line

# Ask how many students are registering
num_students = int(input("How many students are registering? "))

# Open file in write mode
with open("reg_form.txt", "w") as file:
    for _ in range(num_students):
        student_id = input("Enter student ID: ")
        file.write(student_id + "\n")
        file.write("---------\n")
