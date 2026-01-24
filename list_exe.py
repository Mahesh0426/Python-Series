# You have a shopping cart:
# A user adds "eggs" at the end and wants "bread" replaced with "brown bread".
# Update the cart and print the final list.

cart = ["milk", "bread", "butter"]
cart.append("eggs")
cart[1] = "brown bread"
print(cart)  # Output: ["milk", "brown bread", "butter", "eggs"]



# 2. Student Marks Processing
# Remove the lowest mark, sort the list, and then print the highest mark.

marks = [56, 78, 90, 45, 89, 92]
marks.remove(min(marks))
marks.sort()
print(marks[-1])


# 3. Mobile App Notifications
# Your app should show the latest notification first.
# Reverse the list, then print the first notification.
notifications = ["Like", "Comment", "Follow", "Share"]
notifications.reverse()
print(notifications[0])


# 4. E-commerce Filter System
# Create a list of products cheaper than 500 using list comprehension.
prices = [120, 999, 450, 230, 799, 1500]
print([price for price in prices if price < 500])


# 5. Library Book Management
# Remove books with less than 200 pages, then sort and print the remaining books.
books = [
    ("Book A", 150),
    ("Book B", 220),
    ("Book C", 180),
    ("Book D", 300)
]

filtered_books = [book for book in books if book[1] >=200]
print(filtered_books)
filtered_books.sort()
print(filtered_books)



# 6. Todo App Task Update
# Your todo list:
# User finishes "Gym" and wants to add "Laundry" at index 1.
# Remove "Gym" and insert "Laundry".
tasks = ["Study", "Gym", "Shopping"]
tasks[1] = "Laundry"
print(tasks)

# or
tasks = ["Study", "Gym", "Shopping"]
tasks.remove("Gym")
tasks.insert(1, "Laundry")
print(tasks)



# 7. Social Media Followers Count
# You track followers every month:
# This month you gained 300.
# Append it, then print the total follower growth using sum().
followers = [100, 150, 200, 250]
followers.append(300)
print(followers)
# sum = 0
# for follower in followers:
#     sum += follower
# print(sum)

# or
print( "total followers is: ",sum(followers))


# 8. Booking System Seats
# Rows of booked seats:
# Someone cancels seat 5.
# Remove 5 and show the updated nested list.
seats = [
    [1, 2, 3],
    [4, 5, 6]
]
seats[1].pop(1)
print(seats)



# 9. Cleaning Duplicate Records
# A list has duplicate customer IDs:
# Create a new list without duplicates (without using set).
ids = [101, 103, 101, 104, 103, 105]
unique_ids = []
[unique_ids.append(x) for x in ids if x not in unique_ids]
print(unique_ids)

# or
unique_ids = []
for items in ids:
    if items not in unique_ids:
        unique_ids.append(items)
print(unique_ids)
 


# 9. Music Playlist Update
# User wants "song4" added, and "song2" moved to the end.
# Solve using pop() and append().
playlist = ["song1", "song2", "song3"]
playlist.append("song4")
print(playlist)
song = playlist.pop(1)
playlist.append(song)
print(playlist)


# 10. Weather App Temperatures
# Temperatures for the week:
# Create a list of temperatures above 25 and print how many days were hotter.
temps = [22, 25, 28, 24, 26, 29, 27]
hot_days = [temp for temp in temps if temp > 25]
print(hot_days)
print("Number of hotter days: ",len(hot_days))




# 11. Restaurant Menu Manager
# Owner adds "salad" at index 2 and removes "fries".
# Print the updated men
menu = ["pizza", "burger", "pasta", "fries"]
menu.insert(2 ,"salads")
print(menu)
menu.remove("fries")
print(menu)


# 12. Student Attendance Tracker
# Daily attendance count:
# Reverse the list and print the last two values.

attendance = [45, 48, 50, 47, 49]
attendance.reverse()
print(attendance)
print(attendance[-2:])


ratings = [4, 5, 3, 4, 5, 2, 5]
rating_above_4 = [rate for rate in ratings if rate >= 4]
print(rating_above_4)
print(rating_above_4.count(5))
