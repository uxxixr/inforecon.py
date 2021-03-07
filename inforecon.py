import sys
import requests
import socket
import json

if len(sys.argv) < 2:
	print("[+] Usage " + sys.argv[0] + "url")
	sys.exit(1)
	
req = requests.get("https://" + sys.argv[1])
print("/n"+ str(req.headers))

gethostby_ = socket.gethostbyname(sys.argv[1])
print("/n[+] The IP Address of " + sys.argv[1] + " is: "+gethostby_ + "/n")

req1 = requests.get("https://ipinfo.io/"+gethostby_+"/json")
resp = json.loads(req1.text)

print("--> Location: "+resp["loc"])
print("--> Region: "+resp["region"])
print("--> City: "+resp["city"])
print("--> Country: "+resp["country"])