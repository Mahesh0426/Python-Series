#Default parameter
#write a function that greats a user. If no name is provided. it should great with a default name 
def greet(name = "User"):
    return "hello, " + name + "!"


print(greet())
print(greet("Alice"))
