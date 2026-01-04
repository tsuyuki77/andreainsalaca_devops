import requests 
from token_auth import token, room

access_token = token
room_id = room 
person_email = 'ayoub.boussata@student.odisee.be' 
url = 'https://webexapis.com/v1/memberships' 
headers = { 
'Authorization': 'Bearer {}'.format(access_token), 
'Content-Type': 'application/json'} 
params = {'roomId': room_id, 'personEmail': person_email} 
res = requests.post(url, headers=headers, json=params) 
print(res.json())