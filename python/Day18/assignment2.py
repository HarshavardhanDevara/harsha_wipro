# 2. HTTP PUT Request              Assign  2
# Updates a resource on the server.

import requests
url = "https://jsonplaceholder.typicode.com/posts/1"
data = {
    "title": "Rps  Title",
    "body": "Updated from Rps",
    "userId": 1
}
 
response = requests.put(url, json=data)
 
if response.status_code == 200:
    print("Updated Successfully:", response.json())
else:
    print("Update failed")