# Task:
# Move to that automation folder list all files that either test at the begining or at the end  of python files
# import pytest
# #to run from this file directly
# pytest.main(["-k", "test or _test"])
# #to run in terminal directly without path
# #pytest -k "test or _test"
import os
import re
 
folder = r"C:\Users\harsh\Desktop\harsha_wipro\python\Day14\automation"
files = os.listdir(folder)
pattern = r"^test_.|._test$"
matching_files = [f for f in files if re.findall(pattern,f)]
 
for file in matching_files:
 print(file)