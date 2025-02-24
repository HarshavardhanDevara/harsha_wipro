import requests
 
r = requests.get('http://google.com')
 
for c in r.cookies: 
	print(c.name +"==>>", c.value)