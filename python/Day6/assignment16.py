#  Return a set of elements present in Set A or B, but not both
set1 = {10, 20, 30, 40, 50}
set2 = {30, 40, 50, 60, 70}
symmetric_difference = set1.symmetric_difference(set2)
print(symmetric_difference)