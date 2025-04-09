import sqlite3

connection = sqlite3.connect('youtube_manager.db')

cursor = connection.cursor()

# Create a table to store video information
cursor.execute(''' 
CREATE TABLE IF NOT EXISTS videos (
               id INTEGER PRIMARY KEY,
               name TEXT NOT NULL,
               time TEXT NOT NULL
               )
''')

list_videos():


      

def main():
    while True:
        print(f"\n Youtube  Manager app with DB")
        print(f"1. List video")
        print(f"2. Add video")
        print(f"3. update video")
        print(f"4. delete video")
        print(f"5. Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            list_videos()
        
if __name__ == "__main__":
    main()