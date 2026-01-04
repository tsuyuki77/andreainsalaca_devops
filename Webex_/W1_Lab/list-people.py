import requests
import json
from token_auth import token

access_token = token

url = 'https://webexapis.com/v1/people'

headers = {
 'Authorization': 'Bearer {}'.format(access_token),
 'Content-Type': 'application/json'
}
params = {
 'email': 'andrea.insalaca@student.odisee.be'
}
res = requests.get(url, headers=headers, params=params)
print(json.dumps(res.json(), indent=4))