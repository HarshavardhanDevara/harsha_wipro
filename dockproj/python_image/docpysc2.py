#Assignment1
def find_bigger_number(a, b):
    if a > b:
        return a
    else:
        return b

a = 10
b = 20

bigger_number = find_bigger_number(a, b)
print(f"The bigger number between {a} and {b} is: {bigger_number}")
