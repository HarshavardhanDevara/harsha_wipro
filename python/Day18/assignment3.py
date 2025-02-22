# 3. Batch HTTP Requests  -Assign 3
# Since HTTP does not natively support batch requests, you can:
# Use multiple requests in a loop.

import requests
 
urls = [
    "https://jsonplaceholder.typicode.com/posts/1",
    "https://jsonplaceholder.typicode.com/posts/2",
    "https://jsonplaceholder.typicode.com/posts/3"
]
 
responses = [requests.get(url).json() for url in urls]  #
 
print(responses)