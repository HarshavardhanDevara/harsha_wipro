from itertools import combinations
numbers=[2, 3, 5, 6, 8]
target=8
for r in range(len(numbers) + 1):
    for subset in combinations(numbers, r):
        print(subset)                 
        #if sum(subset) == target:
             # print(subset)