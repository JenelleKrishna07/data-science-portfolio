# task_manager.py
# Capstone Project - Task Manager
# Student: Jenelle Krishna

from datetime import datetime
import os

# ======== Helper Functions ========

def reg_user():
    """
    Allows the admin to register a new user if the username doesn't already exist.
    Saves new credentials to user.txt.
    """
    with open("user.txt", "r") as file:
        existing_users = [line.strip().split(',')[0] for line in file.readlines()]

    while True:
        new_username = input("Enter new username: ")
        if new_username in existing_users:
            print("Username already exists. Please try a different one.")
        else:
            break

    new_password = input("Enter new password: ")
    confirm_password = input("Confirm password: ")

    if new_password == confirm_password:
        with open("user.txt", "a") as file:
            file.write(f"{new_username}, {new_password}\n")
        print(f"User '{new_username}' registered successfully!")
    else:
        print("Passwords do not match. Registration failed.")

def add_task():
    """
    Prompts the user for task details and appends the task to tasks.txt.
    """
    assignee = input("Enter the username of the person the task is assigned to: ")

    # Optional: check if user exists
    with open("user.txt", "r") as file:
        valid_users = [line.strip().split(',')[0] for line in file.readlines()]
    if assignee not in valid_users:
        print("Error: This user does not exist.")
        return

    title = input("Enter the title of the task: ")
    description = input("Enter a description of the task: ")
    due_date = input("Enter the due date (e.g., 2025-06-30): ")
    date_assigned = datetime.today().strftime("%Y-%m-%d")
    completed = "No"

    task_line = f"{assignee}, {title}, {description}, {date_assigned}, {due_date}, {completed}\n"

    with open("tasks.txt", "a") as file:
        file.write(task_line)

    print("Task successfully added!")

def view_all():
    """
    Reads and displays all tasks from tasks.txt in a user-friendly format.
    """
    try:
        with open("tasks.txt", "r") as file:
            tasks = file.readlines()

        if not tasks:
            print("There are no tasks to display.")
            return

        for idx, line in enumerate(tasks, 1):
            parts = line.strip().split(", ")
            if len(parts) == 6:
                assignee, title, description, date_assigned, due_date, completed = parts
                print(f"\nTask {idx}:")
                print(f"Assigned to: {assignee}")
                print(f"Title: {title}")
                print(f"Date assigned: {date_assigned}")
                print(f"Due date: {due_date}")
                print(f"Completed: {completed}")
                print(f"Description: {description}")
                print("-" * 40)
            else:
                print(f"⚠️ Skipped malformed task entry: {line}")
    except FileNotFoundError:
        print("Error: tasks.txt not found.")

def get_valid_task_number(prompt, max_number):
    """
    Recursively prompts the user for a valid task number or -1 to cancel.
    Returns a valid task number or -1.
    """
    selection = input(prompt)
    if selection == "-1":
        return -1
    if selection.isdigit() and 1 <= int(selection) <= max_number:
        return int(selection)
    print("Invalid selection. Please try again.")
    return get_valid_task_number(prompt, max_number)

