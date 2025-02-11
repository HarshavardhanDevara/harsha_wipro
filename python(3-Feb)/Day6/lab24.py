class Calculator:
    def add(self, *args):
        return sum(args)
 
calc = Calculator()
 
print(calc.add(1))  # Output: 1
print(calc.add(1, 2))  # Output: 3
print(calc.add(1, 2, 3, 4))  # Output: 10
 