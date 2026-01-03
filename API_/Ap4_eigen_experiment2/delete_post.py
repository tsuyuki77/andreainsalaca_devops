import requests

post_id = input("Geef het post ID dat je wil verwijderen: ")

url = "https://dummyjson.com/posts/" + post_id

response = requests.delete(url)

print("\nStatus code:")
print(response.status_code)

print("\nResponse:")
print(response.json())
