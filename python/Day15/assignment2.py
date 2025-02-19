# Task: 2 [ Assignment-2 ]
# Move to that automation folder
# 1. list all files that either test at the begining or at the end  of python files
# 2. from the list of files obtained from 1 , list all the files that contains word "divisible" as a
#    part of the file name

import os
import re

base_dir = os.getcwd()
test_pattern = r"^(test_.*\.py|.*_test\.py)$"

test_files = {}
divisible_files = {}

# Search for test files in automation folders
for root, _, files in os.walk(base_dir):
    if "automation" in root.split(os.sep):
        matched_files = [f for f in files if re.findall(test_pattern, f)]
        if matched_files:
            test_files[root] = matched_files
            divisible_matches = [f for f in matched_files if "divisible" in f]
            if divisible_matches:
                divisible_files[root] = divisible_matches

# Print test files grouped by folder
for folder, files in test_files.items():
    print(f"\nFiles from: {folder}")
    print("\n".join(files))

# Print divisible files with their folders
for folder, files in divisible_files.items():
    print(f"\nFiles containing 'divisible' from: {folder}")
    print("\n".join(files))


