#str="Doss 50 60"
#doss is name
#50 and 60 are scores of two subjects
#i need the following output
# Name    : doss
# Marks1  : 50
# Marks2  : 60
# Total   : 110

str="Harsha,50,60"
st=str.split(",")
print("Name   =" , st[0])
print("Marks 1   = " , st[1])
print("Marks 2   = " , st[2])
print("Total     =" , int(st[1])+int(st[2]))