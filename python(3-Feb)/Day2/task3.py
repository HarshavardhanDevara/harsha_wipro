#Task : create an empty list say marks .  add five marks from the console and list

marks=[]
for i in range(5):
    x=int(input("Enter value for marks  "))
    marks.append(x)
print(marks)    

# we have aggregate functions max, min, sum
print("Max marks         " , max(marks))
print("Min marks         " , min(marks))
print("Total             " , sum(marks))
print("Length of list    " , len(marks))