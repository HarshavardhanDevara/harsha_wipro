import re
panno=input("Enter your pandcard no without spaces ") 
'''
The valid PAN Card number must satisfy the following conditions: 
It should be ten characters long.
The first five characters should be any upper case alphabets.
The next four-characters should be any number from 0 to 9.
The last(tenth) character should be any upper case alphabet.
It  contains any white spaces.
'''
x = re.search("[A-Z]{5}\\s[0-9]{4}\\s[A-Z]{1}", panno)
 
if x:
   print("valid pandcard      ")
else:
   print("Invalid pancard     ")