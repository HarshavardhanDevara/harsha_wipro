import json
from pymongo import MongoClient

# Step 1: Connect to MongoDB
client = MongoClient('mongodb://localhost:27017/')
db = client['harsha']
collection = db['restau']

# Step 2: Load JSON data line by line
with open(r'C:\Users\harsh\Desktop\harsha_wipro\python\Day12\restaurants.json', 'r') as file:
    data = [json.loads(line) for line in file]  # Read each line as a separate JSON object

# Step 3: Insert data into MongoDB
if data:
    collection.insert_many(data)
    print("Data imported successfully!")
else:
    print("No data found in the JSON file.")
