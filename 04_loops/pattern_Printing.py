#1 Right-Angled Triangle
n = 5
for i in range(1, n+1):
    print("*" * i)
    

#2 Inverted Right-Angled Triangle
n = 5
for i in range(n ,0, -1):
    print("*" * i)

#3 Hollow Square
n = 5
for i in range(n):
    for j in range(n):
        if i == 0 or i == n-1 or j == 0 or j == n-1:
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()

#4 Pyramid Pattern
n = 5
for i in range(1, n + 1):
    print(" " * (n - i) + "*" * (2 * i - 1))


#6  Number Triangle
n = 5
for i in range(1, n + 1):
    for j in range(1, i + 1):
        print(j, end=" ")
    print()

#5  reverse pyramid

n = 5
for i in range(n, 0, -1):  # Reverse loop (5 to 1)
    print(" " * (n - i) + "*" * (2 * i - 1))