def view_mine(username):
    """
    Displays tasks assigned to the logged-in user with index numbers,
    and allows marking a task as complete or editing it (if incomplete).
    """
    try:
        with open("tasks.txt", "r") as file:
            tasks = file.readlines()

        user_tasks = []
        for idx, line in enumerate(tasks):
            parts = line.strip().split(", ")
            if parts[0] == username:
                user_tasks.append((idx, parts))

        if not user_tasks:
            print("You have no assigned tasks.")
            return

        print("\nYour Tasks:")
        for count, (task_index, task_data) in enumerate(user_tasks, 1):
            print(f"\nTask {count}:")
            print(f"Title: {task_data[1]}")
            print(f"Description: {task_data[2]}")
            print(f"Assigned: {task_data[3]}")
            print(f"Due Date: {task_data[4]}")
            print(f"Completed: {task_data[5]}")
            print("-" * 40)

        selection = get_valid_task_number("\nEnter the task number to edit/mark complete, or '-1' to return: ", len(user_tasks))
        selection = get_valid_task_number(
            "\nEnter the task number to edit/mark complete, or '-1' to return: ",
            len(user_tasks)
        )

        if selection == -1:
            return

        selected_task_index, task_data = user_tasks[selection - 1]
        
        action = input("Enter 'c' to mark as complete, or 'e' to edit the task: ").lower()

        if action == 'c':
            task_data[5] = "Yes"
            tasks[selected_task_index] = ", ".join(task_data) + "\n"
            with open("tasks.txt", "w") as file:
                file.writelines(tasks)
            print("Task marked as complete.")

        elif action == 'e':
            if task_data[5].lower() == "yes":
                print("You cannot edit a completed task.")
                return

            new_assignee = input("Enter new assignee (or press enter to keep current): ")
            new_due_date = input("Enter new due date (or press enter to keep current): ")

            if new_assignee:
                task_data[0] = new_assignee
            if new_due_date:
                task_data[4] = new_due_date

            tasks[selected_task_index] = ", ".join(task_data) + "\n"
            with open("tasks.txt", "w") as file:
                file.writelines(tasks)
            print("Task updated successfully.")
        else:
            print("Invalid action.")

    except FileNotFoundError:
        print("Error: tasks.txt not found.")

def view_completed():
    """
    Admin-only: View all completed tasks in a user-friendly format.
    """
    try:
        with open("tasks.txt", "r") as file:
            tasks = file.readlines()

        completed_tasks = [line for line in tasks if line.strip().endswith("Yes")]

        if not completed_tasks:
            print("No completed tasks found.")
            return

        print("\n=== Completed Tasks ===")
        for idx, line in enumerate(completed_tasks, 1):
            parts = line.strip().split(", ")
            if len(parts) == 6:
                assignee, title, description, date_assigned, due_date, completed = parts
                print(f"\nTask {idx}:")
                print(f"Assigned to: {assignee}")
                print(f"Title: {title}")
                print(f"Date assigned: {date_assigned}")
                print(f"Due date: {due_date}")
                print(f"Completed: {completed}")
                print(f"Description: {description}")
                print("-" * 40)
            else:
                print(f"⚠️ Skipped malformed task entry: {line}")
    except FileNotFoundError:
        print("Error: tasks.txt not found.")

def delete_task():
    """
    Admin-only: Deletes a task by its number from tasks.txt.
    """
    try:
        with open("tasks.txt", "r") as file:
            tasks = file.readlines()

        if not tasks:
            print("No tasks available to delete.")
            return

        print("\n=== All Tasks ===")
        for idx, line in enumerate(tasks, 1):
            print(f"\nTask {idx}: {line.strip()}")

        selection = input("\nEnter the task number to delete (or -1 to cancel): ")
        if selection == "-1":
            return

        if not selection.isdigit() or not (1 <= int(selection) <= len(tasks)):
            print("Invalid selection.")
            return

        deleted_task = tasks.pop(int(selection) - 1)

        with open("tasks.txt", "w") as file:
            file.writelines(tasks)

        print(f"Task deleted:\n{deleted_task.strip()}")

    except FileNotFoundError:
        print("Error: tasks.txt not found.")

