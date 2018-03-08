import urllib.request as urllib
import re
import datetime

today = datetime.date.today()

url = 'https://www.bankofcanada.ca/valet/fx_rss/FXUSDCAD'    
response = urllib.urlopen(url)
for line in response:
    if '<cb:value decimals=>' in str(line):
        x = str(x)

y = re.findall("\d+\.\d+", x)
z = float(y[0])

print('1 USD =', z, 'CAD \n(US dollar to Canadian dollar daily exchange rate as of', str(today) + ')\n')

amt = float(input('CAD: '))
usd = amt/z
print(round(amt,2), 'CAD is ' + str(round(usd,2)) + ' USD')
