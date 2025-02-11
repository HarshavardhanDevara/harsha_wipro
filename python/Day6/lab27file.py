#creating a new file
import os

file_path = "C:/Users/harsh/Desktop/python_dt_b2/python/Day6/new_file.txt"
with open(file_path, 'w') as file:
    file.write("Hello my name is harshavardhan")

print(f"A new file has been created at {file_path}")