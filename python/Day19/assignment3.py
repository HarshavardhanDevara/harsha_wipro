# Reverse words in a string
# Given a string str, the task is to reverse the order of the words in the given string.
# Note that str may contain leading or trailing dots(.) or multiple trailing dots(.)
# between two words. The returned string should only have a single dot(.) separating the words.
# Examples:
# Input: str = “i.like.this.program.very.much” 
# Output: str = “much.very.program.this.like.i” 
def reverse_words(s):
    words = s.split(".")  # Split by dots
    words = [word for word in words if word]  # Remove empty strings (caused by multiple dots)
    return ".".join(reversed(words))  # Reverse and join with a single dot

print(reverse_words("i.like.this.program.very.much"))  

