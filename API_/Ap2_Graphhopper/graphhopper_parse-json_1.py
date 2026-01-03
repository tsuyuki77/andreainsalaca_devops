import requests 
import urllib.parse

geocode_url = "https://graphhopper.com/api/1/geocode?" 
route_url = "https://graphhopper.com/api/1/route?" 

loc1 = "Rome, Italy" 
loc2 = "Baltimore, Maryland"

key = "a3c0ad04-6d1f-4de5-889d-97e8b1b15be1"

url = geocode_url + urllib.parse.urlencode({"q":loc1, "limit": "1", "key":key}) 

replydata = requests.get(url) 
json_data = replydata.json() 
json_status = replydata.status_code 
#print(json_data)

json_status = replydata.status_code 