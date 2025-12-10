import requests
import json
from auth import getAuthToken

APIHOST = "http://library.demo.local"

def add_book(apiKey):
    book = {
        "id": 4,
        "title": "Nieuw Boek",
        "author": "Jijzelf"
    }
    r = requests.post(
        f"{APIHOST}/api/v1/books",
        headers={"Content-Type": "application/json", "X-API-Key": apiKey},
        data=json.dumps(book)
    )
    r.raise_for_status()
    print("Nieuw boek toegevoegd!")

if __name__ == "__main__":
    token = getAuthToken()
    add_book(token)
