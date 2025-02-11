import os
file_path = r"c:/Users/harsh/Desktop/python/python_dt_b2/python/Day6/lab9.py"
if os.path.exists(file_path):
    print("The file exists!")
else:
    print("The file does not exist.")