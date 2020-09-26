###--->>> Random quote from quotes.net <<<---###
import requests
import random
from lxml import html


### --->>> Set up functions
def getQuote():
	# Start at 2 because quote 1 is gibberish
	rand = random.randrange(2,80000)
	###--->>> Go out and retrieve our random quote
	r = requests.get('https://www.quotes.net/quote/' + str(rand))

	###--->>> If we get the green light, parse the quote
	if r.status_code == 200:
		# Retrieve the HTML elements from response data
		tree = html.fromstring(r.content)
		quotetitle = tree.xpath('//title/text()')
		global q
		q = quotetitle[0]

	###--->>> If there is an issue, say something
	else:
		print("Looks like you encountered an error retrieving the page.")

def testQuote(quote):
	if quote == "Quotes.net":
		return False
	else:
		return True


### --->>> Run functions and print quote after validating it
actualQuote = False
while actualQuote == False:
	quote = getQuote()
	test = testQuote(q)

	if test == True:
		print(q)
		actualQuote = True

	else:
		pass
