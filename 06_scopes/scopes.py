userName= "chaiaurcode"


def func():
    userName= "chai"
    print(userName)


print(userName)
func()

# 2
x= 99
def func2(y):
    z= x+ y
    return z

result = func2(1)
print(result)

#3
# def func3():
#     global x
#     x = 12

# func3()
# print(x) 

#4
def func4():
    x = 88   # it will take global x 99 if there is no x declare like x = 88
    def func5():
        print(x)
    # return func5
    func5()
# result = func4()
func4()
# result()  # this will print 88

#5  clouser function
def outer(num):
    def inner(x):
        return x ** num
    return inner

square = outer(2)
cube = outer(3)

# print(square)
# print(cube)

print(square(3))
print(cube(3))

#6 scope 
# Global scope
x = 1


def foo():
    # global x
    x = 11
    y = 12
    print(f"foo sees x equal to {x}")
    print(f"foo sees y equal to {y}")

def bar():
    print(f"bar sees x equal to {x}")  # it use global x 
    # print(f"bar sees y equal to {y}")  # This will raise an error because y is not defined in this scope

foo()
bar()
print(f"global sees x equal to {x}")

