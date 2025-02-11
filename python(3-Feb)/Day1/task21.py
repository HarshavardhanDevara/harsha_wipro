#break : this statement is used to exit from the loop
#continue : this ignores current iteration and control goes to next iteration
# i want to print nos frm 1 to 12 , except 8

for i in range(1,13):
    if i==8:
       continue
    else:
       print(i)
