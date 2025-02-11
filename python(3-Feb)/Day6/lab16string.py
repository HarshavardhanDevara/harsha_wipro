import re
#The import re statement is used to import the re module,
# which provides support for working with regular expressions in Python. 
# Regular expressions are a powerful tool for matching patterns in text.
#Return a list containing every occurrence of "ai":
txt = "The rain in Spain"
x = re.findall("ai", txt)
print(x)