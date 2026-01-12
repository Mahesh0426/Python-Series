from pymongo import MongoClient
from bson import ObjectId


client = MongoClient("mongodb+srv://youtubepy:youtubepy@cluster0.2gi2uk6.mongodb.net/", tlsAllowInvalidCertificates=True)

db = client["ytmanager"]
video_collection = db["videos"]
# print(video_collection)
def list_videos():
    for video in video_collection.find():
        print(f"ID: {video["_id"]}, Name: {video["name"]}, Time: {video["time"]}")
    

def add_video(name, time):
    video_collection.insert_one({"name":name, "time":time})

def update_video(newname, newtime, video_id):
    video_collection.update_one({"_id":ObjectId(video_id)},{"$set":{"name":newname,"time":newtime}})

def delete_video(video_id):
  video_collection.delete_one({"_id":ObjectId(video_id)})


def main():
    while True:
        print("\n youtube Manager App")
        print("1. List all Videos")
        print("2. add a Video ")
        print("3. update a Video ")
        print("4. delete a Video ")
        print("5. exist a app ")

        choice = input("Enter your choice: ")
        if choice == "1":
            list_videos()
        elif choice == "2":
            name = input("Enter video name: ")
            time = input("Enter video time: ")
            add_video(name, time)
        elif choice == "3":
            video_id = input("Enter  video ID: ")
            name = input("Enter updated video name: ")
            time = input("Enter updated video time: ")
            update_video(name, time, video_id)
        elif choice == "4":
            video_id = input("Enter video ID to delete: ")
            delete_video(video_id)
        elif choice == "5":
            break
        else:
            print("Invalid choice. Please try again.")
            
         
            

if __name__ == "__main__":
    main()