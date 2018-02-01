from os import system
system('cls')



import http.client


API_URL = 'coinmarketcap.com'

conn = http.client.HTTPSConnection(API_URL)



my_coins = ['BTC', 'ETH', 'XMR', 'FCN', 'AEON', 'BCN', 'DSH', 'ETC', 'BCH', 'BTX']

excluded = ["AUD", "BRL", "CAD", "CHF", "CLP", "CNY", "CZK", "DKK", "EUR", "GBP", "HKD", "HUF", "IDR", "ILS", "INR", "JPY", "KRW", "MXN", "MYR", "NOK", "NZD", "PHP", "PKR", "PLN", "RUB", "SEK", "SGD", "THB", "TRY", "TWD", "ZAR", "USDT"]

exchanges= ['', '']



coin = 'bitcoin'

conn.request("GET", "/currencies/" + coin + "/#markets")

rate = conn.getresponse()

sajt = rate.read()


print(sajt)




print()
print()





from html.parser import HTMLParser
import urllib.request as urllib2
from html.parser import HTMLParser

# A class that inherits from HTMLParser.
# ... It implements two methods.
class TagParser(HTMLParser):
	def handle_starttag(self, tag, attrs):
		# Set "tag" field to the name of the opened tag.
		self.tag = tag

	def handle_data(self, sajt):
		# Print data within currently-open tag.
		# if self.tag == 'a':
			# print(self.tag + ":", data)
		# if self.tag == 'span':
			# print(self.tag + ":", data)
			# print()
		pass

parser = TagParser()
parser.feed("<h1>Python</h1>" +
			"<p>Is cool.</p>");




# Opening NYTimes site using urllib2
html_page = urllib2.urlopen("https://coinmarketcap.com/currencies/bitcoin/#markets")

# Feeding the content
parser.feed(str(html_page.read()))









from html.parser import HTMLParser
# data = '''
# <html>
# <table border="1px">
# <tr>
# <td>yes</td>
# <td>no</td>
# </tr>
# </table>
# </html>
# '''

tableBjacz = []



class TableParser(HTMLParser):
	def __init__(self):
		HTMLParser.__init__(self)
		self.in_td = False

	def handle_starttag(self, tag, attrs):
		if tag == 'td':
			self.in_td = True

	def handle_data(self, data):
		if self.in_td:
			if data.strip():
				tableBjacz.append(data.strip())
				print(data)

	def handle_endtag(self, tag):
		self.in_td = False

p = TableParser()
fet = p.feed(sajt.decode())

print()
print()
print()
print()
print()

tmp		= []
tejbyl	= {}

for i in range(len(tableBjacz)):
	try:
		if isinstance(int(tableBjacz[i-7]), int):
			tejbyl[str(tableBjacz[i-7])] = tmp
			tmp		= []
	except:
		pass
	if i == '0':
		pass
	else:
		tmp.append(tableBjacz[i])

for i in range(391, 401):
	del tejbyl[str(i)]

highest			= 0.0
highestindex	= 0

for i in tejbyl:
	print(tejbyl[i])
	if float(tejbyl[i][4][1:]) > highest:
		if (tejbyl[i][2].split('/')[0] in excluded) or (tejbyl[i][2].split('/')[1] in excluded):
			pass
		else:
			highest			= float(tejbyl[i][4][1:])
			highestindex	= i


print()
print()
print()
print()
print()


print(tejbyl[highestindex][1], tejbyl[highestindex][2], tejbyl[highestindex][4][1:])
