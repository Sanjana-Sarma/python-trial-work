import urllib.request,urllib.parse,urllib.error
import ssl
import xml.etree.ElementTree as ET

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url=input("Enter location:")
uh=urllib.request.urlopen(url,context=ctx)
data=uh.read()
datalen=len(data)
tree=ET.fromstring(data)
lst=tree.findall('comments/comment')
count1=len(lst)
summation=0
lst2=tree.findall('.//count')
count2=len(lst2)
lst3=list()
for item in lst:
	lst3.append(item.find('count').text)
for ls in lst3:
	num=int(ls)
	summation+=num
print("Retreiving",url)
print("Retreived",datalen,"characters")
print("Count:",count2)
print("Sum:",summation)