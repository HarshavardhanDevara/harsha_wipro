# 1: Creating a Hash Table (Dictionary)
hash_table = {}  # Empty dictionary
hash_table["name"] = "Alice"
hash_table["age"] = 25
hash_table["city"] = "New York"
print(hash_table)  # {'name': 'Alice', 'age': 25, 'city': 'New York'}
 
# 2. Accessing Values
print(hash_table["name"])  # Alice
# Using a non-existent key raises a KeyError. Use .get() to avoid this:
print(hash_table.get("country", "Not Found"))  # Not Found
 
# 3. Removing Elements
del hash_table["age"]  # Removes key 'age'
print(hash_table)  # {'name': 'Alice', 'city': 'New York'}
# Using pop()
city = hash_table.pop("city")
print(city)  # New York
 
# 4. Checking if a Key Exists
if "name" in hash_table:
    print("Key exists!")
 
# 5. Iterating Over a Hash Table
for key, value in hash_table.items():
    print(f"{key}: {value}")
 
# 6. Handling Collisions with collections.defaultdict
# If multiple values need to be stored under the same key, use defaultdict:
from collections import defaultdict
hash_table = defaultdict(list)
hash_table["fruits"].append("Apple")
hash_table["fruits"].append("Banana")
print(hash_table)  # {'fruits': ['Apple', 'Banana']}

 