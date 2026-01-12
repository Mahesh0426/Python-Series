# A dictionary is a data structure in Python that stores key-value pairs.
#Dictionaries are similar to JavaScript objects!

# Empty dictionary
my_dict = {}

# Using dict() constructor
another_dict = dict(name="Alice", age=22)

# Dictionary with initial values
student = {
    "name":"ramesh",
    "age": 22,
    "city":"Sydney"


}
print( "all the distionary item", student)

# Add a New Key-Value Pair
student["gender"] = "male"
print("student dictionary after adding new key-value pair", student)

#Update a Value
student["age"] = 23
print("student dictionary after updating age", student)

# Delete a Key-Value Pair
# del student["gender"]
# print("student dictionary after deleting key-value pair", student)

#pop to remove
# student.pop("gender")
# print("student dictionary after popping key-value pair", student)

#delete uisng popitem to delete last added key value
# student.popitem()
# print("student dictionary after popping last key-value pair", student)

print("My name is", student.get("name"))
print("I live in ",student["city"])
student["name"]= "bishal"
print("name after chnage",student)

# for in  | Loop Through Dictionary
# Print all keys and all values separately using a loop.
for key in student:
    # print(item)
    print(key, student[key])
    
# for key value
# for key, value in student.items():
#     print(key, value)

# check if  exist 
if "name" in student:
    print("name is present in the dictionary")

#length
print("Length of student dictionary is ", len(student))

#Nested Dictionary
students = {
    "Bikash": {"age": 20, "city": "Strathfield"},
    "Ramesh": {"age": 22, "city": "Ashfield"},
    "Mahesh": {"age": 21, "city": "Newtown"}
}

print(students["Mahesh"]["city"])  
# Output: London

# Square Numbers
square = {x:x**2 for x in range(1,6) }
print(square)
print(square.clear())
print(square)

#Print Keys and Values Separately
data = {"name": "Bishal", "age": 25, "city": "Newtown"}

for key in data.keys():
    print(key)
# Output: name, age, city

for value in data.values():
    print(value)
# Output: Alice, 25, New York


# Merge Two Dictionaries
dict1 = {"a": 1, "b": 2}
dict2 = {"c": 3, "d": 4}

merged_dict = dict1 | dict2  
print(merged_dict)
# Output: {'a': 1, 'b': 2, 'c': 3, 'd': 4}
