# read three values from the console, print biggest of three

a=int(input("Enter value for  a   " ))
b=int(input("Enter value for  b   "))
c=int(input("Enter value for  c   "))

if a >=b:
   biggest=a
else:
   biggest=b

if biggest <=c:
   biggest=c

print("Biggest   =" , biggest)
