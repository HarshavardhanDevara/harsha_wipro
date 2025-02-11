num=[1,2,3,4,5,6,7,8,9]
op = [n*n for n in num]  #squares of numbers
print(op)

op=[]
for n in num:
    x=n*n
    op.append(x)
print(op)