import requests
 
response = requests.get("https://api.github.com")
 
headerInfo=response.headers
 
print(headerInfo)


