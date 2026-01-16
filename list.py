# numbers = [1, 2, 3, 4, 5]
mixed = ["hello", 42, 3.14, True]
fruits = ["apple", "banana", "cherry","orange"]
# print(fruits)
# print(fruits[0])  # First element
# print(fruits[-1])  # Last element

#  Slicing a List
# print(fruits[1:2])
# print(fruits[:2])
# print(fruits[2:])

#Modifying Elements
fruits[0]= "blueberries"
# print(fruits)
# fruits[1:2]= "grapes" 
# print(fruits)
fruits[1:2]= ["grapes"]
# print(fruits)
fruits[1:2]= []
# print(fruits)

#insert (Add at a specific index) | list.insert(index, value)
fruits.insert(4,"Kiwi")
# print(fruits)

#append (Add at the end) | list.append(value)
fruits.append("Mango")
# print(fruits)

# remove (Remove by value)
fruits.remove("orange")
# print(fruits)

# pop (Remove by index, default is the last one)
fruits.pop(1)
# print(fruits)

# extend (Add multiple items at the end)
fruits.extend(["Strawberry","Pineapple"])
# print(fruits)

# clear (Remove all items)
# fruits.clear()
# print(fruits)

# for in 
Frameworks = ["numpy","pandas","tensorflow","pytorch","Scikit-learn"]
# for popular_framework in Frameworks:
    # print(popular_framework, end="-")
    # print(popular_framework)


#Searching in a List
numbers = [0,1,3,1,4,5,6,7,8,9,10]
# print(3 in numbers)  # check if 3 is in the list | return boolean
# print(numbers.index(4))    # give the index of the value
# print(numbers.count(1)) 
 #This counts how many times the value 1 appears in the list numbers.


# Sorting a List
number = [5, 3, 1, 4, 2]
number.sort()
# print(number) 
 # Output: [1, 2, 3, 4, 5]


# Sorting a List in Descending Order (reverse=True)
# number.sort(reverse=True)
# print(number) 
 # Output: [5, 4, 3, 2, 1]

# Reversing a List
number.reverse()
# print(number)  
# Output: [5, 4, 3, 2, 1]   

#Copying a List
list1 = [1, 2, 3]
list2 = list1.copy()
list2.append(4)
print(list1)  # Output: [1, 2, 3]
print(list2)  # Output: [1, 2, 3, 4]

#joining Lists
list1 = [1, 2, 3]
list2 = [4, 5, 6]
combined = list1 + list2
# print(combined)  # Output: [1, 2, 3, 4, 5, 6]

 #List to String
words = ["Hello", "World"]
sentence = " ".join(words)
# print(sentence)  # Output: Hello World

#String to List
sentence = "Hello World"
words = sentence.split()
# print(words)  # Output: ['Hello', 'World']

#Nested Lists
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
# print(matrix[1][2])  # Output: 6  (Row index 1, Column index 2)

# List Comprehension
#without Comprehension
numbers = [1, 2, 3, 4, 5]
squares = []  

for num in numbers:
    squares.append(num ** 2)  

# print(squares)  # Output: [1, 4, 9, 16, 25]

# syntax - new_list = [expression for item in iterable]
numbers = [1, 2, 3, 4, 5]
squares = [num ** 2 for num in numbers]
# print(squares)  # Output: [1, 4, 9, 16, 25]

# Nested List Comprehension
squares = [x ** 2 for x in range(1, 6)]
# print(squares)  # Output: [1, 4, 9, 16, 25]

#Filtering elements
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
even_numbers = [x for x in numbers if x % 2 == 0]
# print(even_numbers)  # Output: [2, 4, 6, 8, 10]


