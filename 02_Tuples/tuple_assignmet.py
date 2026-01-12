# 1️⃣ Create a tuple with at least five numbers and print its sum.
numbers = (1, 2, 3, 4, 5)
print(sum(numbers))

# 2️⃣ Find the largest and smallest elements in a tuple.
num = (2,5,8,9,11,23,45)
print("Smallest element:", min(num))
print("Largest element:", max(num))

# 3️⃣ Convert a list into a tuple.
my_list = [1, 2, 3, 4, 5]
my_tuple = tuple(my_list)
print(my_tuple)

# 4️⃣ Check if a value exists in a tuple.
my_tuple = (1, 2, 3, 4, 5)
value = 3
print(value in my_tuple)

 # 5️⃣ Given a tuple (1, 2, 3, [4, 5]), modify the list inside the tuple to [40, 50].
my_tuple = (1, 2, 3, [4, 5])

# Modifying the list inside the tuple
my_tuple[3][0] = 40
my_tuple[3][1] = 50 
print(my_tuple)

# 6️⃣ Write a function that returns multiple values as a tuple.
def calculate_values(a, b):
    sum_result = a + b
    product_result = a * b
    difference_result = a - b
    return sum_result, product_result, difference_result  # Returns a tuple

# Calling the function
result = calculate_values(5, 3)

print(result)  # Output: (8, 15, 2)

# Unpacking the tuple
sum_val, product_val, diff_val = result
print("Sum:", sum_val)       # Output: Sum: 8
print("Product:", product_val)  # Output: Product: 15
print("Difference:", diff_val)  # Output: Difference: 2

# 7️⃣ Write a program to swap two numbers using tuple unpacking.
num1 = 5
num2 = 10

# Swapping numbers using tuple unpacking
num1, num2 = num2, num1
print("After swapping:")
print("num1:", num1)  # Output: num1: 10
print("num2:", num2)  # Output: num2: 5

# 8️⃣ Use tuple unpacking to extract first and last elements of a tuple.
my_tuple = (1, 2, 3, 4, 5)
first_element, *middle_elements, last_element = my_tuple
print("First element:", first_element)  # Output: First element: 1
print("Middle elements:", middle_elements)  # Output: Middle elements: [2, 3, 4]
print("Last element:", last_element)  # Output: Last element: 5