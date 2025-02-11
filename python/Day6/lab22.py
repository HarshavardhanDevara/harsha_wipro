# Write a  Python program that executes an operation on a list and handles an IndexError
# exception if the index is out of range.
# Define a function named test_index that takes 'data' and 'index' as parameters.

marks=[1,2,3]
print(marks[5])
def test_index(data, index):
 
    try:
        result = data[index]
        print("Result:", result)
    except IndexError:
        print("Error: Index out of range.")
 
# Define a list of numbers 'nums'.
nums = [1, 2, 3, 4, 5, 6, 7]
index = int(input("Input the index: "))
test_index(nums, index)