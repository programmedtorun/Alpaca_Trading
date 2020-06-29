import json


secrets_filename = 'KEY_FILE.json'
api_keys = {}
with open(secrets_filename, 'r') as f:
    api_keys = json.loads(f.read())

print(api_keys['API_KEY_ID'])