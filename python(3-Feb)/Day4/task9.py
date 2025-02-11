# Adharcard validation :
# How to check Aadhaar number is valid or not using Regular Expression
# The valid Aadhaar number must satisfy the following conditions:
# It should have 12 digits.
# It should not start with 0 and 1.
# It should not contain any alphabet and special characters.
# It should have white space after every 4 digits.
# has context menu
import re
adharno=input("Enter your aadhar no with spaces ") 
x=re.search("[2-9][0-9]{3}\\s[0-9]{4}\\s[0-9]{4}",adharno)
if x:
    print("valid Aharcard no")
else:
    print("Invalid Adharcard no")