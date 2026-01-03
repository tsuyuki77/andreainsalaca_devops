import requests

url = "https://dummyjson.com/posts/add"

title = input("Geef een titel: ")
body = input("Geef de inhoud (body): ")

data = {
    "title": title,
    "body": body,
    "userId": 1
}

response = requests.post(url, json=data)

print("\nStatus code:")
print(response.status_code)

print("\nResponse:")
print(response.json())
