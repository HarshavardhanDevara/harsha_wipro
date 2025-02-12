arr = [10, 20, 30, 40, 50]
arr[2] = 99  # Update the 3rd element
print(arr)  # Output: [10, 20, 99, 40, 50]
arr.remove(20)  # Remove element by value
print(arr)  # Output: [10, 99, 40, 50]
del arr[1]  # Remove element by index
print(arr)  # Output: [10, 40, 50]
arr.reverse()
print(arr)  # Output: [50, 40, 10]
# Alternative way using slicing:
print(arr[::-1])  # Output: [50, 40, 10]