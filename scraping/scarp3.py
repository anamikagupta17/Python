
#scap data from particular site  specific data
import requests
from bs4 import BeautifulSoup

   
URL = "https://www.passiton.com/passiton-blog"
r = requests.get(URL)
   
soup = BeautifulSoup(r.content, 'html5lib')
   
quotes=[]  # a list to FEATURE SERIES
   
table = soup.find('section', attrs = {'class':'blog-post-style3'}) 
for row in table.findAll('div',attrs = {'class':'blog-post bg-light-gray inner-match-height'}):
    
    quote = {}
    quote['url'] = row.a['href']
    quote['img'] = row.img['src']
    quote['lines'] = row.img['alt']
    titleblock = row.find('a',attrs={'class':'alt-font post-title text-medium text-extra-dark-gray width-100 d-block lg-width-100 margin-15px-bottom'})
    quote['title']=titleblock.text
    quote['description'] = row.p.text
    quotes.append(quote)
    
print(quotes)    
    
