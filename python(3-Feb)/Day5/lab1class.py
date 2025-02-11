class Employee:
    def __init__(self,name,id):
        self.name=name
        self.id=id
    def display(self):
        print("ID: %d \nName: %s" % (self.id, self.name))
      
emp1 = Employee("John", 101)  
emp2 = Employee("David", 102)  
# accessing display() method to print employee 1 information  
emp1.display() 
emp2.display()