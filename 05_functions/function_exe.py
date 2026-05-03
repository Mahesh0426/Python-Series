#1. Write a function that counts how many vowels are in a string.
def count_vowels(string):
    vowels = "aeiou"
    count = 0
    for char in string:
        if char in vowels:
            count +=1
    return count
print(count_vowels("maheshkunwar"))

# 2.Write a function that takes a list and returns a new list without duplicates.
def remove_duplicates(list:list):
    new_list=[]
    for item in list:
        if item not in new_list:
            new_list.append(item)
    return new_list

# print(remove_duplicates([1,2,2,3,4,4,5]))

# 3.Write a function that checks if a given word is a palindrome.
def is_palindrome(word:str):
    word = word.lower()
    return word == word[::-1]

# print(is_palindrome("madam"))

# 4.Write a function that takes a list of numbers and returns the sum of only the even numbers.
def even_sum(num_list:list):
    total = 0
    for num in num_list:
        if num % 2 == 0:
            total +=num
    return total

# print(even_sum([1,2,3,4,5,6]))

# 6.Write a function that takes a dictionary of student names and marks and 
# returns the name of the student with the highest mark.
def student_details(stud_dict):
     return max(stud_dict, key=stud_dict.get)

stud_dict = {
    "Alice": 88,
    "Bob": 95,
    "Charlie": 72,
    "Diana": 95
}

print(student_details(stud_dict))

def top_student(students: dict):
    if not students:
        return None

    highest_mark = max(students.values())
    top_students = [name for name, mark in students.items() if mark == highest_mark]

    if len(top_students) > 1:
        return f"Tie between: {', '.join(top_students)} with {highest_mark} marks"
    
    return f"{top_students[0]} with {highest_mark} marks"

students = {
    "Alice": 88,
    "Bob": 95,
    "Charlie": 72,
    "Diana": 95
}

print(top_student(students))  # Tie between: Bob, Diana with 95 marks

    

    





    

    
    
    


    

    
