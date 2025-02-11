# task read marks and print grade based on the rule given below
# marks                Grade
# >80                  First Grade
# 60-80                Second grade
# >=40 and <60         third Grade
# < 40                 Fail

marks=int(input("Enter marks   "))

if marks>80:
   print("First Grade   ")

if marks>=60 and marks <=80:
   print("Second Grade  ")

if marks>=40 and marks <60 :
   print("Third Grade  ")

if marks <40:
   print("Fail")