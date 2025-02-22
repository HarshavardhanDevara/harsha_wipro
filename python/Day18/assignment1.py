# 1. HTTP GET Request   -Assign 1
# Fetches data from a server.
import requests
 
url = "https://jsonplaceholder.typicode.com/posts/1"
 
response = requests.get(url)
 
if response.status_code == 200:
 
    print("Response:", response.json())  # JSON response
else:
    print("Failed to fetch data")