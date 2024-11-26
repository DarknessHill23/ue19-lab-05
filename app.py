import requests


def get_joke():
    url = "https://official-joke-api.appspot.com/random_joke"

    headers = {"Content-Type": "application/json"}

    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()
        joke = response.json()
        print(f"{joke['setup']} - {joke['punchline']}")
    except requests.exceptions.RequestException as e:
        print(f"An error occurred: {e}")


if __name__ == "__main__":
    get_joke()
