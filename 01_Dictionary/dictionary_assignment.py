# 1.Create a dictionary of 5 countries and their capitals.
# Print the capital of any country using its key.

countries = {"Australia":"Canberra","Nepal":"Kathmandu","India":"New Delhi","USA":"Washington DC","UK":"London"}
print("The capital of Australia is:", countries["Australia"])
print("The capital of Nepal is:",countries.get("Nepal"))


# 2.Add and remove elements in a dictionary.
# Create a dictionary with 3 fruits and their prices.
# Add a new fruit to the dictionary.
#Remove one fruit using the pop() method.

fruits= {"Grapes":3,"Banana":8, "Apple":6}
fruits["Orange"] = 4
print(fruits)
fruits.pop("Banana")
print(fruits)
# fruits.popitem()
# print(fruits)

# 3. Check if a key exists in a dictionary.
# Given data = {"name": "Alice", "age": 25, "city": "New York"}, check if "age" exists in the dictionary.
# Print "Key exists" if found, otherwise print "Key not found".

data = {"name":"Alice","age":25, "city":"Nee York"}

# Method 1: Using 'in' keyword 
if "age" in data:
    print("Key exists")
else:
    print("Key not found")

# Method 2: Using the get() method
if data.get("age") is not None:
    print("Key exists")
else:
    print("Key not found")

# 4. Count the frequency of characters in a string.
# Take a string input from the user (e.g., "hello") and create a dictionary that stores the count of each character.
# Example output for "hello": {'h': 1, 'e': 1, 'l': 2, 'o': 1}

# Take input from user
user_input = input("Enter a string: ")

# Initialize an empty dictionary to store character counts
char_count = {}

# Count each character in the string
for char in user_input:
    if char in char_count:
        char_count[char] += 1
    else:
        char_count[char] = 1

# Display the result
print("Character frequencies:", char_count)

#  5. Sort a dictionary by values.
# Given marks = {"Alice": 88, "Bob": 75, "Charlie": 90}, sort the dictionary by marks in descending order.

marks = {"Alice": 88, "Bob": 75, "Charlie": 90}
dec_order = dict(sorted(marks.items(), key=lambda item: item[1], reverse=True))
print("Sorted dictionary by marks (descending):", dec_order)

# 6. Use dictionary comprehension to create a dictionary of squares.
# Create a dictionary where keys are numbers from 1 to 5 and values are their squares.
# Example output: {1: 1, 2: 4, 3: 9, 4: 16, 5: 25}

square = {x:x**2 for x in range(1,6) }
print("Dictionary of squares:", square)

# 7. Convert two lists into a dictionary.
# Given:
# keys = ["name", "age", "city"]
# values = ["Alice", 25, "New York"]
# Convert these into a dictionary: {"name": "Alice", "age": 25, "city": "New York"}

keys = ["name", "age", "city"]
values = ["Alice", 25, "New York"]

# Method 1: Using zip() in a dictionary comprehension
# result_dict = {k: v for k, v in zip(keys, values)}

# Method 2: Using dict() with zip()
result_dict = dict(zip(keys, values))
print("values into dictionary",result_dict)

# 8. Find the key with the maximum value.
# Given data = {"a": 10, "b": 50, "c": 30}, find the key with the highest value ("b") and print it.
data = {"a": 10, "b": 50, "c": 30}
max_key = max(data, key=data.get)
print( "highest value:", max_key) 

# 9. Create a nested dictionary for a student's report card.
# report_card = {
#     "Alice": {"Math": 85, "Science": 90, "English": 88},
#     "Bob": {"Math": 78, "Science": 82, "English": 80},
# }
# Print Alice’s Math score.
# Add a new subject "History": 92" to Bob’s record.
# Remove "English" from Alice’s record.

report_card = {
     "Alice": {"Math": 85, "Science": 90, "English": 88},
    "Bob": {"Math": 78, "Science": 82, "English": 80},
 }
# print Alice's Math score.
print("score of Alice in Math:",report_card["Alice"]["Math"])

# Add a new subject "History": 92" to Bob's record.
report_card["Bob"]["History"]= 92
print("report card after adding history score:", report_card["Bob"])

# Remove "English" from Alice's record.
del report_card["Alice"]["English"]
print("report card after removing English score:", report_card["Alice"])