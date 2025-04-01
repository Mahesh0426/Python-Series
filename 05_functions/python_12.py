# Create a recursive function to calculate the factorial of a number
def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)
    
# Test cases
print(factorial(5))  # Output: 120 (5*4*3*2*1)