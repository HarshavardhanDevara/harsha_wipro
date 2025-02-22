import requests
 
url = 'https://www.skillsugar.com/search'
params = {'query': 'python', 'sort': 'date'}
result = requests.get(url, params=params)
print(result.url)