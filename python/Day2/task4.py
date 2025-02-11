# Task:we have list called score=[23,45,67,89,12]
# write python script to print how many scores 50 and above and how many less than 50

score=[23,45,67,89,12]
pcnt=0
ncnt=0
for i in score:
    if i>=50:
       pcnt=pcnt+1
    else:
       ncnt=ncnt+1
print(pcnt)
print(ncnt)