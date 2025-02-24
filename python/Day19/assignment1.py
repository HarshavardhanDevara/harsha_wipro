# Task 1 :Check if given String is Pangram or not
# Given a string s, the task is to check if it is Pangram or not. A pangram is a
# sentence containing all letters of the English Alphabet.
# Examples:
# Input: s = “The quick brown fox jumps over the lazy dog”
# Output: true
# Explanation: The input string contains all characters from ‘a’ to ‘z’.
# Input: s = “The quick brown fox jumps over the dog”
# Output: false
# Explanation: The input string does not contain all characters from ‘a’ to ‘z’, as ‘l’, ‘z’, ‘y’ are missing
     

import string
 
def is_pangram(s):
    # Convert to lowercase and remove spaces
    s = s.lower()
    # Get all letters of the alphabet
    alphabet = set(string.ascii_lowercase)
    # Check if all letters are present in the given string
    return alphabet.issubset(set(s))
 

sentence1 = "The quick brown fox jumps over the lazy dog"
sentence2 = "Hello World"
 
print(is_pangram(sentence1))  
print(is_pangram(sentence2))  
