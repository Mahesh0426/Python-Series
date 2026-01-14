# 1.Clean and Format User Input
raw_name = "   maHeSh kunWar   "
clean_name = raw_name.strip()
print(clean_name.title())

# 2. Extract Domain From Email
email = "  student123@university.edu  "
clean_email = email.strip()
print(clean_email.split("@")[1]) # this extracts the word after @

# 3. Count Words in a Sentence
sentence = "Python is great and Python is powerful"
word_to_count = "Python"
count = sentence.count(word_to_count)
print(count)
# print(sentence.split())  
print(len(sentence.split()))  # total words in the sentence

#4. Mask a Phone Number | Replace the first 8 digits with *
phone = "  +61 456 789 123  "
masked_phone = phone.strip().replace(" ", "")  # Remove spaces
print(masked_phone.replace(masked_phone[:9], "********"))

# 5. Create a Slug for URLs
title = "  Learn Python Programming in 2025  "
slug = title.lower().strip().replace(" ", "-")
print(slug)

#6 Merge a List to Create a Sentence
words = ["python", "makes", "coding", "fun"]
sentence = " ".join(words).upper()
print(sentence)


# 7. Check If a Word Exists
text = "Welcome to the Python Developer Community"
word_to_check = "Developer"
print(word_to_check in text)

# 8. Reverse Each Word  | output: I evol gninrael nohtyP | reverse each word
line = "I love learning Python"
# print(" ".join(word[::-1] for word in line.split()))
words = line.split()
print(words)
reversed_words = [word[::-1] for word in words]
print(reversed_words)
result = " ".join(reversed_words)
print(result)

#9. Find and Replace Multiple Words
msg = "I like Java and Java is popular"
replace_words = msg.replace("Java", "Python")
print(replace_words)
print(replace_words.count("Python"))

# 10. Format Billing Information
name = "Mahesh"
product = "Laptop"
price = 1450.75
result = f"{name} purchased {product} for ${price:.2f}"
print(result)


#11. Combine Three Strings Smartly
first = "Hello"
second = "World"
third = "from Python"
result = " , ".join([first, second, third])
print(result)

