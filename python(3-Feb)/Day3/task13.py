
# Task :
 
# 1 Read name and marks for 3 students from the console and store in stud.txt
# 2.Read names and marks from the stud.txt and print onto the console in the following format
 
# ***************************************************
# Name        marks
# ***************************************************
# ***          55
# ***************************************************
# ****         60
# ***************************************************

f=open("stud.txt", "w")
for i in range(3):
    name=input("Enter value for name  ")
    marks=input("Enter marks         ")
    f.write(name+" "+marks+"\n")
 
f.close()
 
f=open("stud.txt")
print("************************")
print("Name   Marks          ")
print("************************")
for i in f:
    str=i.split(" ")
    name=str[0]
    marks=str[1]
    print(name+"  "+marks)
 
print("************************")
 
f.close()