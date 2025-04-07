file = open('youtube.txt', "w")

# error handling 1
try:
    file.write("Hello World")
finally:
    file.close()


# error handling 2
with open('youtube.txt',"w") as file:
    file.write("Hello World")