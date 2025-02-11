# In Python, you can use the endswith() method to check if a string ends with a specified suffix.
# string.endswith(suffix[, start[, end]])
# suffix: The string or a tuple of strings to check.
# start (optional): The starting index to check from.
# end (optional): The ending index to check up to (exclusive).

text = "hello.py"
# Basic usage
print(text.endswith(".py"))  # Output: True
print(text.endswith(".txt"))  # Output: False
 
# Using start and end index
print(text.endswith("lo", 0, 5))  # Output: True
 
# Checking multiple suffixes
print(text.endswith((".py", ".txt", ".java")))  # Output: True