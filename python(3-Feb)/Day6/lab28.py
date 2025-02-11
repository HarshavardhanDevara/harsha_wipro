#renaming an old file
import os

new_file = "C:/Users/harsh/Desktop/python_dt_b2/python/Day6/new_file.txt"
hello_name = "C:/Users/harsh/Desktop/python_dt_b2/python/Day6/hello_name.txt"

os.rename(new_file, hello_name)
print(f"File renamed from {new_file} to {hello_name}")