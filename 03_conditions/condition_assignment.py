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
# a = float(input("Enter side 1: "))
# b = float(input("Enter side 2: "))
# c = float(input("Enter side 3: "))

# Check triangle validity
# if (a + b > c) and (a + c > b) and (b + c > a):
#     print("The triangle is valid.")
# else:
#     print("The triangle is not valid.")


# 4. Build a simple login system. If the username is “admin” and the password is “1234”, show “Login successful”. Otherwise show “Login failed”.
username = input("Enter username: ")
password = input("Enter password: ")

if username == "admin" and password == "123" :
    print("Login successful")
else:
    print("authentication failed . Try again!!")

# 5 Create a program that checks if a person is allowed to vote. Rules: Age must be 18 or older and nationality must be Australian.
age = int(input("Enter your age: "))
nationality = input("Enter your nationality ?")

if age >= 18 and nationality.lower() == "australian":
    print("You are eligible for voting")
else:
    print("You are not eligible for voting")


# 6.Ask for a month number (1–12). Print how many days the month has. Use nested conditions for February.
month = int(input("Enter the month number (1-12): "))

if month == 2:
    year = int(input("Enter the year: "))
    if year % 4 == 0:
        print("The month has 29 days.")
    else:
        print("The month has 28 days.")
elif month in [4, 6, 9, 11]:
    print("The month has 30 days.")
else:
     print("The month has 31 days.")