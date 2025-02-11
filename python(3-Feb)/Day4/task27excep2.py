try:
    a=int(input("Enter value for a  "))
    b=int(input("Enter value for b " ))
    c=a/b
    print(c)
except ZeroDivisionError as e:
     print("Division by zero is not allowed ")
 
else :
     print("Program works fine ")
 
finally:
     print("Program ends")