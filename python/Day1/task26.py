# Task :
#   Read name from the console .
#   count how many vowels in the string
#  input murugadoss
# output : 4

name=input("Enter name  ")  # string is an object
str=name.lower()
cnt=0
for i in str:
    if i=='a' or i=='e' or i=='i' or i=='o' or i=='u':
       cnt=cnt+1 
print("No of vowels in "  , name , " is  " , cnt )