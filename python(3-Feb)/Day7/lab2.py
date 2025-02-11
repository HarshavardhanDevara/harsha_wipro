# Generator expression
 
squares = (x**2 for x in range(5))
 
# Using our generator
for square in squares:
    print(square)