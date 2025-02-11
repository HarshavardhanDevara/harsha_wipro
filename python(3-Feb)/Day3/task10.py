f=open("marks.txt", "w")
for i in range(3):
    name=input("enter name  ")
    m1=int(input("enter marks "))
    m2=int(input("enter marks "))
    total=(m1+m2)
    f.write(name+" "+m1+" "+m2+" "+total)
f.close()
f=open("marks.txt")
print(f.read())

