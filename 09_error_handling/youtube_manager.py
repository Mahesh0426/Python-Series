# This is a simple Youtube video manager app that allows you to manage your favourite videos.
# It allows you to add, update, delete and list your favourite videos.
# It uses a JSON file to store the data, so you can easily access it later.

import json
# function to load data from json file
def load_data():
    try:
        with open('youtube.txt','r') as file:
           test = json.load(file)
        #    print(type (test))
           return test
        #    return json.load(file)

    except FileNotFoundError:
        return[]

# function to save data to json file
def save_data_helper(videos):
    with open('youtube.txt','w')as file:
        json.dump(videos, file)
    
# function to list all videos
def list_all_videos(videos):
    print("\n")
    print("*" * 70)
    for index, video in enumerate(videos,start=1):
        print(f"{index}. {video['name']}, Duration: {video['time']}")
        # print(f"{index}. {video.get('name', 'Unknown')}, Duration: {video.get('time', 'N/A')}")
    print("\n")
    print("*" * 70)
    # for vid in videos:
    #     print(f"{vid}.")

# function to add video
def add_video(videos):
    name = input("Enter the video title: ")
    time = input("Enter the video time: ")
    videos.append({"name":name, "time":time})
    save_data_helper(videos)

# function to update video
def update_video(videos):
    list_all_videos(videos)
    index = int(input("Enter the video number to update: "))
    if 1 <= index <= len(videos):
        name = input("Enter the new video title: ")
        time = input("Enter the new video time: ")
        videos[index -1] = {"name":name,"time":time }
        save_data_helper(videos)
    else:
        print("Invalid video number")

# function to delete video
def delete_video(videos):
    list_all_videos(videos)
    index = int(input("Enter the video number to delete: "))

    if 1 <= index <= len(videos):
        del videos[index - 1]
        save_data_helper(videos)
    else:
        print("Invalid video number")

# main function
def main():
    videos = load_data()


    while True:
        print("\n Youtube Manager | choose an option")
        print(" 1.List all favourite videos")
        print(" 2.Add a youtube video")
        print(" 3.Update a youtube video details")
        print(" 4.delete a youtube video details")
        print(" 5.Exit the app")
        choice = input("enter your choice: ")
        # print(videos)

        match choice:
            case '1':
                list_all_videos(videos)
            case '2':
                add_video(videos)
            case '3':
                update_video(videos)
            case '4':
                delete_video(videos)
            case '5':
                break
            case _:
                print("Invalid choice, please try again")

if __name__ == "__main__":
    main()


    for index, movie in  enumerate(movies, start=1):
        print(f"{index}. {movie['name']}")
        