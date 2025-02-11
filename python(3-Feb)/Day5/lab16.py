class Animal:           # Animal is the base class
    def __speak(self):  # __speak is private, can be accessed within the class in which it is defined          
        print("Animal Speaking")

    def speak(self):    # Adding a public method to access the private method
        self.__speak()

# Child class Dog inherits the base class Animal 
class Dog(Animal):      # Dog is the derived class 
    def bark(self):  
        print("dog barking")  

d = Dog()  
d.bark()  
d.speak()  # Accessing the private method through a public method