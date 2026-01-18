import requests

url = "https://postman-echo.com/put"

post_id = input("Geef een post ID: ")
title = input("Nieuwe titel: ")
body = input("Nieuwe inhoud: ")

data = {
    "postId": post_id,
    "title": title,
    "body": body
}

response = requests.put(url, data=data)

print("\nStatus code:")
print(response.status_code)

print("\nResponse:")
print(response.json())