import requests
import os
import json

url = "https://apidojo-yahoo-finance-v1.p.rapidapi.com/auto-complete"

querystring = {"q":"tesla","region":"US"}

k_file = 'RAPID_KEY.json'
with open(k_file, 'r') as f:
    key_dict = json.loads(f.read())
os.environ["RAPID_API_KEY"] = key_dict['API_KEY']
os.environ["RAPID_API_HOST"] = "apidojo-yahoo-finance-v1.p.rapidapi.com"

headers = {
    'x-rapidapi-key': key_dict['API_KEY'],
    'x-rapidapi-host': os.getenv("RAPID_API_HOST")
    }

response = requests.request("GET", url, headers=headers, params=querystring)

print(response.text)