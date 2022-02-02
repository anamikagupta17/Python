import requests
from bs4 import BeautifulSoup
  
URL = "https://www.geeksforgeeks.org/data-structures/"
r = requests.get(URL)
#print(r.content)
soup = BeautifulSoup(r.content, 'html5lib') 