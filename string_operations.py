#concatination
str1 = "Hello"
str2 = "World"
result = str1 + " " + str2
print(result)  

# lowercase
str3 = "HELLO WORLD"
result = str3.lower()
print(result)

# uppercase
str4 = "hello world"
result = str4.upper()
print(result)

#strip
str5 = "   hello world   "
print(str5.strip())  # "hello world" (removes leading & trailing spaces)
print(str5.lstrip()) # "hello world  " (removes only left spaces)
print(str5.rstrip()) # "  hello world" (removes only right spaces)



#replace
str6 = "Hello World"
result = str6.replace("World", "Universe")
print(result)

#split
languages = "Python, C-sharp, JavaScript, TypeScript"
result = languages.split(", ")
print(result)

#find
backend = "Welcome to Python"
result = backend.find("Python")
print(result)

#count
countStrig = "Hello World"
result = countStrig.count("e")
print(result)

#format
name = "Mahesh"
language = 3
result = "My name is {} and I know {} programming languages"
print(result.format(name, language))

#join
languages = [ "Python", "C-sharp", "JavaScript", "Ruby" ]
result = ", ".join(languages)
print(result)

#length
lengthStr = "Hello World"
print(len(lengthStr))

#for in 
# day = "Sunday"
# for letter in day:
#     print(letter)

# / 
print("He said, \"Python is most popular language\" ")

# print as it is using r
print(r"c:\user\pwd")
print(r"python/nlanguage")

#in 
chaiName = "Masala Chai"    
print("Masala" in chaiName) 