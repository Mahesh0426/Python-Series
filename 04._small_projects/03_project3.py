# 3. Advanced: Banking System With Multiple Accounts
# Uses: dict + tuple + while + break + continue + conditions

# Problem
# Create a login-based banking app where user can:
#  - Enter username
#  - Verify PIN
#  - Withdraw mone
#  - Stop with "exit"

# If wrong PIN is entered 3 times, lock the user out.
# You have bank customers stored like:

accounts = {
    "mahesh": {"balance": 5000, "pin": 1234},
    "john": {"balance": 8200, "pin": 4321},
    "Alish":{"balance":100000,"pin":4444}
}

while True:
    name = input("Enter your username (exit to quit): ")
    if name == "exit":
        break
    if name not in accounts:
        print("Username not found use correct name!!")
        continue

    attempts = 0
    max_attempts = 3 

    while attempts < max_attempts:
        pin = int(input("enter your PIN:"))
        if pin == accounts[name]["pin"]:
            print("Access granted")
            break
        attempts += 1
        print(f"Remaining attempts: {max_attempts - attempts}")
    else:
        print("Too many attempts. Account locked.")
        continue

     # Now logged in
    print (f"welcome {name}")
    while True:
        option = input("Withdraw or Exit?").lower()

        if option == "exit":
            break
        if option == "withdraw":
            amount = int(input("Enter amount to withdraw: "))
            if amount > accounts[name]["balance"]:
                print("insufficient balance")
                continue

            accounts[name]["balance"] -= amount
            print("withdrawl successfull")
            print("New balance: ", accounts[name]["balance"])
            
     
