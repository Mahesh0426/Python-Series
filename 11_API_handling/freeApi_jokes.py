
import requests

def fetch_random_jokes():
    url = "https://api.freeapi.app/api/v1/public/randomjokes"
    response = requests.get(url)
    data = response.json()

    if data["success"] and "data" in data:
        joke_data = data["data"]["data"]
        
        # loop through the first 5 jokes and return them
        jokes = []
        for i in range(5):
            if i < len(joke_data):  # Check if there are at least 5 jokes
                joke = joke_data[i]["content"]
                jokes.append(joke)
        return jokes
    else:
        raise Exception("Failed to fetch data from the API")

def main():
    try:
        jokes = fetch_random_jokes()
        for i, joke in enumerate(jokes, 1):
            print(f"Joke {i}: {joke}")
    except Exception as e:
        print(str(e))

if __name__ == "__main__":
    main()
