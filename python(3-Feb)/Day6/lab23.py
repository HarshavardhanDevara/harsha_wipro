class Calculator:
    def add(self, a, b=0):
        return a + b
 
# Creating an instance of Calculator
calc = Calculator()
 
# Using the add method with one argument
print(calc.add(5))  # Output: 5
 
# Using the add method with two arguments
print(calc.add(5, 3.5))  # Output: 8
