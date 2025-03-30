# Basic for 
for i in range(5):
    print("Iteration:", i)

#Looping Through a List
fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    print(fruit)


#while Loop (Runs Until a Condition is Met)
count = 0
while count < 5:
    print("Count:", count)
    count += 1


#  Using break and continue
for i in range(10):
    if i == 5:
        break  # Stops when i is 5
    print(i)

for i in range(10):
    if i == 5:
        continue  # Skips 5
    print(i)



#Looping Through a String
word = "Python"
for letter in word:
    print(letter)


#Nested Loops
for i in range(3):
    for j in range(3):
        print(f"({i}, {j})")


# grid 
for i in range(3):
    for j in range(3):
        print("*", end=" ")
    print()
