def find_subsets(numbers, target, start=0, path=[], res=[]):
    if sum(path) == target:
        res.append(path)
        return res
    for i in range(start, len(numbers)):
        find_subsets(numbers, target, i + 1, path + [numbers[i]], res)
    return res
 
print(find_subsets([2, 3, 5, 6, 8], 8))