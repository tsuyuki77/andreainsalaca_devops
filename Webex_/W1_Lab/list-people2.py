import requests
import json
from token_auth import token

access_token = token
person_id = 'Y2lzY29zcGFyazovL3VzL1BFT1BMRS84MGNiZWY1OC1jZjkxLTRmODUtOGJjMC1hYzNhYTcxY2FmYjI'
url = 'https://webexapis.com/v1/people/{}'.format(person_id)

headers = {
 'Authorization': 'Bearer {}'.format(access_token),
 'Content-Type': 'application/json'
}


res = requests.get(url, headers=headers)
print(json.dumps(res.json(), indent=4))