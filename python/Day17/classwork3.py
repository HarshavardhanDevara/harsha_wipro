# Appending data 

import json
 
with open(r"C:\Users\harsh\Desktop\harsha_wipro\python\Day17\dataj.json", "r") as file:

    existing_data = json.load(file)
 
existing_data["email"] = "harsha@example.com"  # Modify or add data
 
with open(r"C:\Users\harsh\Desktop\harsha_wipro\python\Day17\dataj.json", "w") as file:

    json.dump(existing_data, file, indent=4)

 