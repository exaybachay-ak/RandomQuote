###--->>> Random quote from quotes.net <<<---###

### --->>> Perform imports
import requests
import re
import random
from lxml import html

### --->>> Set up functions
def getQuote():
	### Start at 2 because quote 1 is nothing
	rand = random.randrange(2,80000)
	### Go out and retrieve our random quote
	r = requests.get('https://www.quotes.net/quote/' + str(rand))

	### If we get the green light, parse the quote
	if r.status_code == 200:
			# Retrieve the HTML elements from response data
			tree = html.fromstring(r.content)
			quotetitle = tree.xpath('//title/text()')
			return quotetitle[0]

	### If there is an issue, say something
	else:
		print("Looks like you encountered an error retrieving the page.")

def testQuote(quote):
	if quote == "Quotes.net":
		return False
	else:
		return True

### --->>> Run functions and return quote after checking it
quote = getQuote()

if testQuote(quote):
	print(quote)
else:
	secondquote = getQuote()
	if testQuote(secondquote):
		print(secondquote)
	else:
		# Just print whatever we get here.. odds are it will be a real quote
		thirdquote = getQuote()
		print(thirdquote)
