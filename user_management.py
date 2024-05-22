# import json
# import os
# #User creation
# def create_user():
#     user_data = {}
#     user_data['id'] = int(input("Enter user ID: "))
#     user_data['name'] = input("Enter user name: ")
#     user_data['email'] = input("Enter user email: ")
#     user_data['isActive'] = input("Is user active? (True/False): ").lower() == 'true'
#     return user_data
# # Initializing user file if none exists
# def initialize_file(users_file):
#     if not os.path.exists(users_file):
#         with open(users_file, 'w') as file:
#             json.dump([], file)
# # function to load users to the file.txt
# def load_users(users_file):
#     with open(users_file, 'r') as file:
#         return json.load(file)
# #function to save users to the txt file
# def save_users(users, users_file):
#     with open(users_file, 'w') as file:
#         json.dump(users, file, indent=4)
# # function to update users details
# def updateUser(users_file, user_id, newName, newEmail):
#     users = load_users(users_file)
#     for user in users:
#         if user['id'] == user_id:
#             user['name'] = newName
#             user['email'] = newEmail
#             break
#     save_users(users, users_file)
# #function to delete users from the txt
# def deleteUser(users_file, user_id):
#     users = load_users(users_file)
#     users = [user for user in users if user['id'] != user_id]
#     save_users(users, users_file)
# # function to list/show users info
# def listUsers(users_file):
#     users = load_users(users_file)
#     for user in users:
#         print(f"ID: {user['id']}, Name: {user['name']}, Email: {user['email']}, Active: {user['isActive']}")
# # function to search for users
# def findUsersByName(users_file, searchString):
#     users = load_users(users_file)
#     result = [user for user in users if searchString.lower() in user['name'].lower()]
#     return result
# # The main function to prompt user to perform given task
# def main():
#     users_file = 'users.json'
#     initialize_file(users_file)

#     while True:
#         choice = input('''Select one of the following options:
#         1. Create User
#         2. Update User
#         3. Delete User
#         4. List Users
#         5. Find Users by Name
#         6. Exit
#         Enter your choice: ''')
        
#         if choice == '1':
#             user_data = create_user()
#             users = load_users(users_file)
#             users.append(user_data)
#             save_users(users, users_file)
#             print("User data has been saved.")

#         elif choice == '2':
#             user_id = int(input("Enter user ID to update: "))
#             newName = input("Enter new name: ")
#             newEmail = input("Enter new email: ")
#             updateUser(users_file, user_id, newName, newEmail)
#             print("User updated successfully.")

#         elif choice == '3':
#             user_id = int(input("Enter user ID to delete: "))
#             deleteUser(users_file, user_id)
#             print("User deleted successfully.")

#         elif choice == '4':
#             print("List of Users:")
#             listUsers(users_file)

#         elif choice == '5':
#             searchString = input("Enter the name to search: ")
#             result = findUsersByName(users_file, searchString)
#             print("Users with name containing '{}' are:".format(searchString))
#             for user in result:
#                 print(f"ID: {user['id']}, Name: {user['name']}, Email: {user['email']}, Active: {user['isActive']}")
        
#         elif choice == '6':
#             print("Exiting the program.")
#             break

#         else:
#             print("Invalid choice. Please try again.")

# if __name__ == "__main__":
#     main()

import json
import os

# User creation
def create_user():
    user_data = {}
    user_data['id'] = int(input("Enter user ID: "))
    user_data['name'] = input("Enter user name: ")
    user_data['email'] = input("Enter user email: ")
    user_data['isActive'] = input("Is user active? (True/False): ").lower() == 'true'
    return user_data

# Initializing user files if none exist
def initialize_files(users_json_file, users_txt_file):
    if not os.path.exists(users_json_file):
        with open(users_json_file, 'w') as file:
            json.dump([], file)
    if not os.path.exists(users_txt_file):
        open(users_txt_file, 'w').close()

# Function to load users from JSON file
def load_users_json(users_file):
    with open(users_file, 'r') as file:
        return json.load(file)

# Function to save users to JSON file
def save_users_json(users, users_file):
    with open(users_file, 'w') as file:
        json.dump(users, file, indent=4)

# Function to append users to TXT file
def append_users_txt(user_data, users_file):
    with open(users_file, 'a') as file:
        file.write(f"ID: {user_data['id']}, Name: {user_data['name']}, Email: {user_data['email']}, Active: {user_data['isActive']}\n")

# Function to create user and append to both JSON and TXT files
def create_user_and_append(users_json_file, users_txt_file):
    user_data = create_user()
    users_json = load_users_json(users_json_file)
    users_json.append(user_data)
    save_users_json(users_json, users_json_file)
    append_users_txt(user_data, users_txt_file)
    print("User data has been saved.")

# The main function to prompt user to perform given task
def main():
    users_json_file = 'users.json'
    users_txt_file = 'users.txt'
    initialize_files(users_json_file, users_txt_file)

    while True:
        choice = input('''Select one of the following options:
        1. Create User
        2. Update User
        3. Delete User
        4. List Users
        5. Find Users by Name
        6. Exit
        Enter your choice: ''')
        
        if choice == '1':
            create_user_and_append(users_json_file, users_txt_file)

        elif choice == '2':
            user_id = int(input("Enter user ID to update: "))
            newName = input("Enter new name: ")
            newEmail = input("Enter new email: ")
            updateUser(users_json_file, user_id, newName, newEmail)
            print("User updated successfully.")

        elif choice == '3':
            user_id = int(input("Enter user ID to delete: "))
            deleteUser(users_json_file, user_id)
            print("User deleted successfully.")

        elif choice == '4':
            print("List of Users:")
            listUsers(users_json_file)

        elif choice == '5':
            searchString = input("Enter the name to search: ")
            result = findUsersByName(users_json_file, searchString)
            print("Users with name containing '{}' are:".format(searchString))
            for user in result:
                print(f"ID: {user['id']}, Name: {user['name']}, Email: {user['email']}, Active: {user['isActive']}")

        elif choice == '6':
            print("Exiting the program.")
            break

        else:
            print("Invalid choice. Please try again.")

# function to update users details
def updateUser(users_file, user_id, newName, newEmail):
    users = load_users_json(users_file)
    for user in users:
        if user['id'] == user_id:
            user['name'] = newName
            user['email'] = newEmail
            break
    save_users_json(users, users_file)

# function to delete users from the JSON file
def deleteUser(users_file, user_id):
    users = load_users_json(users_file)
    users = [user for user in users if user['id'] != user_id]
    save_users_json(users, users_file)

# function to list/show users info
def listUsers(users_file):
    users = load_users_json(users_file)
    for user in users:
        print(f"ID: {user['id']}, Name: {user['name']}, Email: {user['email']}, Active: {user['isActive']}")

# function to search for users
def findUsersByName(users_file, searchString):
    users = load_users_json(users_file)
    result = [user for user in users if searchString.lower() in user['name'].lower()]
    return result

if __name__ == "__main__":
    main()
