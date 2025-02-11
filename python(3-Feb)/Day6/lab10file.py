import os
file_path = r"C:\Users\harsh\Desktop\python\python_dt_b2\python\Day3\marks.txt"
if os.path.exists(file_path):
    print("The file exists!")
else:
    print("The file does not exist.")