# Task :45 55  -65 -75  5  - 10   [ to stop enter 0 ]
# Sum of pos nos  : 105
# Sum of neg nos  : -150


psum=0
nsum=0
while True:
  x=int(input("Enter value for  x, To stop enter 0 " ))

  if x==0:
     break

  if x > 0:
     psum=psum+x 

  if x < 0:
     nsum=nsum+x


print("Sum of  positive nos  " ,  psum)
print("Sum of  negative nos  " ,  nsum)