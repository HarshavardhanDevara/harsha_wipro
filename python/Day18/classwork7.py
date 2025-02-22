import requests
response = requests.get("https://api.github.com")
dict=response.json()
print(dict)

# print(response.content)
# print(response.text)  # Prints the response body as text
# print(response.json())  # Parses and prints JSON data
print(type(response.json()))
print(type(response.text))  # Prints the response body as text
print(type(response.content))