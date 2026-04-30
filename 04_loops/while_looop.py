# 1.Use a while loop to print numbers 1 to 10.
# count = 1 
# while count <=10:
#     print(count)
#     count += 1

# 2. Print even numbers from 2 to 20
count = 2

# while count <= 20:
#     if count % 2 == 0:
#         print(count)
#     count += 1

#another way

while count <= 20:
    # print(count)
    count += 2
    
# 3. Sum of numbers from 1 to 100
count = 1
sum = 0

while count <= 100:
    sum = sum + count
    count = count + 1
    # print(sum)
    
# 4. Countdown from 10 to 1
count = 10
while count >= 1:
    # print(count)
    count -= 1

# 5. . Print digits of a number
# Example: input = 458
# Output:
# 5
# 8

num_val = 458
while num_val > 0:
    digit = num_val % 10
    # print(digit)
    num_val = num_val // 10
    
#6. 2. Reverse a number. Example: 123 → 321
num = 123
reversed_num = 0

while num > 0 :
    digit = num % 10
    # print(f"digit: {digit}")
    reversed_num = reversed_num * 10 + digit
    # print(f"reversed_num: {reversed_num}")
    num = num // 10
    # print(f"num: {num}")

# print(f"rev: {reversed_num}")   

# 7. Count digits in a number
# Example: 5409 → 4 digits

count = 0
num = 54098

while num > 0 :
    digit = num % 10
    # print(f"digit: {digit}")
    count += 1
    # print(f"count: {count}")  
    num = num // 10
    # print(f"num: {num}")
   
# print(f"Total digits: {count}")

# 8. Sum of digits
# Example: 452 → 4 + 5 + 2 = 11

num =  452
sum = 0
 
while num > 0:
    digit = num % 10
    # print(f"digit: {digit}")
    sum = sum + digit
    # print(f"sum: {sum}")
    num = num // 10
    # print(f"num: {num}")
# print(f"Total sum is: {sum}")


# 10. Check if a number is prime

num = 8

while num > 1:
    if num % 2 == 0:
        # print("Not prime")
        break 
    else:
        # print("Prime")
        break 

#11. 2. Find factorial of a number
# 5! = 120
num = 4
fact = 1

while num > 1:
    fact = fact * num
    # print(f"fact: {fact}")
    num -= 1
    # print(f"num: {num}")
    
# print(f"Factorial  is {fact}")

# 13. ATM PIN system (3 attempts only)
# Real-world use: ATMs limit wrong PIN attempts.
# Ask the user to enter a PIN.
# Allow only 3 attempts.
# Stop as soon as the user enters the correct PIN.
correct_pin = 1234
attempts = 0

while attempts < 3:
    pin = int(input(f"Enter PIN (Attempt {attempts + 1}): "))
    if pin == correct_pin:
        print("Access granted")
        break
    else:
        print("wrong pin try again")
        attempts +=1
        remaining = 3 - attempts
        if remaining > 0:
            print(f" You have {remaining} attempts left.")
if attempts == 3:
    print("Account locked")
else:
    print("Done")
    

    
