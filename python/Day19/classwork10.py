from itertools import combinations
 
def find_combinations(numbers, target):
    return [list(subset) for r in range(len(numbers) + 1)
                        for subset in combinations(numbers, r)
                        if sum(subset) == target]
 
print(find_combinations([2, 3, 5, 6, 8], 8))