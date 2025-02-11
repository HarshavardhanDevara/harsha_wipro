my_list = [1, 2, 3]
 
my_iterator = iter(my_list)
 
try:
 
    while True:
        item = next(my_iterator)
        print(item)
except StopIteration:
    print("End of iterator reached!")