class Person: 
    def __init__(self, name, age):    # constructor is a method to initialize values 
                                      # for the varibales at the time of creation
                                      # self refers to current  object
                                      # name and age are instance variables
        self.name = name    
        self.age = age  
    def greet(self):  
        print("Hello, my name is " + self.name) 
        print("My age is          ", self.age)      
# Create a new instance of the Person class and assign it to the variable person1  
person1 = Person("Ayan", 25)  
person1.greet()    