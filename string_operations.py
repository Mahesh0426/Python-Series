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

#title
str_title = "hello world from python"
result = str_title.title() # Convert to first letter of each word to uppercase
print(result) #Hello World From Python

#capitalize
str_capitalize = "hello rOCKETS"
result = str_capitalize.capitalize() # Convert first letter to uppercase and rest to lowercase
print(result) #Hello rockets

#strip | remove left and right spaces but not in middle 
str5 = "   hello world   "
print(str5.strip())  # "hello world" (removes leading & trailing spaces)
print(str5.lstrip()) # "hello world  " (removes only left spaces)
print(str5.rstrip()) # "  hello world" (removes only right spaces)

#replace | replace a part of string
str6 = "Hello World"
result = str6.replace("World", "Universe")
print(result) #Hello Universe

#2 replace  | replace spaces in middle
phone = "+61 456 789 123"
result = phone.replace(" ", "")
print(result) #+61456789123

#split - it split into list 
languages = "Python, C-sharp, JavaScript, TypeScript"
result = languages.split(", ")
print(result) #["Python", "C-sharp", "JavaScript", "TypeScript"]

#find
backend = "Welcome to Python"
result = backend.find("Python")
print(result) #7

#count
countStrig = "Hello World"
result = countStrig.count("e")
print(result) #2

#format
name = "Mahesh"
language = 3
result = "My name is {} and I know {} programming languages"
print(result.format(name, language)) #My name is Mahesh and I know 3 programming languages

#join
languages = [ "Python", "C-sharp", "JavaScript", "Ruby" ]
result = ", ".join(languages) # Join elements of a list with a comma and space
print(result) #Python, C-sharp, JavaScript, Ruby

#length
lengthStr = "Hello World"
print(len(lengthStr)) #11

#for in 
# day = "Sunday"
# for letter in day:
#     print(letter)

# / 
print("He said, \"Python is most popular language\" ")   #Using escape character for double quote (\")
print('It\'s a beautiful day')  #Using escape character for single quote (\')

# print as it is using r
print(r"c:\user\pwd") #prints c:\user\pwd
print(r"python/nlanguage") #python/nlanguage

#in 
chaiName = "Masala Chai"    
print("Masala" in chaiName) #True