class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
 
    def __add__(self, other):
        return Point(self.x + other.x, self.y + other.y)

 
    def __str__(self):
        return f"({self.x}, {self.y})"
 
# Creating objects
p1 = Point(1, 2)
p2 = Point(3, 4)
 
# Using operator overloading
p3 = p1 + p2
print(p3)  # Output: (4, 6)
 