class Animal:           #animal is base class
    def _speak(self):   # _speak is protected, can be accessed within the class and its subclasses          
        print("Animal Speaking")
 
#child class Dog inherits the base class Animal 
class Dog(Animal):                           # dog is derived class 
    def bark(self):  
        print("dog barking")
        self._speak()
d = Dog()  
d.bark()  
# d._speak()  # This line should be removed to avoid accessing the protected method directly

