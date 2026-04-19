# 1. 20Ask the user for a number and check if it is positive, negative, or zero.

# number = float(input("Enter a number: "))

# if number > 0:
#     print("The number is positive.")
# elif number < 0:
#     print("The number is negative.")
# else:
#     print("The number is zero.")

# 2. Ask the user for a temperature and classify it as Cold, Warm, or Ho

# temperature = float(input("Enter the temperature: "))
# if temperature < 15:
#     print("It is Cold.")
# elif temperature <= 30:
#     print("It is Warm.")
# else:
#     print("It is Hot.")

# 3. Create a program that checks if a triangle is valid. 
# A triangle is valid if the sum of any two sides is greater than the third.

# Take input from user
a = float(input("Enter side 1: "))
b = float(input("Enter side 2: "))
c = float(input("Enter side 3: "))

# Check triangle validity
if (a + b > c) and (a + c > b) and (b + c > a):
    print("The triangle is valid.")
else:
    print("The triangle is not valid.")