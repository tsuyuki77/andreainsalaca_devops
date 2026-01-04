import requests 
from token_auth import token, room

access_token = token 
room_id = room 
url = 'https://webexapis.com/v1/memberships' 
headers = { 
'Authorization': 'Bearer {}'.format(access_token), 
'Content-Type': 'application/json' 
} 
params = {'roomId': room_id} 
res = requests.get(url, headers=headers, params=params) 
print(res.json())