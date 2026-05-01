# INVOICE GENERATOR LOGIC (ADVANCED)
# Menu with items stored as tuples inside a dict:

# You will ask the user to add items. They can add multiple items until they type 0.

# System must:
# - Validate item numbers
# - Validate quantities
# - Add item totals
# - Store bill items as tuples: (item_name, qty, price, line_total)
# - Add tax
# - Add optional discount
# - Generate final invoice

menu = {
    1: ("Burger", 8.5),
    2: ("Pizza", 12.0),
    3: ("Pasta", 10.0),
    4: ("Coffee", 4.5),
    5: ("Fries", 3.0)
}

cart = []
subtotal = 0.0

print("----- MENU -----")
for key,val in menu.items():
    print(f"{key} : {val[0]} - ${val[1]}")

while True:
    choice = int(input("Enter item number(0 to checkout): "))

    if choice == 0:
        break
    if choice not in menu:
        print("Invalid item number, try again")
        continue
    item_name,price = menu[choice]
    qty = int(input(f"How many {item_name} ? " )) 

    if qty <= 0:
        print("Quantity must be positive")
        continue

    line_total = price * qty
    subtotal += line_total
    # print("subtotal", subtotal)

    cart.append((item_name,qty,price,line_total))
    print(f"Added {qty} x {item_name} = ${line_total} to cart")

# invoice section
print("\n------ INVOICE ------")

for name,qty,price, total in cart:
    print(f"{name} : {qty} x @${price:.2f} = ${total:.2f}")

print("\n Sub total ", subtotal)

# optional discount
discount = input("Apply 10% discount? (y/n): ").lower()

if discount == "y":
    discount_amount = subtotal * 0.10
    print("10% discount applied")
else:
    discount_amount = 0

# tax
tax = (subtotal - discount_amount) * 0.05

#final total
final_total = subtotal - discount_amount + tax

print("\n ------Final bill-------")

print(f"Discount {discount_amount:.2f}")
print(f"Tax (5%) {tax:.2f}")
print(f"Final total: {final_total:.2f}")
print("------- Thank you for shopping with us ------")
    




    

 
    
    