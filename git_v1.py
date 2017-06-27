import requests
from bs4 import BeautifulSoup

#f=open('a','w')
#print >> f,requests.get("https://github.com/Ayush21298/").text.encode('utf-8')
res=requests.get("https://github.com/Ayush21298/").text.encode('utf-8')
soup=BeautifulSoup(res,"lxml")
for x in soup.findAll('span',{'class':'repo js-repo'}):
	print x.contents[0]
