# Task 2 :
# read name , m1 and m2 from the console for 3 students and store it in marks.txt
# read name and marks m1 and m2 from marks.txt and print in the following format
# Name   m1   m2   total
# ****   50   60   110
# ****   80   70   150
# ****   60   60   120
f=open("marks.txt" ,"w")
for i in range(3):
    name=input("Enter name   ")
    m1=input("Enter value for marks 1  ")
    m2=input("Enter value for marks 2   ")
    f.write(name+" "+m1+" "+m2+"\n")
f.close()
 
f=open("marks.txt" )
print("name  m1  m2 total")
for i in f:
    str=i.split(" ")
    name=str[0]
    m1=str[1]
    m2=str[2]
    total=int(m1)+int(m2)
    print(name,m1,m2,total)
f.close()    