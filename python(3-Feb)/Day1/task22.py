# i want to print nos from 1 to 12 , except  5 and 8

for i in range(1,13):
    if i==5 or i==8 :
       continue  # continue ignores current iteration and executes next iteration
    else:
       print(i)
