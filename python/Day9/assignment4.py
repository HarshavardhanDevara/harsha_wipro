# Assignment 4: For the given list of values  , 
# write python script to sort  using selection sort and display
def selection_sort(arr):
    for i in range(len(arr)):
        min_idx = i
        for j in range(i+1, len(arr)):
            if arr[min_idx] > arr[j]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]

    return arr

values = [64, 25, 12, 22, 11, 44, 18, 2]
sorted_values = selection_sort(values)
print("Sorted array is:", sorted_values)