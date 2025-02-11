#FileNotFoundError
try :
    f=open("data.txt")
    print(f.read())
except FileNotFoundError:
    print("There is no such file  ")
 