
#scap data from particular site  specific data
import requests
import time
from bs4 import BeautifulSoup



URL = "https://finsight.com/list-of-global-fixed-income-corporate-sponsors"

r = requests.get(URL) 
 
soup = BeautifulSoup(r.content, 'html5lib')
print(soup)

quotes=[]  # a list to FEATURE SERIES
   
table = soup.find('div', attrs = {'class':'catalogScrollHolder'}) 
print(table)
for row in table.findAll('p'):
    
    quote = {}
    titleblock = row.find('a')
    quote['title']=titleblock.text
    quote['url'] = titleblock.a['href']
    quotes.append(quote)
    
print(quotes)