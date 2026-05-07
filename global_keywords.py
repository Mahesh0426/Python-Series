# Python has two scopes:
# Global scope → variables defined outside all functions
# Local scope → variables defined inside a function (they die when the function ends)

# example 1
balance = 1000.00   # Global variable

def deposit(amount):
    global balance          # 👈 "Hey Python, use the GLOBAL balance"
    balance += amount       # Modifies the actual global balance
    print("Updated balance :", balance)  
# deposit(300)
# print("final balance :", balance)   

# Python looks at global balance and says — "go find balance in the global scope and modify it"
# So when balance += amount runs, it updates the real balance variable
# After the function ends, balance is permanently changed ✅

#example 2 - WITHOUT global
def deposit(amount):
    # NO global keyword
    balance += amount    # 💥 ERROR!
    print("Updated balance :", balance)  

# deposit(200)

#EXPERIMENT 1 -Just reading (no global needed):
def check_balance():
    print(balance)   # ✅ Works fine — just READING, not modifying

check_balance()
# Output: 1000.0

#EXPERIMENT - 2  Modifying WITHOUT global:
def deposit(amount):
    balance += amount   # ❌ CRASH!

# deposit(500)
# Output: UnboundLocalError: local variable 'balance' referenced before assignment


# EXPERIMENT 3-  Modifying WITH global:
def deposit(amount):
    global balance
    balance += amount   # ✅ Works perfectly

deposit(500)
print(balance)
# Output: 1500.0