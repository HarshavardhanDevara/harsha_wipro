#looping: A set of statements executed for a fixed no of times or as long as the condition is true


#range(5)  , starts from 0 and ends with 4 , increment is 1

#range(1,5)  , sv=1  , fv=4 , incr is 1

#range(1,10,2) , iv=1,  fv=9, increment is 2

 
for x in range(5):  # 0,1,2,3,4
    print(x)

print("\n")  # \n makes one line spaces
for x in range(2,10):
    print(x)
    
print("\n") 
for x in range(1,10,2): # 1,3,5,7,9
    print(x)