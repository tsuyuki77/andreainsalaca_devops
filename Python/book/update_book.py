import requests
import json
from auth import getAuthToken

APIHOST = "http://library.demo.local"
BOOK_ID = 4

def update_book(apiKey):
    updated_book = {
        "title": "Aangepaste titel",
        "author": "Nog steeds jij"
    }
    r = requests.put(
        f"{APIHOST}/api/v1/books/{BOOK_ID}",
        headers={"Content-Type": "application/json", "X-API-Key": apiKey},
        data=json.dumps(updated_book)
    )
    r.raise_for_status()
    print("Boek aangepast!")

if __name__ == "__main__":
    token = getAuthToken()
    update_book(token)
