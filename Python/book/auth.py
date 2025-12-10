import requests

APIHOST = "http://library.demo.local"
LOGIN = "cisco"
PASSWORD = "Cisco123!"

def getAuthToken():
    r = requests.post(f"{APIHOST}/api/v1/loginViaBasic", auth=(LOGIN, PASSWORD))
    r.raise_for_status()
    return r.json()['token']

if __name__ == "__main__":
    print(getAuthToken())