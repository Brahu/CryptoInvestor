from os import system
system('cls')


import http.client
import json

API_URL = 'api.coinmarketcap.com'

conn = http.client.HTTPSConnection(API_URL)



my_coins = ['BTC', 'ETH', 'XMR', 'FCN', 'AEON', 'BCN', 'DSH', 'ETC', 'BCH', 'BTX']



conn.request("GET", "/v1/ticker/?limit=1000")

rate = conn.getresponse()

data = rate.read()

data = json.loads(data)

print(data)

tab = '	'

for i in range(len(data)):
	if len(data[i]['id']) < 7:
		print(data[i]['id'], tab*3, data[i]['symbol'], tab, data[i]['price_usd'], tab, data[i]['price_btc'], tab)
	elif len(data[i]['id']) < 15:
		print(data[i]['id'], tab*2, data[i]['symbol'], tab, data[i]['price_usd'], tab, data[i]['price_btc'], tab)
	else:
		print(data[i]['id'], tab, data[i]['symbol'], tab, data[i]['price_usd'], tab, data[i]['price_btc'], tab)

print()

for i in range(len(data)):
	if data[i]['symbol'] in my_coins:
		print(data[i]['symbol'], tab, data[i]['rank'])

print()
print()
