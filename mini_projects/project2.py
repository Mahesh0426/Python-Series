# 2. Simple ATM Simulator
# Functions:

# * check_balance()
# * deposit(amount)
# * withdraw(amount)
# * show_transactions()
# Use a loop to keep the program running.

balance = 500.00
transactions= ["Initial Deposit : $500.00"]

def check_balance():
    print(f"\n  Your  Current Balance is: $ {balance}")


def deposit(amount):
    global balance 
    if amount <=0:
        print("Amount must be positive")
        return

    balance += amount
   
    entry= f"Deposit : +${amount:.2f} -> Balance: ${balance:.2f}"
    transactions.append(entry)
    print(f"Deposit Successful! New balance: $ {balance:.2f}")


# withdraw function
def withdraw(amount):
    global balance
    if amount <=0:
        print("Invalid Amount")
        return

   
   
# get amount
def get_amount(prompt):
   try:
    amount = float(input(prompt).strip())
    if amount <= 0:
        print("Invalid Amount")
        return None
    return amount
   except ValueError:
    print("Invalid amount. Please enter a number.")
    return None

    
            


def show_menu():
    print("\n" + "=" * 40)
    print("         🏦  Welcome to PyATM")
    print("=" * 40)
    print("  [1] Check Balance")
    print("  [2] Deposit")
    print("  [3] Withdraw")
    print("  [4] Transaction History")
    print("  [5] Exit")
    print("=" * 40)       

# main loop

def main():
    print("\nATM is trarting upp.....")
    while True:
        show_menu()
        choice = input("Enter your choice (1-5): ").strip()

        if choice == "1":
            check_balance()
        elif choice =="2":
            amount = get_amount("Enter amount to deposit : ")
            if amount is not None:
                deposit(amount)
            continue
            
        else:
            print("\n Invalid choice. Please try again.")





if __name__ == "__main__":
    main()
    