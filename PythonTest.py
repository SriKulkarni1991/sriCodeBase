# REST API Calls

import requests
from bs4 import BeautifulSoup

response = requests.get("https://www.google.co.in")
print(response.status_code)
print(response.text)

soup = BeautifulSoup(response.text, 'html.parser') 
for link in soup.find_all('a'):
#    print(link.get('href'))
#    print()
    
#to read all links from www.google.com
    
response = requests.get("https://www.google.co.in")
print(response.links())
