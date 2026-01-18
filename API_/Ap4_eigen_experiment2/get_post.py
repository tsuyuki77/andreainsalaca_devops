import requests

url = "https://postman-echo.com/get"

post_id = input("Geef een post ID: ")

params = {
    "postId": post_id
}

response = requests.get(url, params=params)

print("Status code:")
print(response.status_code)

print("\nResponse:")
print(response.json())
