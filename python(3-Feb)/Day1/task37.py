#  Read value for N .[ Max value is 6 ].
#    find factorial of N
#     !N = 1*2*3 ....(N-1)*N

n=int(input("Enter value for n  "))
f=1
for i in range(2,n+1):
    f=f*i

print("Factorial of " , n , " is   " , f)
