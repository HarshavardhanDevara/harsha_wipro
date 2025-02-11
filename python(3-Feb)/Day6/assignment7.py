#Exercise 7: Check if a value exists in a dictionary
sample_dict = {'a': 100, 'b': 200, 'c': 300}  
value_to_check = 200

if value_to_check in sample_dict.values():
    print(f"{value_to_check} exists in the dictionary")
else:
    print(f"{value_to_check} does not exist in the dictionary")