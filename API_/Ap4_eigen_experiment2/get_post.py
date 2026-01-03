import requests

url = "https://dummyjson.com/posts"

response = requests.get(url)

print("Status code:")
print(response.status_code)

print("\nPosts:")
print(response.json())
