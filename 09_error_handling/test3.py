movies = [
    ("Inception", "2h 28m"),
    ("Interstellar", "2h 49m"),
    ("The Matrix", "2h 16m"),
    ("Spirited Away", "2h 5m")
]

list_of_movies = []

for index,(title, time) in enumerate(movies, start=1):
    print(f"{index}. {title}  ({time})")
#     list_of_movies.append({"id": index, "title": title, "time": time})
# print(list_of_movies)


