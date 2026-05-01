#Uses: while + if + dict + tuple + continue

#Problem

# Create a loop where the user can:
#  - Buy an item
#  - Check available stock
#  - Skip invalid items
#  - Stop by typing "exit"

# Each item has (quantity, price).
# You have an inventory like this:
inventory = {
    "apple": (50, 2.5),
    "banana": (30, 1.2),
    "milk": (20, 3.0)
}

while True:
    item = input("Enter the item you want to buy or type 'exit' to quit: ")

    if item == "exit":
        break

    if item not in inventory:
        print("sorry item is not available")
        continue

   # destructure tuple | unpack tuple
    qty_available,price = inventory[item]
    qty_wanted = int(input("How many you want to buy : "))

    if qty_wanted > qty_available:
        print(f"Only {qty_available} {item} are available")
        continue
    total = qty_wanted * price

    print(f"You bought {qty_wanted} of {item} and total cost is ${total}")
       # update inventory
    inventory[item] = (qty_available - qty_wanted, price)
    
print("Final Inventory:", inventory)

   

    


