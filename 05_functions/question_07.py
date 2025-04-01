# Write a function that takes variable number of arguments and returns their sum.
def summ_all(*args):
    return sum(args)

print(summ_all(1, 2, 3, 4, 5))
print(summ_all(10, 20, 30))
print(summ_all(100, 200))