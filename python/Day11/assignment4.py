# Assignment 4 : convert dictionary into json format and write into a file
import json
# Dictionary to be converted into JSON format
data = {
    "name": "harshavardhan",
    "age": 25,
    "city": "Tirupati"
}

# Convert dictionary to JSON and write to a file
with open(r"c:/Users/harsh/Desktop/harsha_wipro/python/Day11/data.json", 'w') as json_file:
    json.dump(data, json_file)
print("Dictionary has been written to data.json in JSON format")