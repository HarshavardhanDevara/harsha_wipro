# Removal all characters from a string except integers
# Given:
# str1 = 'I am 25 years and 10 months old'
# Expected Output:
str1 = 'I am 25 years and 10 months old'
result = ''.join(filter(str.isdigit, str1))
print(result)