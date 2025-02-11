import re
txt = "harsha vardhan"
#Check if the string if ends with doss :
# $ symbol is used to match at the end
x = re.search("vardhan$", txt)   
# search method returns true if match , otherwise false
if x:
  print("Yes, the string ends  vardhan")
else:
  print("No  ")


x = re.search("harsha$", txt)   
# search method returns true if match , otherwise false
if x:
  print("Yes, the string ends  vardhan")
else:
  print("No  ")

x = re.search("Vardhan$", txt)   
# search method returns true if match , otherwise false
if x:
  print("Yes, the string ends  vardhan")
else:
  print("No  ")