import requests
import json

APIHOST = "http://library.demo.local"

def get_books():
    r = requests.get(f"{APIHOST}/api/v1/books")
    r.raise_for_status()
    print(json.dumps(r.json(), indent=4))

if __name__ == "__main__":
    get_books()
