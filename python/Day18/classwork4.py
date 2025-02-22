import requests
 
response=requests.get("https://api.github.com")
 
if response:
    print("Success!")
else:
    raise Exception(f"Non-success status code: {response.status_code}")
 
# when we raise - it is custom exception. Tt is not  built in exception