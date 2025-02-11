import re
txt = "welcome Hello planet"
#Search for a sequence that starts with "he", followed by two (any) characters,
#and an "o":
x = re.search("[Hh]e..o", txt)
if x:
   print("Match")
else:
   print("No match")    