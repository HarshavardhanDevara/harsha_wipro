import re
txt = "Hi hello planet"
#Check if the string starts with 'hello':
x = re.search("^hello", txt)   # search method returns true if match , otherwise false
if x:
  print("Yes, the string starts with 'hello'")
else:
  print("No match")
 

txt = "Hi hello planet"
#Check if the string starts with 'hello':
x = re.search("^Hi", txt)   # search method returns true if match , otherwise false
if x:
  print("Yes, the string starts with 'hello'")
else:
  print("No match")

x = re.search("^hi", txt)   # search method returns true if match , otherwise false
if x:
  print("Yes, the string starts with 'hello'")
else:
  print("No match")