
# The zip() function in Python combines multiple iterables such as lists, tuples, strings, 
# dict etc, into a single iterator of tuples. Each tuple contains elements from the input iterables
# that are at the same position.
names = ['John', 'Alice', 'Bob', 'Lucy']
scores = [85, 90, 78, 92]
res = zip(names, scores)
print(list(res))