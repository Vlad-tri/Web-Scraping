import requests
from bs4 import BeautifulSoup

page = requests.get("http://dataquestio.github.io/web-scraping-pages/simple.html")

print page.status_code

soup = BeautifulSoup(page.content,'html.parser')

print soup.prettify()

for item in list(soup.children):
    print type(item)

html = list(soup.children)[2]

print list(html.children)

for item in list(html.children):
   print type(item)

body = list(html.children)[3]

print list(body.children)

p = list(body.children)[1]

print p.get_text()

print soup.find_all('p')[0].get_text()
