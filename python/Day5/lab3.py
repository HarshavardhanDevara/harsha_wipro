class Student:
    def __init__(self):
        print("this is not parametrized constructor")
    def show(self,name):
        print("hello", name)
student=Student()
student.show("john")