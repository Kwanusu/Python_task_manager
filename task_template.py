import os
import hashlib
from datetime import datetime

# Initialize empty dict to store 
user_pass_dict = {}

with open('user.txt', 'r+') as user_file:
    for line in user_file:
        parts = line.strip().split(', ')
        if len(parts) == 2:
            username = parts[0].strip()
            password = parts[1].strip()
            user_pass_dict[username] = password
        elif len(parts) == 1:
            username = parts[0].strip()
            user_pass_dict[username] = "" 
            
def admin_login():
    admin_username = input("Enter admin username: ")
    admin_password = input("Enter admin password: ")
    if admin_username == "admin" and admin_password == "adm1n":
        return True
    else:
        return False
                       

while True:
    username_input = input("Please enter your username, (Please note username is case sensitive): ")
    if username_input in user_pass_dict:
        print(f"Hello, {username_input}.")
        
        while True:
            password = input("Please enter your password: ")
            if password == user_pass_dict[username_input]:    
                print(f"Welcome {username_input}!")
                break
            elif password.lower() == 'exit':
                print("Goodbye")
                break
            else:
                print("Password incorrect, please try again")
        break
    else:
        print("Username invalid, please try again or contact system administrator")

# Function to hash passwords
def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()

# Load users and tasks from files
def load_users():
    users = {}
    with open("users.txt", "r") as file:
        for line in file:
            username, password = line.strip().split(", ")
            users[username] = password
    return users

# Function to save users to file
def save_users(users):
    with open("users.txt", "w") as file:
        for username, password in users.items():
            file.write(f"{username}, {password}\n")

# Function to load tasks from file
def load_tasks():
    tasks = []
    with open("tasks.txt", "r") as file:
        for line in file:
            task_info = line.strip().split(", ")
            tasks.append({
                "assigned_user": task_info[0],
                "title": task_info[1],
                "description": task_info[2],
                "assigned_date": datetime.strptime(task_info[3], "%Y-%m-%d"),
                "due_date": datetime.strptime(task_info[4], "%Y-%m-%d"),
                "completed": task_info[5]
            })
    return tasks

# Function to save tasks to file
def save_tasks(tasks):
    with open("tasks.txt", "w") as file:
        for task in tasks:
            file.write(f"{task['assigned_user']}, {task['title']}, {task['description']}, "
                       f"{task['assigned_date'].strftime('%Y-%m-%d')}, {task['due_date'].strftime('%Y-%m-%d')}, "
                       f"{task['completed']}\n")

# Function to register new user
def register_user():
    username = input("Enter new username: ")
    password = hash_password(input("Enter new password: "))
    confirm_password = hash_password(input("Confirm password: "))
    if password == confirm_password:
        users[username] = password
        save_users(users)
        print("User registered successfully.")
    else:
        print("Passwords do not match.")

# Function to display statistics
def display_statistics():
    total_users = len(load_users())
    total_tasks = len(load_tasks())
    print(f"Total number of users: {total_users}")
    print(f"Total number of tasks: {total_tasks}")

# Function to add new task
def add_task():
    assigned_user = input("Enter username of the assigned user: ")
    title = input("Enter task title: ")
    description = input("Enter task description: ")
    due_date = datetime.strptime(input("Enter due date (YYYY-MM-DD): "), "%Y-%m-%d")
    current_date = datetime.now()
    tasks.append({
        "assigned_user": assigned_user,
        "title": title,
        "description": description,
        "assigned_date": current_date,
        "due_date": due_date,
        "completed": "No"
    })
    save_tasks(tasks)
    print("Task added successfully.")

# Function to view all tasks
def view_all_tasks():
    tasks = load_tasks()
    for task in tasks:
        print_task(task)

# Function to view tasks assigned to the logged-in user
def view_my_tasks():
    username = input("Enter your username: ")
    tasks = load_tasks()
    for task in tasks:
        if task["assigned_user"] == username:
            print_task(task)

# Function to print task details
def print_task(task):
    print(f"Assigned User: {task['assigned_user']}")
    print(f"Title: {task['title']}")
    print(f"Description: {task['description']}")
    print(f"Assigned Date: {task['assigned_date']}")
    print(f"Due Date: {task['due_date']}")
    print(f"Completed: {task['completed']}")
    print()

def main():
    global users, tasks
    users = load_users()
    tasks = load_tasks()

    while True:
        print("\nMain Menu:")
        print("1. Admin Login")
        print("2. Exit")
        choice = input("Enter choice (1/2): ")

        if choice == "1":  # Admin Login
            admin_username = input("Enter admin username: ")
            admin_password = input("Enter admin password: ")
            if admin_username == "admin" and admin_password == "adm1n":
                admin_menu()
            else:
                print("Invalid admin credentials.")

        elif choice == "2":  # Exit
            break

        else:
            print("Invalid choice.")

def admin_menu():
    while True:
        print("\nAdmin Menu:")
        print("a. Add a new task")
        print("r. Register new user")
        print("va. View all tasks")
        print("vm. View my tasks")
        print("s. Display statistics")
        print("e. Logout")
        choice = input("Enter choice (a/r/va/vm/s/e): ")

        if choice == "a":  # Add Task
            add_task()

        elif choice == "r":  # Register new user
            register_user()

        elif choice == "va":  # View All Tasks
            view_all_tasks()

        elif choice == "vm":  # View My Tasks
            view_my_tasks()

        elif choice == "s":  # Display Statistics
            display_statistics()

        elif choice == "e":  # Logout
            break

        else:
            print("Invalid choice.")

if __name__ == "__main__":
    main()
