# Assignment 1:
# Create list containing 10 values [values can be int, float]. All these 10 values must be read
# from the console. Read value for x from the console. Print x is in list or not in the list
# use linear search algorithm

# Initialize an empty list
a = []

# Read 10 values from the console and append them to the list
for i in range(10):
    b = float(input("Enter value for the list: "))
    a.append(b)

# Read the value for x from the console
x = float(input("Enter value for x to be searched: "))

# Initialize a flag to indicate if x is found
flag = False

# Perform linear search to check if x is in the list
for i in range(10):
    if a[i] == x:
        flag = True
        break

# Print the result
if flag:
    print(x, "is found and its index position is", i)
else:
    print(x, "is not found in the list")
    
    
    
    
    
    