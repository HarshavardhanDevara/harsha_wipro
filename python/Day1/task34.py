# str="Python#$123"
# Task is print sum of digits

str="Python#$123"
tot=0
for i in str:
    if i.isdigit():
       tot=tot+int(i)
print(tot)       