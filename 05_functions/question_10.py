#Write a function that takes a number and returns whether it's even or odd.
def check_even_odd(number):
    if number % 2 == 0:
        return "Even"
    else:
        return "Odd"

# Test cases
print(check_even_odd(10))  # Output: Even
print(check_even_odd(7))   # Output: Odd
