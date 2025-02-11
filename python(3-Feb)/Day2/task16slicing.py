a = [1,2,3,4,5,6,7,8,9]  #slicing(starts from zer0)
print(a[1:4])            #to print from index1 to index3 4 will excluded 
print(a[::])             # to print all
print(a[:])
b=a[2:]                  #to print from index2 to last 
print(b)
c=a[:4]                  #to print from zero to index3
print(c)
d=a[::2]                #after 2 
print(d)
e=a[7:15]
print(e)       #outbound slicing not throw error in list while given wrong index at end also 
print(a[15]) #no 15 index but above with slicing no issue
        