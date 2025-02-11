x = 20  # Global variable
def my_function():
    global x  # Using the global variable
    x = 30  # Modifying the global variable
    print("Inside function:", x)
 
my_function()
print("Outside function:", x)  # x is modified globally