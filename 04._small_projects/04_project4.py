# 5. Advanced: Authentication + Role Access
# Uses: dict + tuple + while + break + continue + nested conditions

# Problem
# Your system should:
#  - Ask for username
#  - Ask for password
#  - Verify role
#  - If admin, show admin menu
#  - If customer, show customer menu
#  - Stop with "quit"

# Users data:

users = {
    "admin": ("pass123", "admin"),
    "john": ("hello", "customer"),
    "sita": ("world", "customer")
}

while True :
    username = input("Enter username: ")
    if username == "quit":
        break
    if username not in users:
        print("User not found")
        continue

    password = input("Enter password: ")

    #unpack tuple
    stored_pass,role = users[username]

    if password != stored_pass:
        print("invalid password")
        continue
    
    print("Access granted")

    if role == "admin":
        print("Admin menu loaded...")
        print("[1] Add User")
        print("[2] Delete User")
        print("[3] Logout")
        choice = input("Enter your choice: ")
        if choice == "1":
            print("Add User")

            #todo
            name = input("Enter username: ")
            if name in users:
                print("Username already exists")
                continue
            password = input("Enter password: ")
            users[name] = (password, "customer")
            print("User added successfully")


        elif choice == "2":
            print("Delete User")

            #todo
            name = input("Enter username to delete: ")
            if name not in users:
                print("User not found")
                continue
            del users[name]
            print("User deleted successfully")

        elif choice == "3":
            print("Logout")
            break

    elif role == "customer":
        print("customer menu loaded...")
        print("[1] View Profile")
        print("[2] Logout")
        choice = input("Enter your choice: ")
        if choice == "1":
            print("View Profile")

            #todo
            print("Username: ", username)
            print("Role: ", role)

        elif choice == "2":
            print("Logout")
            break

  
    
    