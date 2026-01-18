import requests

url = "https://postman-echo.com/post"

title = input("Geef een titel: ")
body = input("Geef de inhoud: ")

data = {
    "title": title,
    "body": body,
    "userId": "1"
}

response = requests.post(url, data=data)

print("\nStatus code:")
print(response.status_code)

print("\nResponse:")
print(response.json())