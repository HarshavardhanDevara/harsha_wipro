import requests
response = requests.get("https://api.github.com")
print(response)  # This will output: <Response [200]>

print(response.status_code)

# print(response.text)  # Prints the response body as text
# print(response.json())  # Parses and prints JSON data