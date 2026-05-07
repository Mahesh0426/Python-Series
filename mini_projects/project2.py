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
    print(entry)
    transactions.append(entry)
    print("tranctions", transactions)
    print(f"Deposit Successful! New balance: $ {balance:.2f}")


# withdraw function
def withdraw(amount):
    global balance
    if amount <= 0:
        print(" ❌ Invalid Amount")
        return
    if amount > balance:
        print(f"❌ Insufficient Balance. Limit: $ {balance:.2f}")
        return
    
    balance -= amount
    entry = f"Withdraw: ${amount:.2f} -> Balance: ${balance:.2f}"
    print("\n")
    print(entry)
    transactions.append(entry)
    print("tranctions", transactions)
    print(f"\n  ✅ ${amount:.2f} withdrawn successfully.")
    print(f"  💰Remaining balance: $ {balance:.2f}")

# show transaction
def show_transactions():
    print("\n===== TRANSACTION HISTORY =====")
    print(" " + "-" * 50)

    if not transactions:
        print("No transactions yet.")
    else:
        for i, t in enumerate(transactions , 1):
            print(f" {i:>2}. {t}")
    print(" " + " " * 50)
        
  
    
# get amount
def get_amount(prompt):
   try:
    amount = float(input(prompt).strip())
    if amount <= 0:
        print("\n  ❌ Invalid Amount")
        return None
    return amount
   except ValueError:
    print("\n  ❌ Invalid amount. Please enter a number.")
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
    print("\nATM is starting up.....")
    while True:
        show_menu()
        choice = input("Enter your choice (1-5): ").strip()

        if choice == "1":
            check_balance()
        elif choice =="2":
            amount = get_amount("Enter amount to deposit : ")
            if amount is not None:
              deposit(amount)
        elif choice == "3":
            amount = get_amount("Enter amount to withdraw:")
            if amount is not None:
                withdraw(amount)
        elif choice == "4":
            show_transactions()
        
        elif choice == "5":
            print("\n Thank you for using PyATM. Good Bye!")
            break
        
            
        else:
            print("\n Invalid choice. Please try again.")





if __name__ == "__main__":
    main()
    