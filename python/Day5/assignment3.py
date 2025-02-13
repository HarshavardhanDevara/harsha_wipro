# Create a script that lists all files and directories in the current directory, 
# # creates a copy of a file, and renames a directory. Use the os module for these operations. 

import os
import shutil

def list_files_and_directories():
    print("Listing all files and directories in the current directory:")
    for item in os.listdir('.'):
        print(item)

def copy_file(src, dest):
    try:
        shutil.copy(src, dest)
        print(f"Copied file '{src}' to '{dest}'.")
    except Exception as e:
        print(f"Error copying file: {e}")

def rename_directory(src, dest):
    try:
        os.rename(src, dest)
        print(f"Renamed directory '{src}' to '{dest}'.")
    except Exception as e:
        print(f"Error renaming directory: {e}")

# List all files and directories
list_files_and_directories()

# Replace 'source_file.txt' and 'copy_file.txt' with your file names
src_file = 'demo.txt'
dest_file = 'fav_quote.txt'
copy_file(src_file, dest_file)

# Replace 'old_directory_name' and 'new_directory_name' with your directory names
old_dir = r'C:\Users\harsh\Desktop\harsha_wipro\python\Day5\assignment'
new_dir = r'C:\Users\harsh\Desktop\harsha_wipro\python\Day5\new_assignment'
rename_directory(old_dir, new_dir)
