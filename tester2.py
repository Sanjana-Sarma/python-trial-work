import urllib.request,urllib.parse,urllib.error
import ssl
import json

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE
url=input("Enter URL:")
uh=urllib.request.urlopen(url,context=ctx)
data=uh.read()
length=len(data)
js=json.loads(data)
lst=js['comments']
summation=0
count=0

for item in lst:
	num=int(item['count'])
	summation+=num
	count+=1
print("Retreiving",url)
print("Retreived",length,"characters")
print("Count:",count)
print("Sum:",summation)

