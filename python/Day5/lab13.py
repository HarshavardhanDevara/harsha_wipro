class Animal:
    def _speak(self):
        print("Animal speaking")
class Dog(Animal):
    def bark(self):
        print("Dog barking")
d= Dog()
d.bark()
d._speak()