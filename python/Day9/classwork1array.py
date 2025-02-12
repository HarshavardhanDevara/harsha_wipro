import array
arr = array.array('i', [10, 20, 30, 40, 50])
arr[2] = 99  # Update 3rd element
print(arr)  # Output: array('i', [10, 20, 99, 40, 50]
arr.remove(20)  # Remove by value
print(arr)  # Output: array('i', [10, 99, 40, 50])
del arr[1]  # Remove by index
print(arr)  # Output: array('i', [10, 40, 50])
arr.reverse()
print(arr)  # Output: array('i', [50, 40, 10])

