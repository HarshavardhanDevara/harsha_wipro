#removing dir
import os
import shutil

dir_to_remove = "C:/Users/harsh/Desktop/python_dt_b2/python/Day6/NewFolder"

if os.path.exists(dir_to_remove):
    shutil.rmtree(dir_to_remove)           #to give permission to del folders if it has files in it
    print(f"Directory {dir_to_remove} has been removed.")
else:
    print("The directory does not exist.")