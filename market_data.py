# import os
import websocket
# import alpaca_trade_api as trade_api


def on_open(ws):
    print("opened")
    # auth_data = {
    #     "action" : "authenticate",
    #     "data" : {"key_id" : api_keys['API_KEY_ID'], "secret_key" : api_keys['SECRET_KEY']}
    # }
    # ws.send(json.dumps(auth_data))


# websocket.enableTrace(True)
socket = "wss://data.alpaca.markets/stream"
ws = websocket.WebSocketApp(socket, on_open=on_open)
ws.run_forever()
print('hello')


# def on_message(ws, message):
#     print("rec a message")
#     print(message)


# secrets_filename = 'KEY_FILE.json'
# api_keys = {}
# with open(secrets_filename, 'r') as f:
#     api_keys = json.loads(f.read())
# os.environ["APCA_API_KEY_ID"] = api_keys['API_KEY_ID']
# os.environ["APCA_API_SECRET_KEY"] = api_keys['SECRET_KEY']
# os.environ["APCA_API_BASE_URL"] = "https://paper-api.alpaca.markets"

# ws = websocket.WebSocket()
#
# ws = websocket.WebSocketApp(socket, on_open=on_open, on_message=on_message)  # , on_message=on_message, on_close=on_close
# ws.on_open = on_open(ws)
# ws.run_forever()
# print("goodbye")

# if __name__ == "__main__":
