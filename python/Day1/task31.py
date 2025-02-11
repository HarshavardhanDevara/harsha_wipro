# The rstrip() method removes trailing whitespace characters from a string.
# The lstrip() method removes leading whitespace characters from a string. 
# strip() removes whitespaces from both ends

nos=input("Enter value for nos  ")
nos=nos.strip()
tot=0
for i in nos:
    tot=tot+int(i)
    
print("total of digits  " , tot)