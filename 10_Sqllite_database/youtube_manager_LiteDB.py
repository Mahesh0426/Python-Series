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

def list_videos():
    cursor.execute("SELECT * FROM videos")
    for row in cursor.fetchall():
        print(row)

def  add_video(name,time):
    cursor.execute("INSERT INTO videos(name , time) VALUES(?, ?)", (name, time))
    connection.commit()
    

def update_video(video_id, new_name, new_time):
    cursor.execute("UPDATE videos SET name = ?, time = ? WHERE id = ?", (new_name, new_time, video_id))
    connection.commit()

def delete_video(video_id):
    cursor.execute("DELETE FROM videos WHERE id = ?", (video_id,))
    connection.commit()

      

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
        elif choice == '2':
            name = input("Enter video title: ")
            time = input("Enter video time: ")
            add_video(name, time)
        elif choice == '3':
            video_id =  input("Enter video id to update: ")
            name = input("Enter video title to update: ")
            time = input("Enter video time to update: ")
            update_video(video_id, name, time)
        elif choice == '4':
            video_id = input("Enter video id to delete:")
            delete_video(video_id)
        elif choice == '5':
            break
        else:
            print("Invalid choice.")
            
    connection.close()

        
        
if __name__ == "__main__":
    main()