# # Cache return value
# # Implement a decorator that cache the return values of a function, so that when it's called with the same arguments, 
# # the cached value is returned instead of re-executing the function again.
# import time

# def cache(func):
#     cache_value = {}
#     print(f"Cache value: {cache_value}")

#     def wrapper(*args):
#         if args in cache_value:
#             return cache_value[args]
#         result = func(*args)
#         cache_value[args]= result
#         return result
#         pass
#     return wrapper


# @cache
# def long_running_func(a,b):
#     time.sleep(4)
#     return a + b

# print(long_running_func(1,2))
# print(long_running_func(1,2))
# print(long_running_func(7,2))

def say_hello(name):
    return f"Hello, {name}!"

# Assign the function to a variable
greet = say_hello
print(greet("Alice"))