a = [1, 4, 6, 8, 0, 45, 67]

x = int(input("Enter value to search: "))

flag = False

for i in a:
    if x == i:
        print(x, "is found")
        flag = True
        break

if  flag==False:
    print("Not found")