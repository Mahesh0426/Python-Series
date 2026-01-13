#Write a program that takes two strings:
# Join them with a space and print the full name.

firstName = "Mahesh"
lastName = "Kunwar"
fullName = firstName + " " + lastName
print(fullName)
print(f"{firstName} {lastName}") # Using f-string for string interpolation
print("{} {}".format(firstName, lastName)) # Using format method
print(firstName, lastName) # Using comma in print function

#lowrcase
text = "PYTHON IS FUN"
print(text.lower())


msg = "    Welcome to Python  "
print(msg.strip())  # Removes leading and trailing whitespace
print(msg.lstrip()) # Removes leading whitespace
print(msg.rstrip()) # Removes trailing whitespace

line = "I love JavaScript"
print(line.replace("JavaScript","Pyhton"))

programming_languages = "Python, Java, C++, JavaScript"
print(programming_languages.split(","))
print(programming_languages.join("|"))

title = "Welcome to Masala Chai House"
print(title.find("o"))
count = title.count("o")
print(f"Number of 'o' in the title is: {count}")


items = ["Keyboard", "Mouse", "Monitor"]
print(" | ".join(items))

msg = "i am learning Python"
print(msg.capitalize())
print(msg.title())
print(len(msg))
print(msg.startswith("i am"))
print(msg.endswith("Python"))