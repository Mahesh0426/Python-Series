# 1. Age group Categorization
# Classify a person's age group: Child(<13), Teenager(13-19), Adult(20-59), Senior(60+)

# age = input("Enter a age: ")
# age_in_Int = int(age)

# if age_in_Int < 13:
#     print("Age group is : Child")
# elif age_in_Int < 20:
#     print("Age group is : Teenager")
# elif age_in_Int < 60:
#     print("Age group is : Adult")
# else:
#     print("Age group is : Senior")


 #2 movie Ticketing Pricing
    # Calculate the ticket price based on the age group: $12 for adults(18 and over),
    #  $8 for Children, $2 discount for everyone on wednesday 

# age = input("Enter your Age: ")
# age_in_int = int(age)
# day = input("Enter your booking Day: ")

age_in_int = 28
day = "Wednesday"

price = 12 if age_in_int >=18 else 8
if day == "Wednesday":
    price -= 2
print("ticket price for you is $",price)

#3 Assign a letter grade based on a student's score : A(90-100), B(80-89), C(70-79), D(60-69),F(below 60)
score =  90
if score >=101:
    print("Invalid score. Please enter a score between 0 and 100.")
    exit()

if score >=90:
    grade = "A"
elif score >=80:
    grade = "B"
elif score >=70:
    grade = "C"
elif score >=60:
    grade = "D"
else:
    grade = "F"

print("The student's grade is :", grade)

#4 Determine if a fruit is ripe, overripe, or unripe based on its color.(eg. Banana :Green - unripe, Yellow - Ripe, Brown-Overripe)
fruit= "Banana"
fruit_color = "Green"

if fruit == "Banana":
    if fruit_color == "Green":
         print(fruit, "is Unripe")
    elif fruit_color == "Yellow":
         print(fruit, "is Ripe")
    elif fruit_color == "Brown":
         print(fruit, "is Overripe")

#5  Suggest an activity based on the weather(eg.Sunny - Go for a walk, Rainy- Read a book, Snowy-Build a snowman)

weather="Sunny"

if weather == "Sunny":
   activity = "Go for a Walk"
elif weather == "Rainy":
    activity = "Read a book"
elif weather == "Snowy":
    activity = "Build a snowman"

print(activity)

#6 Choose a mode of transporation based on the distance (eg. <3 km Walk, 3-15 km: Bike, >15km:Car)
distance = 19

if distance < 3:
    transport = "walk"
elif distance <=15:
    transport = "bike"
else:
    transport = "car"

print("The most suitable mode of transportation for you is :", transport)

#7 Customize a coffe order: small, medium or large with an option for Extra shot of espresso

order_size = "large"
extra_shot = False

if extra_shot:
    coffee = order_size + " coffee with an extra shot"
else:
    coffee = order_size + " coffee"

print("Your customized coffee order is :", coffee)

#8 Check if a password is "Weak, "Medium", or "Strong". Criteria: <6 char - week, 6-10 char - meduim, >10 char - Strong
password = "bikash@133"

if len(password) < 6:
    password_strength = "weak"

elif len(password) <10:
    password_strength = "medium"
else:
   password_strength = "Strong"

print("Password strength is :", password_strength)

#9 Determine if a year is a leap year .(Leap years are divisible by 4, but not by 100 unless also divisible by 400)

year = 2023

if (year % 400 == 0) or (year % 4 == 0 and year % 100 !=0):
    print(year, "is a leap year" )
else:
    print(year,"is not leap year ")

#10 Recommend a type of pet food based on the pet's species and age (eg. Dog:<2 year- Puppy food,Cat:>5 years - Senior cat food)
 
pet_species = "cat"  
pet_age = 7         

recommendation = "Standard Adult Food"

if pet_species.lower() == "dog":
    if pet_age < 2:
        recommendation = "Puppy Food"
    elif pet_age > 7:
        recommendation = "Senior Dog Food"
elif pet_species.lower() == "cat":
    if pet_age < 1:
        recommendation = "Kitten Food"
    elif pet_age > 5:
        recommendation = "Senior Cat Food"

print(f"Recommended food for your {pet_species} (age {pet_age}): {recommendation}")