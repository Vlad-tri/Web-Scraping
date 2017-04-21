import urllib
import re

symbolfile = open("symbol.txt")

symlist = symbolfile.read()
symlist = symlist.split("\n")

for name in symlist:
	htmlfile = urllib.urlopen("http://www.nasdaq.com/symbol/"+name+"/after-hours")
	htmltext = htmlfile.read()
	regex = '<div id="qwidget_lastsale" class="qwidget-dollar">(.+?)</div>'
	pattern = re.compile(regex)
	price = re.findall(pattern,htmltext)
	print "The Stock Price for "+name+" is "+str(price)+"."
