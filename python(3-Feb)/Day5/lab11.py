class Animal:
    def speak(self):
        print("Animal speaking")
class Dog(Animal):
    def bark(self):
        print("Dog barking")
class Dogchild(Dog):
    def eat(self):
        print("eating bread")
        
d= Dogchild()
d.bark()
d.speak()             #inheritance
d.eat()