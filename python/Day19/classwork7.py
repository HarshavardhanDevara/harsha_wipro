#Suppose we have a knapsack which can hold int w = 10 weight units. 
# We have a total of int n = 4 items to choose from, 
# whose values are represented by an array int[] val = {10, 40, 30, 50} and 
# weights represented by an array int[] wt = {5, 4, 6, 3}
def knapsack(w, wt, val, n):
    # Creating a 2D DP table
    dp = [[0 for _ in range(w + 1)] for _ in range(n + 1)]

    # Building the table
    for i in range(1, n + 1):
        for j in range(1, w + 1):
            if wt[i - 1] <= j:  # If item can fit in the knapsack
                dp[i][j] = max(val[i - 1] + dp[i - 1][j - wt[i - 1]], dp[i - 1][j])
            else:
                dp[i][j] = dp[i - 1][j]

    return dp[n][w]  # Maximum value possible

# Given inputs
w = 10
n = 4
val = [10, 40, 30, 50]
wt = [5, 4, 6, 3]

# Calling function
max_value = knapsack(w, wt, val, n)
print(max_value)
