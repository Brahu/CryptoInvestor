from os import system
system('cls')



import hashlib
import hmac
import http.client
import json

API_URL = 'api.changelly.com'
API_KEY = 'a6fe39309b6348c2b15f24418fdacb2b'
API_SECRET = 'a982183cbe3446f9ed4282c27f4cbd1e2ea8524255c0dfe19621d836aaa05516'

conn = http.client.HTTPSConnection(API_URL)

message = {
  "jsonrpc": "2.0",
  "method": "getMinAmount",
  "params": {
    "from": "ltc",
    "to": "eth",
  },
  "id": 0
}

message = {
  "jsonrpc": "2.0",
  "method": "getCurrencies",
  "params": {},
  "id": 0
}

message = {
  "jsonrpc": "2.0",
  "method": "getExchangeAmount",
  "params": [{
    "from": "ltc",
    "to": "eth",
    "amount": "1"
  }, {
    "from": "dash",
    "to": "xmr",
    "amount": "1"
  }],
  "id": 0
}





serialized_data = json.dumps(message)

sign = hmac.new(API_SECRET.encode('utf-8'), serialized_data.encode('utf-8'), hashlib.sha512).hexdigest()


headers = {'api-key': API_KEY, 'sign': sign, 'Content-type': 'application/json'}


conn.request("POST", "/", serialized_data, headers)

res = conn.getresponse()
data = res.read()

print(data.decode("utf-8"))
