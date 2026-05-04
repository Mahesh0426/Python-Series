# 1. Expense Tracker (Small Project)

# Functions you create:
# add_expense(amount, category)
# get_total_expense()
# get_expense_by_category(category)
# reset_expenses()

expenses=[]

def add_expense(amount, category):
    if amount <=0:
        print("Amount must be positive")
        return

    expense = {"amount":amount,"category":category.lower().strip()}
    expenses.append(expense)
    print(f"Expense of ${amount} added under category: {category}")


#get total of all expensesd
def get_total_expense():
    if not expenses:
        print("No expenses found")
        return 0.0

    total=sum(e["amount"] for e in expenses)
    print(f"Total expenses: ${total:.2f}")
    return total

#get expenses by category

def get_expenses_by_category(category):
    category = category.lower().strip()
    filtered = [e for e in expenses if e["category"]== category]

    if not filtered:
        print(f"No expense found in category : {category}")
        return []
        

    cat_total = sum(e["amount"] for e in filtered)
    print(f"\n Category: {category.capitalize()}")
    print(f" Entries : {len(filtered)}")
    print(f" Total : ${cat_total:.2f}")
    items = [f"-${e['amount']:2f}" for e in filtered]
    print(f"\n Items   : {items}")
    return filtered

#reset expenses
def reset_expenses():
    expenses.clear()
    print("All expenses have been reset.")


# show full summary
def show_summary():
    if not expenses:
        print("No expenses recorded yet")
        return

        categories = {}
        for e in expenses:
            cat = e["category"]
            categories[cat]= categories.get(cat,0)+e["amount"]
        print("\n---------- Expense Summary ----------")
        
        for cat, total in sorted(categories.items()):
            print(f"{cat.capitalize():<15} : ${total:.2f}")
        print("------------------------------------")
        print(f"{'Total': <18} ${sum(categories.values()):.2f}")


 # ══════════════════════════════════════════
#                   DEMO
# ══════════════════════════════════════════       
        

if __name__ == "__main__":
    print("\n── Adding Expenses ──")
    add_expense(50.00,  "food")
    add_expense(120.00, "rent")
    add_expense(15.50,  "food")
    add_expense(200.00, "utilities")
    add_expense(30.00,  "food")
    add_expense(60.00,  "transport")
 
    print("\n── Total Expense ──")
    get_total_expense()
 
    print("\n── Expenses by Category ──")
    get_expenses_by_category("food")
    get_expenses_by_category("rent")
    get_expenses_by_category("gym")   # category not found
 
    print("\n── Full Summary ──")
    show_summary()
 
    print("── Reset ──")
    reset_expenses()
    get_total_expense()        
    


    



