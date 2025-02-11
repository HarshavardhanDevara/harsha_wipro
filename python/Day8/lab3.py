class Vehicle:
    def move(self):
        print("I'm moving!")
 
class Car(Vehicle):
    def move(self):
        print("I'm driving on the road!")
 
class Boat(Vehicle):
    def move(self):
        print("I'm sailing on the water!")
 
# Creating objects
vehicle = Vehicle()
car = Car()
boat = Boat()
 
# Using method overriding
vehicle.move()  # Output: I'm moving!
car.move()      # Output: I'm driving on the road!
boat.move()     # Output: I'm sailing on the water!