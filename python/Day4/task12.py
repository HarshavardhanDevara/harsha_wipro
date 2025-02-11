import re
txt = "The rain in Spain falls mainly in the stays"
#Check if the string contains either "falls" or "stays":
x = re.findall("falls|stay", txt)
print(x)
if x:
  print("Yes, there is at least one match!")
else:
  print("No match")

import re
txt = "hello planet"
#Search for a sequence that starts with "he", followed by 1 or more  (any) characters, and an "o":
x = re.search("he.+o", txt)
if x:
   print("There is a match ")
else:
   print("There is no match  ")


   import re
txt = "helo planet"
#Search for a sequence that starts with "he", followed by 0 or 1  (any) character, 
# and an "o":
x = re.search("he.?o", txt)
if x:
   print("There is a match")
else:
   print("No Match  ")


   import re

txt = "hello planet"

#Search for a sequence that starts with "he", followed by 0 or more  (any) characters, and an "o":

x = re.findall("he.*o", txt)

print(x)
