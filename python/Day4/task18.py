a={1,2,3,4}
b={4,5,6}
c=a.union(b)  # union operator removes duplicates
print(c)
d =a | b    # union operator | removes duplicates
print(d)
a={1,2,4,5}
b={4,5,6}
print(a-b)  # set of elements in a but not in b
