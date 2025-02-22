import requests
response = requests.get("https://api.github.com")
response.content
print(type(response.content))
print(response.content) #to see data in url
# print(response.text)  # Prints the response body as text
# print(response.json())  # Parses and prints JSON data