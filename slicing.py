# Define the string
num_list = "0123456789"

# variable[start:stop:step]

# Slicing examples
print("Full string:", num_list[:])  # '0123456789'
print("From index 3 to end:", num_list[3:])  # '3456789'
print("From start to index 3 (exclusive):", num_list[:3])  # '012'
print("Every 3nd character from index 0 to 7:", num_list[0:7:3])  # '036'


# 1. Slice from index 2 to the end
print(num_list[2:]) #23456789

#3. Slice characters from index 4 to 8
print(num_list[4:8]) #4567  

#4. Get every 2nd character from the full string
print(num_list[::2]) #02468

#5. Slice the first half of the string
print(num_list[:5]) #01234

#6. Slice the last 4 digits using negative indexing
print(num_list[-4:]) #6789

#7. Reverse the entire string
print(num_list[::-1]) #9876543210

# 8. Reverse only the digits from index 2 to index 7
print(num_list[6:1:-1]) #65432

#9. Get only the even index digits
print(num_list[::2]) #02468

#10. Get only the odd index digits
print(num_list[1::2]) #13579

#11. Use slicing to get "579"
print(num_list[5::2]) #579


s = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
#1. Extract every 4th character from the full string
print(s[::4]) #048CGMSY

# 2. Slice the string so you get: "89ABC"
print(s[8:13]) #89ABC

# 3. Reverse only the letters, but keep the digits as they are
num = s[:10]
letters = s[10:]
print(num + " " + letters[::-1]) #0123456789 ZYXWVUTSRQPONMLKJIHGFEDCBA

# 4. Extract "2468ACEG"
print(s[2:18:2]) #2468ACEG

# 5. Extract all letters using slicing, no indexes, no length function
print(s[10:]) #ABCDEFGHIJKLMNOPQRSTUVWXYZ

# 6. Reverse only odd-indexed digits, give "97531"
print(s[1:10:2][::-1]) #97531

# 7. Return empty string using slicing that "looks valid"
print(s[5:2:1])

# 9. Last 10 characters reversed
print(s[-10:][::-1])

# 12. Reverse only the middle 10 characters
print(s[:13] + s[13:23][::-1] + s[23:]
)