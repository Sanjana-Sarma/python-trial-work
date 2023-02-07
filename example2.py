import urllib.request,urllib.parse,urllib.error
from bs4 import BeautifulSoup
import ssl
import re
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE
url=input("Enter URL:")
cnt=input("Enter count:")
pos=input("Enter position:")
count=int(cnt)
position=int(pos)
html=urllib.request.urlopen(url,context=ctx).read()
soup=BeautifulSoup(html,'html.parser')
urllist=list()
lst=list()
lst.append(url)
tags=soup('a')
for tag in tags:
	urllist.append(tag.get('href',None))
for i in range(count):
	content=urllist[position-1]
	lst.append(content)
	html1=urllib.request.urlopen(content,context=ctx).read()
	soup1=BeautifulSoup(html1,'html.parser')
	tags1=soup1('a')
	urllist.clear()
	for tag1 in tags1:
		urllist.append(tag1.get('href',None))
length=len(lst)
names=list()
for j in range(length):
	print("Receiving:",lst[j])
	name1=''.join((re.findall("^http:.*known_by_([A-Za-z]+).html",lst[j])))
	names.append(name1)
namseq=""
for name in names:
	namseq+=" "+name
print("Sequence of names:",namseq)
lnamestr=''.join(names[len(names)-1])
print("Last Name in sequence:",lnamestr)