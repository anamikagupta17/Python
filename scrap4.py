
#scap data from particular site  specific data
import requests
from bs4 import BeautifulSoup

   
URL = "https://ra.co/music"
r = requests.get(URL)
   
soup = BeautifulSoup(r.content, 'html5lib')
   
quotes=[]  # a list to FEATURE SERIES
   
table = soup.find('section', attrs = {'class':'Box-omzyfs-0 Alignment-sc-1fjm9oq-0 SubSectionStacked__StyledAlignment-fviaip-0 iYpGFd'}) 
print(table)

# for row in table.findAll('li',attrs = {'class':'Column-sc-18hsrnn-0 Slide__Item-sc-1lo5y47-1 bcohQC'}):
    
#     quote = {}
#     quote['url'] = row.a['href']
#     quote['img'] = row.img['src']
#     quote['lines'] = row.img['alt']
#     titleblock = row.find('a',attrs={'class':'alt-font post-title text-medium text-extra-dark-gray width-100 d-block lg-width-100 margin-15px-bottom'})
#     quote['title']=titleblock.text
#     quote['description'] = row.p.text
#     quotes.append(quote)
    
# print(quotes)    
    
