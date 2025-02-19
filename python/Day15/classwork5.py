#There are some circumstances when you want to skip tests or run the tests,
#but not count them during PyTest run, then you can use skip and Xfail tests respectively.
 
# Importing the math and pytest libraries
import math
import pytest
 
# Creating first test case
@pytest.mark.skip
def test_floor():
   num = 7
   assert num==math.floor(6.34532)
 
# Creating second test case
def test_equal():
   assert 50 == 50
 
# Creating third test case
@pytest.mark.xfail
def test_difference():
   assert 99-43==56
 
# Creating fourth test case
def test_square_root():
   val=7
   assert val==math.sqrt(49)