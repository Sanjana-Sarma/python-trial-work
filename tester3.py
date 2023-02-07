import urllib.request,urllib.parse,urllib.error
import ssl
import json

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

api_key=False
if api_key is False:
    api_key = 42
    serviceurl = 'http://py4e-data.dr-chuck.net/json?'
else :
    serviceurl = 'https://maps.googleapis.com/maps/api/geocode/json?'
location=input("Enter Location:")
parms=dict()
parms['address']=location
if api_key is not False:
	parms['key']=api_key
url=serviceurl+urllib.parse.urlencode(parms)

uh=urllib.request.urlopen(url,context=ctx)
data=uh.read().decode()
length=len(data)
js=json.loads(data)
placeID=js["results"][0]["place_id"]
print("Retreiving",url)
print("Retreived",length,"characters")
print("Place ID:",placeID)