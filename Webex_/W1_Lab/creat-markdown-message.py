import requests 
from token_auth import token, room

access_token = token
room_id = room
message = 'Hello **DevNet Associates**!!' 
url = 'https://webexapis.com/v1/messages' 
headers = { 
'Authorization': 'Bearer {}'.format(access_token), 
'Content-Type': 'application/json' 
} 
params = {'roomId': room_id, 'markdown': message} 
res = requests.post(url, headers=headers, json=params) 
print(res.json())