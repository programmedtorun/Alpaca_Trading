import websocket, json, os


secrets_filename = 'KEY_FILE.json'
api_keys = {}
with open(secrets_filename, 'r') as f:
    api_keys = json.loads(f.read())
os.environ["APCA_API_KEY_ID"] = api_keys['API_KEY_ID']
os.environ["APCA_API_SECRET_KEY"] = api_keys['SECRET_KEY']
os.environ["APCA_API_BASE_URL"] = "https://paper-api.alpaca.markets"

def on_open():
    print("opened")
    auth_data = {
        "action" : "authenticate",
        "data" : {"key_id" : api_keys['API_KEY_ID'], "secret_key" : api_keys['SECRET_KEY']}
    }
    ws.send(json.dumps(auth_data))



ws = websocket.WebSocketApp("ws://data.alpaca.markets/stream", on_open=on_open)
ws.run_forever()
print('hello')



# ummmm okay this code works.....  ->
# import websocket
# try:
#     import thread
# except ImportError:
#     import _thread as thread
# import time
#
# def on_message(ws, message):
#     print(message)
#
# def on_error(ws, error):
#     print(error)
#
# def on_close(ws):
#     print("### closed ###")
#
# def on_open(ws):
#     def run(*args):
#         for i in range(3):
#             time.sleep(1)
#             ws.send("Hello %d" % i)
#         time.sleep(1)
#         ws.close()
#         print("thread terminating...")
#     thread.start_new_thread(run, ())
#
#
# if __name__ == "__main__":
#     websocket.enableTrace(True)
#     ws = websocket.WebSocketApp("ws://echo.websocket.org/",
#                               on_message = on_message,
#                               on_error = on_error,
#                               on_close = on_close)
#     ws.on_open = on_open
#     ws.run_forever()
