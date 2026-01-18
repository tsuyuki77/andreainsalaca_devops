import requests

url = "https://postman-echo.com/delete"

post_id = input("Geef het post ID dat je wil verwijderen: ")

data = {
    "postId": post_id
}

response = requests.delete(url, data=data)

print("\nStatus code:")
print(response.status_code)

print("\nResponse:")
print(response.json())
