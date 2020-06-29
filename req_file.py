import json
import requests



secrets_filename = 'KEY_FILE.json'
api_keys = {}
with open(secrets_filename, 'r') as f:
    api_keys = json.loads(f.read())

# print(api_keys['API_KEY_ID'])

BASE_URL = "https://paper-api.alpaca.markets"
ACCOUNT_URL = "{}/v2/account".format(BASE_URL)

r = requests.get(ACCOUNT_URL, headers=
                {"APCA-API-KEY-ID": api_keys['API_KEY_ID'],
                "APCA-API-SECRET-KEY": api_keys['SECRET_KEY']}
                 )

print(r.content)

