# In Python, you can use the startswith() method for strings to check if a string starts with a specified prefix.
# string.startswith(prefix[, start[, end]])
# prefix: The string or tuple of strings to check.
# start (optional): The starting index to check from.
# end (optional): The ending index to check up to (exclusive)
text = "Hello, world!"
# Basic usage
print(text.startswith("Hello"))  # Output: True
print(text.startswith("world"))  # Output: False
 
# Using start index
print(text.startswith("world", 7))  # Output: True
 
# Using start and end index
print(text.startswith("Hello", 0, 5))  # Output: True
 
# Checking multiple prefixes
print(text.startswith(("Hi", "Hello")))  # Output: True
 