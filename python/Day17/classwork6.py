import csv
 
# Data to write
data = [
    ["Name", "Age", "City"],
    ["harsha", 25, "New York"],
    ["muni", 20, "Los Angeles"],
    ["hari", 35, "kadapa"]
]
 
# Writing to a CSV file
with open(r"C:\Users\harsh\Desktop\harsha_wipro\python\Day17\dataj.csv", "w", newline="") as file:
    writer = csv.writer(file)
    writer.writerows(data)  # Write multiple rows