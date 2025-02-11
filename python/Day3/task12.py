f = open(r"C:\Users\harsh\Desktop\python_dt_b2\python\Day3\names.txt")  # r mode is the default 
print(f.read())  # read() reads entire file 
f.close()

f = open(r"C:\Users\harsh\Desktop\python_dt_b2\python\Day3\names.txt")  # r mode is the default 
print(f.readline())  # readline() reads one line at a time 
f.close()

f = open(r"C:\Users\harsh\Desktop\python_dt_b2\python\Day3\names.txt")  # r mode is the default 
print(f.read(3))  # read(3) reads three bytes 
f.close()