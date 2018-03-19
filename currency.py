'''
Converts CAD to EUR, USD, or JPY using real-time currency exchange from the Bank of Canada.
Inputs (for now): euro, usd, or yen

To do:
Solve the same problem but by using XML module rather than by parsing through HTML as follows.
'''

import urllib.request as urllib
import re
import datetime
today = datetime.date.today()

print('This is a CAD currency converter\nType q to quit')

def choose_currency():

	which_cur = str(input('\nChoose euro/usd/yen: '))

	if which_cur == 'euro':
	    conversion('EUR')
	elif which_cur == 'usd':
	    conversion('USD')
	elif which_cur == 'yen':
	    conversion('JPY')
	elif which_cur == 'q':
		quit()
	else:
		print("Not a valid currency")
		choose_currency()

def conversion(x):

	url = 'https://www.bankofcanada.ca/valet/fx_rss/FX' + x + 'CAD'    
	response = urllib.urlopen(url)

	for line in response:
	    if 'value decimal' in str(line):
	        line_with_cur = str(line)

	find_cur = re.findall("\d+\.\d+", line_with_cur)
	cur = float(find_cur[0])
	print('1 ' + x + ' =', cur, 'CAD as of', str(today))

	amount = float(input('CAD: '))
	convert = amount/cur
	print(round(amount,2), 'CAD is ' + str(round(convert,2)) + ' ' + x)
	choose_currency()

choose_currency()
