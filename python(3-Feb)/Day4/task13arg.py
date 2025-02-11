import sys
# total arguments
n = len(sys.argv)
print("Total arguments passed:", n)
# Arguments passed
print("\nName of Python script:", sys.argv[0])
print("\nArguments passed:", end = " ")
for i in range(1, n):
    print(sys.argv[i], end = " ")

max_value = max(int(sys.argv[i]) for i in range(1, n))
print("\n\nMax is:", max_value)


bigger=int(sys.argv[1])
for i in range(2, n):
    if bigger < int(sys.argv[i]):
       bigger=int(sys.argv[i])
print("\n\nBiggest :", bigger)