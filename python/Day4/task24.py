class Person:  
    company = "Wipro Bangalore"     # This is a class variable  
    def __init__(self, name, age):  
 
        self.name = name    # This is an instance variable  
        self.age = age  
 
    def greet(self): 
        print("\nHello, my name is " + self.name) 
        print("My age is          ", self.age)  
        print("My company name    " , Person.company)
 
person1 = Person("Ayan", 25)  
person2 = Person("Bobby", 30)  
person1.greet()
person2.greet()