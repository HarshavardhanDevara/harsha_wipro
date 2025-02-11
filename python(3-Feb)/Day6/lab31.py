#list contents in dir
import os

dir_path = "C:/Users/harsh/Desktop/python_dt_b2/python/Day6"

contents = os.listdir(dir_path)
print("Directory contents:")
for item in contents:
    print(item)