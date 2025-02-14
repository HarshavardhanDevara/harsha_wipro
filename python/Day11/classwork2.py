import pdb
 
 
age=int(input("Enter value for age " ))
 
pdb.set_trace()  # Start debugger
 
if age>=21:
   print("Eligible to vote  ")
else:
   print("Not Eligiblte to vote")
 
print("Program ends   ")