import requests

post_id = input("Geef het post ID dat je wil aanpassen: ")

url = "https://dummyjson.com/posts/" + post_id

title = input("Nieuwe titel: ")
body = input("Nieuwe inhoud (body): ")

data = {
    "title": title,
    "body": body
}

response = requests.put(url, json=data)

print("\nStatus code:")
print(response.status_code)

print("\nResponse:")
print(response.json())
