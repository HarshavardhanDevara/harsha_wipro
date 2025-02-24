# First, take an empty subset.
# Include the next element, which is at index 0 to the empty set.
# If the subset is equal to the sum value, mark it as a part of the solution.
# If the subset is not a solution and it is less than the sum value, add next element to the subset until a valid solution is found.
# Now, move to the next element in the set and check for another solution until all combinations have been tried.

# Try this algorithm  for subset of sum
# If the last element (arr[n-1]) is greater than sum, we cannot include it in our subset isSubsetSum(arr,n,sum) = isSubsetSum(arr,n-1,sum)
# If the last element is less than or equal to sum, we have two choices:
# Include the last element in the subset, isSubsetSum(arr,n,sum) = isSubsetSum(arr,n-1,sum-arr[n−1])
# Exclude the last element, isSubsetSum(arr,n,sum) = isSubsetSum(arr,n-1,sum)
 
def is_subset_sum(arr, n, target_sum):
    # Base cases
    if target_sum == 0:  
        return True  # Found a subset with required sum
    if n == 0:  
        return False  # No elements left, but sum is not achieved

    # If the last element is greater than target sum, exclude it
    if arr[n - 1] > target_sum:
        return is_subset_sum(arr, n - 1, target_sum)

    # Check if subset can be formed either including or excluding the last element
    return is_subset_sum(arr, n - 1, target_sum) or is_subset_sum(arr, n - 1, target_sum - arr[n - 1])

# Given input
arr = [3, 34, 4, 12, 5, 2]
target_sum = 9
n = len(arr)

# Function call
print(is_subset_sum(arr, n, target_sum)) 
