import json

def load_users(users_file):
    try:
        with open('user_data.txt', 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        return []

def save_users(users, users_file):
    with open('user_data.txt', 'w') as file:
        json.dump(users, file, indent=4)

def updateUser(users_file, id, newName, newEmail):
    users = load_users('user_data.txt')
    for user in users:
        if user['id'] == id:
            user['name'] = newName
            user['email'] = newEmail
            break
    save_users(users, 'user_data.txt')

def main():
    users_file = 'user_data.txt'
    id = int(input("Enter user ID to update: "))
    newName = input("Enter new name: ")
    newEmail = input("Enter new email: ")
    updateUser(users_file, id, newName, newEmail)
    print("User data updated successfully.")

if __name__ == "__main__":
    main()