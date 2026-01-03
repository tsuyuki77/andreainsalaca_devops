import requests

url = "https://jsonplaceholder.typicode.com/posts"

response = requests.get(url)

print("Status code:")
print(response.status_code)

print(response.json())
