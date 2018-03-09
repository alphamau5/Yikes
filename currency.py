'''
Converts CAD to EUR, USD, or JPY using real-time currency exchange from the Bank of Canada.

Inputs (for now): euro, usd, or yen

Plan to add more eventually, hopefully in a more efficient and user friendly way.
'''

import urllib.request as urllib
import re
import datetime
today = datetime.date.today()

print('This is a CAD currency converter')
which_cur = str(input('Choose euro/usd/yen: '))

if which_cur == 'euro':
    x = 'EUR'
elif which_cur == 'usd':
    x = 'USD'
elif which_cur == 'yen':
    x = 'JPY'

url = 'https://www.bankofcanada.ca/valet/fx_rss/FX' + str(x) + 'CAD'    
response = urllib.urlopen(url)

for line in response:
    if 'value decimals' in str(line):
        line_with_cur = str(line)

find_cur = re.findall("\d+\.\d+", line_with_cur)
cur = float(find_cur[0])

print('1 ' + str(x) + ' =', cur, 'CAD as of', str(today) + '\n')

amount = float(input('CAD: '))
conversion = amount/cur
print(round(amount,2), 'CAD is ' + str(round(conversion,2)) + ' ' + str(x))
