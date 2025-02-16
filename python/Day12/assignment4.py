import json
from pymongo import MongoClient

# Step 1: Connect to MongoDB
client = MongoClient('mongodb://localhost:27017/')  # Replace with your MongoDB URI
db = client['harsha']  # Replace with your database name
collection = db['restau']  # Replace with your collection name

# Step 2: Load data from a JSON file
with open(r'C:\Users\harsh\Desktop\harsha_wipro\python\Day12\restaurants.json', 'r') as file:
    data = json.load(file)  # Load JSON data into a Python list

# Step 3: Insert data into MongoDB
if data:
    collection.insert_many(data)  # Insert the loaded data
    print("Data imported successfully!")
else:
    print("No data found in the JSON file.")