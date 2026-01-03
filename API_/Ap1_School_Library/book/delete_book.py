import requests
from auth import getAuthToken

APIHOST = "http://library.demo.local"
BOOK_ID = 4

def delete_book(apiKey):
    r = requests.delete(
        f"{APIHOST}/api/v1/books/{BOOK_ID}",
        headers={"X-API-Key": apiKey}
    )
    r.raise_for_status()
    print("Boek verwijderd!")

if __name__ == "__main__":
    token = getAuthToken()
    delete_book(token)
