# Assignment :
# 1. Read two complex numbers  a and b from the console
# 2. method 1 to add two complex nos
# 3. method 2 to subtract  b from a 
# 4. displayComplex() to display complex no
# a=  4+5i
# b=  4+3i
# sum=8+8i
# use Operator overloading
class Complex:
    def __init__(self, real, imag):
        self.real = real
        self.imag = imag
 # Operator overloading for addition
    def __add__(self, other):
        return Complex(self.real + other.real, self.imag + other.imag)
# Operator overloading for subtraction
    def __sub__(self, other):
        return Complex(self.real - other.real, self.imag - other.imag)

    def display(self):
        print(f"{self.real} + {self.imag}i")

# Read two complex numbers from the console
real1, imag1 = map(int, input("Enter real and imaginary part of first complex number: ").split())
real2, imag2 = map(int, input("Enter real and imaginary part of second complex number: ").split())

a = Complex(real1, imag1)
b = Complex(real2, imag2)

# Add and subtract complex numbers
sum_result = a + b
sub_result = a - b

# Display results
print("Sum of the complex numbers:")
sum_result.display()

print("Subtraction of the complex numbers:")
sub_result.display()
