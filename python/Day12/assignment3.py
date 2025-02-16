import csv
from pymongo import MongoClient

# Step 1: Connect to MongoDB
client = MongoClient('mongodb://localhost:27017/')  # Replace with your MongoDB URI
db = client['harsha']  # Replace with your database name
collection = db['cust']  # Replace with your collection name

# Step 2: Fetch data from MongoDB
data = list(collection.find({}))  # Fetch all documents from the collection

# Step 3: Export data to a CSV file
output_file_path = r'C:\Users\harsh\Desktop\harsha_wipro\python\Day12\cus.csv'
if data:
    # Extract field names (keys) from the first document
    fieldnames = data[0].keys()

    with open(output_file_path, 'w', newline='', encoding='utf-8') as file:
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()  # Write the header row
        writer.writerows(data)  # Write all documents

    print(f"Data exported to '{output_file_path}'")
else:
    print("No data found in the collection.")