def get_integer_input():
    try:
        x = int(input("Enter an integer value: "))
        return x
    except ValueError:
        print("Error: Invalid input, input a valid integer.")

n = get_integer_input()
print("Input value:", n)


 