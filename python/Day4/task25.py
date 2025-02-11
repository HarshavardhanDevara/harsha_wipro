class Circle:  
    def __init__(self, rad):  
         self.radius= rad  
    def findArea(self): 
        area=3.14*self.radius*self.radius
        print("Area of Circle " , area)
c1=Circle(5)
c1.findArea()

