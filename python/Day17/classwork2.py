import json
 
with open(r"C:\Users\harsh\Desktop\harsha_wipro\python\Day17\dataj.json", "r") as file:
    loaded_data = json.load(file)
 
print(loaded_data)