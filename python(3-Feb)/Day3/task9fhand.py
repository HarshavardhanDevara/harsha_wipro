f=open("names.txt", "w")
for i in range(5):
    name=input("enter name  ")
    f.write(name+"\n")
f.close()