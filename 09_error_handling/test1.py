# movies = ["Inception", "Interstellar", "The Matrix", "Spirited Away"]

# movie_dict_list = []

# for index, movie in enumerate(movies, start=1):
#     movie_dict_list.append({"id": index, "title": movie})

# print(movie_dict_list)

movies = []

print("🎬 Enter your favorite movies! Type 'exit' at any time to stop.\n")

while len(movies) < 3:
    title = input("Enter movie title: ")
    if title.lower() == "exit":
        break

    duration = input("Enter movie duration (e.g., 2h 28m): ")
    if duration.lower() == "exit":
        break

    movies.append((title, duration))

# Print nicely
print("\n🍿 Your Favorite Movies:")
for index, (title, duration) in enumerate(movies, start=1):
    print(f"{index}. {title} ({duration})")
