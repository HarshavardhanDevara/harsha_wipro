def greet(name):
 
    # inner function
 
    def display_name():
 
        print("Hi", name)
 
    
    # call inner function
 
    display_name()
 
# call outer function
 
greet("John")  