# define a class Rectangle . Initialize width and breadth using constructor
# define two methos  findArea() and findCircum() to get area and circumference of rectangle.
# create an object say r1 with 5 and 6 as width and breadth.
# print its area and circumference
class Rectangle:
    def __init__(self, width, breadth):
        self.width = width
        self.breadth = breadth
    def findArea(self):
        return self.width * self.breadth
    def findCircum(self):
        return 2 * (self.width + self.breadth)
r1 = Rectangle(5, 6)
print("Area:", r1.findArea())
print("Circumference:", r1.findCircum())