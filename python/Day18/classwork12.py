import requests
 
url = 'https://www.skillsugar.com/examples/json/example_1.json'
 
result = requests.get(url)  # result is a variable of type response object
 
print(result.json())