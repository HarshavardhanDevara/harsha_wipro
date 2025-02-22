import json
 
data = {  "name": "harsha", "age": 25, "city": "tirupati" }
 
# Writing JSON to a file
 
with open(r"C:\Users\harsh\Desktop\harsha_wipro\python\Day17\dataj.json", "w") as file:
 
    json.dump(data, file, indent=4)   # 'indent=4'   makes it readable
 
 
# json.dump(obj, file) → Write JSON to a file.