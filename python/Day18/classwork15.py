import requests
 
url = 'https://www.skillsugar.com/contact'
 
params = {'name': 'harsha', 'subject' : 'Programming', 'message': 'Hello', 'email': 'harsha@gmail.com'}
 
result = requests.post(url, params=params)
 
print(result.headers)

data=requests.get(url)
 
# List content under  url = 'https://www.skillsugar.com/contact'

# print(data)
 