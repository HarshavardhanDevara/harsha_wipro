f=open("marks.txt" ,"w")
for i in range(2):
    name=input("Enter name   ")
    m1=input("Enter value for marks 1  ")
    m2=input("Enter value for marks 2   ")
    f.write(name+" "+m1+" "+m2+"\n")
f.close()
 
f=open("marks.txt" )
print("\n\n******************")
for i in f:
    str=i.split(" ")
    name=str[0]
    m1=str[1]
    m2=str[2]
    total=int(m1)+int(m2)
    print("Name    " , name)
    print("Mark1   " , m1)
    print("Mark2   " , m2)
    print("Total   " , total)
    print("******************")
f.close()    