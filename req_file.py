import json
import requests
import os
import alpaca_trade_api as tradeapi
import logging



logging.basicConfig(filename='req_file.log', format='%(asctime)s %(message)s', level=logging.INFO)
#sys.path.insert(0, "/Library/Frameworks/Python.framework/Versions/3.7/lib/python3.7/site-packages")
# Note: you need to install pytz for alpaca_trade_api to work on your system `pip3 install pytz` if it already exists then you may
# have to manually update it by deleting the pytz.<blah>.dist-info and installing again.
logging.warning('%s before you %s', 'Look', 'leap!')
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
    if account.trading_blocked:
        print("account is blocked")
    else:
        print("account is not blocked")

    active_assets = api.list_assets(status='active', asset_class='us_equity')
    print("ACTIVE ASSET LISTING")
    # for a in active_assets:
    #     print(a.symbol)
    print("Account status is --> {}".format(account.status))


#  ------------- order stock -------------
def buy(symbol, side, type, qty, time_in_force):
    api = tradeapi.REST()
    # all_pos = api.list_positions()
    # print(all_pos)
    # snow_pos = api.get_position(symbol)
    # print("position in SNOW is: {}".format(snow_pos))
    order = api.submit_order(
        symbol=symbol,
        side=side,
        type=type,
        qty=qty,
        time_in_force=time_in_force
    )
    print("order is: {}".format(order))
    p_hist = api.get_portfolio_history()
    # print("portfolio history is: {}".format(p_hist))


acct_status()
# buy IBM stock
# buy('IBM', 'buy', 'market', 20, 'day')

