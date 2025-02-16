import json
from pymongo import MongoClient
from bson import json_util
#json_util.default to handle non-serializable types, 
# which provides a more accurate representation of MongoDB-specific types like ObjectId.
# Step 1: Connect to MongoDB
client = MongoClient('mongodb://localhost:27017/')  # Replace with your MongoDB URI
db = client['harsha']  # Replace with your database name
collection = db['restaurants']  # Replace with your collection name

# Step 2: Fetch data from MongoDB
data = list(collection.find({}))  # Fetch all documents from the collection

# Step 3: Export data to a JSON file
output_file_path = r'C:\Users\harsh\Desktop\harsha_wipro\python\Day12\rest.json'
with open(output_file_path, 'w', encoding='utf-8') as file:
    json.dump(data, file, default=json_util.default, indent=4)  
# Use json_util.default to handle non-serializable types like ObjectId
print(f"Data exported to '{output_file_path}'")


#Converts non-serializable types to their string representation using default=str.
# import json
# from pymongo import MongoClient

# # Step 1: Connect to MongoDB
# client = MongoClient('mongodb://localhost:27017/')  # Replace with your MongoDB URI
# db = client['harsha']  # Replace with your database name
# collection = db['restaurants']  # Replace with your collection name

# # Step 2: Fetch data from MongoDB
# data = list(collection.find({}))  # Fetch all documents from the collection

# # Step 3: Export data to a JSON file
# with open(r'C:\Users\harsh\Desktop\harsha_wipro\python\Day12\res.json', 'w') as file:
#     json.dump(data, file, default=str)  # Use default=str to handle non-serializable types like ObjectId

# print("Data exported to 'exported_data.json'")