# Split a string on hyphens
# Write a program to split a given string on hyphens and display each substring.
# str1 = Emma-is-a-data-scientist
# Expected Output:
# Displaying each substring
# Emma
# is
# a
# data
# scientist
str1 = "Emma-is-a-data-scientist"
substrings = str1.split('-')
print("Displaying each substring")
for substring in substrings:
    print(substring)