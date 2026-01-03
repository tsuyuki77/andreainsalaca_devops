import requests

post_id = input("Geef het post ID: ")

url = "https://jsonplaceholder.typicode.com/posts/" + post_id

response = requests.delete(url)

print("Status code:")
print(response.status_code)
print("Post verwijderd")
