class Duck:
    def quack(self):
        print("Quack, quack!")
 
class Person:
    def quack(self):
        print("I'm pretending to be a duck!")
 
def make_it_quack(thing):
    thing.quack()
 
# Creating objects
duck = Duck()
person = Person()
 
# Using duck typing
make_it_quack(duck)    # Output: Quack, quack!
make_it_quack(person)  # Output: I'm pretending to be a duck!




