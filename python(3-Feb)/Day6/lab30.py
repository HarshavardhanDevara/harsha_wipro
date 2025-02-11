#Creating a new directory
import os

new_dir = "C:/Users/harsh/Desktop/python_dt_b2/python/Day6/NewFolder"

if not os.path.exists(new_dir):
    os.mkdir(new_dir)
    print(f"Directory {new_dir} created successfully!")
else:
    print("Directory already exists.")