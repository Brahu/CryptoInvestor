from os import system
system('cls')


import http.client
import json

API_URL = 'shapeshift.io'

conn = http.client.HTTPSConnection(API_URL)



conn.request("GET", "/getcoins")

getcoins = conn.getresponse()

data = getcoins.read()

data = json.loads(data)

print(data['BTG']['status'])


for i in data:
	print(data[i]['status'])



print()
print()
print()



conn.request("GET", "/marketinfo")			#	/rate

rate = conn.getresponse()

data = rate.read()

data = json.loads(data)

# print(data)

tab = '	'

for i in range(len(data)):
	if len(data[i]['pair']) > 6:
		print(data[i]['pair'], tab, data[i]['rate'], tab, data[i]['min'], tab, data[i]['limit'], tab, data[i]['maxLimit'], tab, data[i]['minerFee'])
