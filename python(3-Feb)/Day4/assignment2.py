# a) An Adam number is a number for which the square of the number, when its digits are reversed and 
# is equal to the square of the number obtained by reversing the digits. For example the number 22 is an adam number because,
# the square of 22 is 484 and the reverse of 484 is also 484, So the reversed square and the square of the reversed number
# are equal thus making it an adam number.

num = int(input("Enter a number: "))
square = num ** 2
reverse_num = int(str(num)[::-1])
reverse_square = reverse_num ** 2

if int(str(square)[::-1]) == reverse_square:
    print(num, "is an Adam number.")
else:
    print(num, "is not an Adam number.")

