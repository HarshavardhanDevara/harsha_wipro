class Calculations1:
    def Summation(self,a,b):
         return a+b
class Calculations2:
    def Multiplication(self,a,b):
         return a*b
class Derived(Calculations1,Calculations2):
     def Divide(self,a,b):
         return a/b
d = Derived()
print(d.Summation(10,20))
print(d.Multiplication(10,20))
print(d.Divide(10,20))
         
     
