# The finditer() method in the re (regular expressions) module returns
# an iterator yielding match objects for all non-overlapping matches of
# a pattern in a string. This is useful when you need to find multiple
# occurrences and work with them efficiently.
# import re
# re.finditer(pattern, string, flags=0)
# pattern: The regex pattern to search for.
# string: The input string where the search is performed.
# flags (optional): Modifiers like re.IGNORECASE.

import re
s = 'Readability counts.'
pattern = r'[aeoui]'
matches = re.finditer(pattern, s)
for match in matches:
    print(match)
    