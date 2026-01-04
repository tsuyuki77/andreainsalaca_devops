import requests 
from token_auth import token, room
access_token = token
room_id = room 

url = 'https://webexapis.com/v1/rooms/{}/meetingInfo'.format(room_id) 
headers = { 
'Authorization': 'Bearer {}'.format(access_token), 
'Content-Type': 'application/json' 
} 
res = requests.get(url, headers=headers) 
print(res.json())