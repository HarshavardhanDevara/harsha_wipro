class Animal:
    def speak(self):
        pass
 
class Dog(Animal):
    def speak(self):
        return "Woof!"
 
class Cat(Animal):
    def speak(self):
        return "Meow!"
 
def animal_sound(animal):
    print(animal.speak())
 
# Creating objects
dog = Dog()
cat = Cat()
 
# Using polymorphism
animal_sound(dog)  # Output: Woof!
animal_sound(cat)  # Output: Meow!