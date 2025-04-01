#Write a function that takes a number and returns the sum of its digits
def sum_of_digits(n):
    total = 0
    while n > 0:
        total += n % 10  # Extract last digit
        n //= 10         # Remove last digit
    return total

# Test cases
print(sum_of_digits(1234))  # Output: 10 (1+2+3+4)
print(sum_of_digits(9876))  # Output: 30 (9+8+7+6)
