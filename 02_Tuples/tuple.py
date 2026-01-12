tea_types = ("Black","Green","Oolang")
print(tea_types)
print(len(tea_types))

more_tea = ("Herbal", "Earl Gray")
all_tea = tea_types + more_tea
print(all_tea)

# if check
if "Green" in all_tea:
    print("Green tea is available.")


#nested tuple 
nested_tuple = (1, 2, (3, 4), [5, 6])
print(nested_tuple)

# tuple repetition
t = (1, 2, 3)
print(t * 3)

#Nested Unpacking - similar to destructuring in JS
person = ("Alice", 25, ("Python", "JavaScript"))
name, age, (lang1, lang2) = person

print(lang1)  # "Python"

#Unpacking with * (Rest Operator
numbers = (1, 2, 3, 4, 5)
first, *middle, last = numbers

print(first)  # 1
print(middle) # [2, 3, 4] (becomes a list)
print(last)   # 5
