import json
import requests
import os
import alpaca_trade_api as tradeapi
#sys.path.insert(0, "/Library/Frameworks/Python.framework/Versions/3.7/lib/python3.7/site-packages")
# Note: you need to install pytz for alpaca_trade_api to work on your system `pip3 install pytz` if it already exists then you may
# have to manually update it by deleting the pytz.<blah>.dist-info and installing again.

#  ------------- Setting Key, Secret, Base URL -------------
secrets_filename = 'KEY_FILE.json'
api_keys = {}
with open(secrets_filename, 'r') as f:
    api_keys = json.loads(f.read())
os.environ["APCA_API_KEY_ID"] = api_keys['API_KEY_ID']
os.environ["APCA_API_SECRET_KEY"] = api_keys['SECRET_KEY']
os.environ["APCA_API_BASE_URL"] = "https://paper-api.alpaca.markets"


#  ------------- Using requests python lib -------------
BASE_URL = "https://paper-api.alpaca.markets"
ACCOUNT_URL = "{}/v2/account".format(BASE_URL)

r = requests.get(ACCOUNT_URL, headers=
                {"APCA-API-KEY-ID": api_keys['API_KEY_ID'],
                "APCA-API-SECRET-KEY": api_keys['SECRET_KEY']}
                 )
print("requests.models.Response object - Account information --> {}".format(r.content))


#  ------------- Using alpaca_trade_api -------------
def acct_status():
    api = tradeapi.REST()
    account = api.get_account()
    print("Account status is --> {}".format(account.status))


acct_status()
