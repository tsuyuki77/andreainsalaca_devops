import requests

url = "https://jsonplaceholder.typicode.com/posts"

title = input("Geef een titel: ")
body = input("Geef de inhoud (body): ")

data = {
    "title": title,
    "body": body,
    "userId": 1
}

response = requests.post(url, json=data)

print("Status code:")
print(response.status_code)

print("Response:")
print(response.json())
