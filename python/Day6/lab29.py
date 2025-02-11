#deleting a file
import os

file_to_delete = "C:/Users/harsh/Desktop/python_dt_b2/python/Day6/hello_name.txt"

if os.path.exists(file_to_delete):
    os.remove(file_to_delete)
    print(f"The file {file_to_delete} has been deleted.")
else:
    print("The file does not exist.")