def generate_reports():
    """
    Generates task_overview.txt and user_overview.txt with metrics.
    """
    try:
        with open("tasks.txt", "r") as f:
            tasks = [line.strip().split(", ") for line in f if line.strip()]

        total_tasks = len(tasks)
        completed_tasks = sum(1 for t in tasks if t[5].lower() == "yes")
        incomplete_tasks = total_tasks - completed_tasks
        overdue_tasks = sum(
            1 for t in tasks
            if t[5].lower() != "yes" and datetime.strptime(t[4], "%Y-%m-%d") < datetime.today()
        )
        percent_incomplete = (incomplete_tasks / total_tasks * 100) if total_tasks else 0
        percent_overdue = (overdue_tasks / total_tasks * 100) if total_tasks else 0

        with open("task_overview.txt", "w") as f:
            f.write(f"Total tasks: {total_tasks}\n")
            f.write(f"Completed tasks: {completed_tasks}\n")
            f.write(f"Incomplete tasks: {incomplete_tasks}\n")
            f.write(f"Overdue tasks: {overdue_tasks}\n")
            f.write(f"% Incomplete: {percent_incomplete:.2f}%\n")
            f.write(f"% Overdue: {percent_overdue:.2f}%\n")

        with open("user.txt", "r") as f:
            users = [line.strip().split(",")[0] for line in f if line.strip()]

        with open("user_overview.txt", "w") as f:
            f.write(f"Total users: {len(users)}\n")
            f.write(f"Total tasks: {total_tasks}\n\n")
            for user in users:
                user_tasks = [t for t in tasks if t[0] == user]
                num_user_tasks = len(user_tasks)
                completed = sum(1 for t in user_tasks if t[5].lower() == "yes")
                incomplete = num_user_tasks - completed
                overdue = sum(
                    1 for t in user_tasks
                    if t[5].lower() != "yes" and datetime.strptime(t[4], "%Y-%m-%d") < datetime.today()
                )
                task_percentage = (num_user_tasks / total_tasks * 100) if total_tasks else 0
                complete_percentage = (completed / num_user_tasks * 100) if num_user_tasks else 0
                incomplete_percentage = (incomplete / num_user_tasks * 100) if num_user_tasks else 0
                overdue_percentage = (overdue / num_user_tasks * 100) if num_user_tasks else 0

                f.write(f"User: {user}\n")
                f.write(f"Tasks assigned: {num_user_tasks}\n")
                f.write(f"% of total tasks: {task_percentage:.2f}%\n")
                f.write(f"% completed: {complete_percentage:.2f}%\n")
                f.write(f"% incomplete: {incomplete_percentage:.2f}%\n")
                f.write(f"% overdue: {overdue_percentage:.2f}%\n\n")

        print("Reports generated successfully.")

    except FileNotFoundError as e:
        print(f"Error generating reports: {e}")

def display_statistics():
    """
    Displays contents of task_overview.txt and user_overview.txt.
    Generates the reports first if the files do not exist.
    """
    if not (os.path.exists("task_overview.txt") and os.path.exists("user_overview.txt")):
        print("Report files not found. Generating reports first...")
        generate_reports()

    print("\n==== Task Overview ====")
    try:
        with open("task_overview.txt", "r") as file:
            print(file.read())
    except FileNotFoundError:
        print("task_overview.txt could not be read.")

    print("==== User Overview ====")
    try:
        with open("user_overview.txt", "r") as file:
            print(file.read())
    except FileNotFoundError:
        print("user_overview.txt could not be read.")

def login():
    """Handles login and credential validation."""
    with open("user.txt", "r") as file:
        users = {line.strip().split(',')[0]: line.strip().split(',')[1] for line in file}

    while True:
        username = input("Username: ")
        password = input("Password: ")

        if username in users and users[username] == password:
            print(f"Welcome, {username}!")
            return username
        else:
            print("Invalid username or password. Please try again.")

# ======== Main Menu Loop ========

def main():
    username = login()

    while True:
        if username == 'admin':
            menu = input(
                "\nPlease select one of the following options:\n"
                "r  - register user\n"
                "a  - add task\n"
                "va - view all tasks\n"
                "vm - view my tasks\n"
                "vc - view completed tasks\n"
                "del - delete task\n"
                "gr - generate reports\n"
                "ds - display statistics\n"
                "e  - exit\n: "
            ).lower()
        else:
            menu = input(
                "\nPlease select one of the following options:\n"
                "a  - add task\n"
                "va - view all tasks\n"
                "vm - view my tasks\n"
                "e  - exit\n: "
            ).lower()

        if menu == 'r' and username == 'admin':
            reg_user()
        elif menu == 'a':
            add_task()
        elif menu == 'va':
            view_all()
        elif menu == 'vm':
            view_mine(username)
        elif menu == 'vc' and username == 'admin':
            view_completed()
        elif menu == 'del' and username == 'admin':
            delete_task()
        elif menu == 'gr' and username == 'admin':
            generate_reports()
        elif menu == 'ds' and username == 'admin':
            display_statistics()
        elif menu == 'e':
            print("Goodbye!")
            break
        else:
            print("Invalid option or insufficient permissions.")

if __name__ == "__main__":
    main()
