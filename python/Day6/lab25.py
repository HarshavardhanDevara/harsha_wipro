import re

text = "apple 123 banana 456 cherry 789"

# Regular expression to match numbers
pattern = r"\d+"

# Using finditer
matches = re.finditer(pattern, text)

# Iterating over matches
for match in matches:
    print(f"Match: {match.group()}, Start: {match.start()}, End: {match.end()}")