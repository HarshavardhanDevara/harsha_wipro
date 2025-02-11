x=[2,3,4,5]
y=[]
for i in x:
    va=i+2
    y.append(va)
print(x)
print(y)
#method 2 by map and lambda
x=[2,3,4,5]
y=map(lambda a:a+2, x)   #to print inputs by add 2
print(list(y))

x=[1,2,3,4,5]
y=map(lambda a:a**2, x)  #sqr by map
print(list(y))
y=map(lambda a:a**3, x)   #cub by map
print(list(y))
y=map(lambda a:a*a, x)    #sqr
print(list(y))
y=map(lambda a:a*a*a, x)   #cub
print(list(y))