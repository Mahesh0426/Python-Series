# print("hello world!")

# def chai(n):
#     print(n)

# chai(4)

print("+ operator", 2 + 2)
print("- operator", 4 - 2)
print("* operator", 2 * 2)
print("/ operator", 6 / 2)  # Float division
print("% operator", 8 % 3)  # Modulus (remainder)
print("** operator", 2 ** 3)  # Exponentiation


    
# Comparison Operators
print("comparison1", 2 == 2)  # True
print("comparison2", 2 == 3)  # False 
print("comparison3", 2 != 3)  # True 
print("comparison4", 2 == "2")  # False (Python compares int vs string)
print("comparison5", 4 < 2)  # False
print("comparison6", 2 <= 2)  # True
print("comparison7", 4 <= int("2"))  # Convert string to int before comparison

# Logical Operators
print("comparison8", True and True)  # AND operator
print("comparison9", True or True)  # OR operator
print("comparison10", not 2)  # NOT operator (2 is truthy, so "not 2" is False)

# Ternary Operator (Conditional Expression in Python)
print("ternary operator", "true" if 4 < 2 else "false")  # False

# Membership Operators:
name = "Alice"
print("A" in name)  # True
print("a" not in name)  # True

#Identity Operators
a = [1, 2, 3]
b = [1, 2, 3]
c = a
print(a is b)   # False (they are two different objects in memory)
print(a is c)   # True (they point to the same object)
