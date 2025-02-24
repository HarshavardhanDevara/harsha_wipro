import requests
import time
# session cookies
sess = requests.cookies.RequestsCookieJar()
 
expires_time = int(time.time()) + 1800
 
sess.set('token1', '123456', domain='example.com', path='/')

sess.set('token2', '123456', domain='example.com', path='/', expires=expires_time)
 
response = requests.get('https://example.com', cookies=sess)
 
print(response)
 