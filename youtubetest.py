import urllib
import re

urls = ["http://google.com","http://nytimes.com","http://CNN.com","https://facebook.com","http://youtube.com"]

regex = '<title>(.+?)</title>'
pattern = re.compile(regex)

for url in urls:
    htmlfile = urllib.urlopen(url)
    htmltext = htmlfile.read()
    titles = re.findall(pattern,htmltext)
    print titles
    print "------BREAK------"
