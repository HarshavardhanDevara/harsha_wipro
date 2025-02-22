import requests
 
response=requests.get("https://api.github.com", timeout=1.05)
 
print(response)
 
response= requests.get("https://api.github.com", timeout=10.05)
 
print(response)