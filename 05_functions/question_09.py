#kwargs
#create a function that accepts  any number of keyword arguments and prints them in the format  key:value

def print_kwargs(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}:{value}")

print_kwargs(name="Bikash", age=22, city="Sydney")
print_kwargs(name="Mahesh", occupation=" soft.Engineer")
print_kwargs(country="Australia", language="English")
print_kwargs(name="Ramesh", age=25, city="Newtown", hobby="cricket")


#  Pass Keyword Arguments to Another Function
def greet(**kwargs):
    if "name" in kwargs:
        print(f"Hello, {kwargs['name']}!")
    else:
        print("Hello, Guest!")

greet(name="Mahesh")
greet()

# Combine with *args
def display_info(*args, **kwargs):
    print("Positional arguments:", args)
    print("Keyword arguments:", kwargs)

display_info(1, 2, 3, name="Mahesh", age=30)
