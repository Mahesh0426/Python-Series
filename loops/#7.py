#1 Counting a list of Numbers 
# Given a list of numbers, count how many are positive
numbers =[1,-2,3,-4,5,6,-7,-8,9, 10]
positive_num_count = 0
for num in numbers:
    if num >0:
        positive_num_count += 1

print("final count of positive num is",positive_num_count)

#2 Calculate the sum of even number up to a given number n
num = 10
sum_even = 0
for i in range(1, num+1):
    if i % 2 == 0 :
        sum_even += i

print("sum of even number is",sum_even)

#3 Print the multiplication table for a given number up to 10, but skip the fifth iteration
num = 3

for i in range(1,11):
    if i == 5:
        continue
    print(num, "x", i, "=", num*i)


#4 reverse string using loop 

str_input = "hello"
reverse_str= ""

for char in str_input:
    reverse_str = char + reverse_str
print(reverse_str)

#5 find the first non repeated characdter
# given a string, find tge first non repeated character

input_str = "teeter"

for char in input_str:
    if input_str.count(char) == 1:
      print("char is:",char)
      break

#6 Factorial calculator
# compute the factorials of a number using a while loop 
number = 5
factorial = 1 

while number > 0:
    factorial = factorial * number
    number = number - 1
print("Factorial:",factorial)

#7 Keep asking the user for input until they enter a number beth 1 and 10 
while True:
    number= int (input("Enter value beth 1 and 10: "))
    if 1 <= number <= 10:
        print("Thanks ")
        break
    else:
        print("Invalid number try again")


#8 check the prime number 
number = 27
is_prime = True

if number > 1:
    for i in range(2, number):
        if (number % i) == 0:
            is_prime = False
            break

print(is_prime)


# 9 check if all the elements in the list are unique. If a duplicate is found, exit the loop and print the duplicate

items=["apple","banana","orange","apple","mango","banana"]
