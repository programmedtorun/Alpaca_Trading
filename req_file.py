import json
import requests
import os
# import pytz
# import sys
#sys.path.insert(0, "/Library/Frameworks/Python.framework/Versions/3.7/lib/python3.7/site-packages")
# Note: you need to install pytz for alpaca_trade_api to work on your system `pip3 install pytz` if it already exists then you may
# have to manually update it by deleting the pytz.<blah>.dist-info and installing again.
import alpaca_trade_api as tradeapi



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

def acct_status():
    # obj = requests.get(ACCOUNT_URL, headers=
    #             {"APCA-API-KEY-ID": api_keys['API_KEY_ID'],
    #             "APCA-API-SECRET-KEY": api_keys['SECRET_KEY']}
    #              )
    # print(type(obj))
    # seting env variables, will move these outside script
    os.environ["APCA_API_KEY_ID"] = api_keys['API_KEY_ID']
    os.environ["APCA_API_SECRET_KEY"] = api_keys['SECRET_KEY']
    os.environ["APCA_API_BASE_URL"] = "https://paper-api.alpaca.markets"
    api = tradeapi.REST()
    account = api.get_account()
    print(account.status)


# print("account status is: {}".format(acct_status()))
acct_status()
