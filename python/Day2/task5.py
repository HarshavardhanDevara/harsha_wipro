score=[23,45,67,89,12]
pmarks=[]
fmarks=[]
for i in score:
    if i >=50:
       pmarks.append(i)
    else:
       fmarks.append(i)

print(score)
print("\nList contains marks 50 and above " , pmarks)
print("List contains marks < 50         " , fmarks)