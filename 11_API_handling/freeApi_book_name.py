import requests

def fetch_random_book():
    url = "https://api.freeapi.app/api/v1/public/books/book/random"
    response = requests.get(url)
    data = response.json()

    if data["success"] and "data" in data:
        book_data = data["data"] 
        book_title = book_data["volumeInfo"]["title"]
        book_author = book_data ["volumeInfo"]["authors"]
        book_description = book_data ["volumeInfo"]["description"]
        book_publisher = book_data ["volumeInfo"]["publisher"]
        return book_title, book_author, book_description, book_publisher
    else:
        raise Exception("Failed to fetch data from the API")
    

def main():
    try:
        book_title, book_author, book_description, book_publisher = fetch_random_book()
        print(f"Book Title: {book_title}")
        print(f"Book Author: {book_author}")
        print(f"Book Description: {book_description}")
        print(f"Book Publisher: {book_publisher}")
    except Exception as e:
        print(str(e))
        
if __name__ == "__main__":
    main()

    
