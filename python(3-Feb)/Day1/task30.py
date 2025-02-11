#read  number say 4567  , print total of its digits 
#Example : 4567 = 4+5+6+7 = 22

nos=input("Enter value for nos  ")
tot=0
for i in nos:
    tot=tot+int(i)
    
print("total of digits  " , tot)    
