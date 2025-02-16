import csv
from pymongo import MongoClient

# Step 1: Connect to MongoDB
client = MongoClient('mongodb://localhost:27017/')  # Replace with your MongoDB URI
db = client['harsha']  # Replace with your database name
collection = db['c']  # Replace with your collection name

# Step 2: Load data from a CSV file
data = []
with open(r'C:\Users\harsh\Desktop\harsha_wipro\python\Day12\cus.csv', 'r') as file:
    reader = csv.DictReader(file)  # Read CSV file as a dictionary
    for row in reader:
        data.append(row)  # Append each row to the data list

# Step 3: Insert data into MongoDB
if data:
    collection.insert_many(data)  # Insert the loaded data
    print("Data imported successfully!")
else:
    print("No data found in the CSV file.")
