import csv
 
with open(r"C:\Users\harsh\Desktop\harsha_wipro\python\Day17\dataj.csv", "r") as file:
 
    reader = csv.reader(file)
 
    for row in reader:
 
        print(row)