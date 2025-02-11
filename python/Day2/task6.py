score=[23,45,67,89,12]
pmarks=[ i  for i in score if i>=50]
fmarks=[ i   for i in score if i<50]
print(score)
print("\n List contains marks 50 and above  " ,pmarks)
print("List contains marks < 50             ",fmarks)
