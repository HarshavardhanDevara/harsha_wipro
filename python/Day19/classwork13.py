# Fractional Knapsack Problem (Greedy Algorithm)
# Here, you can take fractions of an item. We sort items by value/weight ratio and
# take as much as possible.
 
def fractional_knapsack(weights, values, capacity):
    items = sorted(zip(weights, values), key=lambda x: x[1] / x[0], reverse=True)
    total_value = 0
 
    for weight, value in items:
        if capacity >= weight:
            total_value += value
            capacity -= weight
        else:
            total_value += (value / weight) * capacity
            break
 
    return total_value
 
# Example usage
weights = [10, 20, 30]
values = [60, 100, 120]
capacity = 50
print(fractional_knapsack(weights, values, capacity))  # Output: 240.0
 