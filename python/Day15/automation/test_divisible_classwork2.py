# Create a new file test_div_by_13.py
 
import pytest
 
def test_divisible_by_13(input_value):
   assert input_value % 13 == 0
   
   
# pytest -k divisible -v
# import re
# and findall
# pytest -k "test or _test"