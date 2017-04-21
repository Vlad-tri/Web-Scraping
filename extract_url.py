import requests
from bs4 import BeautifulSoup

url = raw_input("Enter the Website\n")

r = requests.get("http://"+url)

data = r.text

soup = BeautifulSoup(data,"lxml")

for link in soup.find_all('a'):
   print(link.get('href'))
