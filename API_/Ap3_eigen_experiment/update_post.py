import requests

post_id = input("Geef het post ID: ")

url = "https://jsonplaceholder.typicode.com/posts/" + post_id

title = input("Nieuwe titel: ")
body = input("Nieuwe inhoud: ")

data = {
    "id": post_id,
    "title": title,
    "body": body,
    "userId": 1
}

response = requests.put(url, json=data)

print("Status code:")
print(response.status_code)

print("Response:")
print(response.json())
