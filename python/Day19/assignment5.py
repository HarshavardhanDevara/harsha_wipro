# Check if Strings Are Rotations of Each Other
# Given two string s1 and s2 of same length, the task is to check whether s2 is a rotation of s1.
# Examples:
# Input: s1 = “abcd”, s2 = “cdab”
# Output: true
# Explanation: After 2 right rotations, s1 will become equal to s2.
# Input: s1 = “aab”, s2 = “aba”
# Output: true
# Explanation: After 1 left rotation, s1 will become equal to s2.
# Input: s1 = “abcd”, s2 = “acbd”
# Output: false
# Explanation: Strings are not rotations of each other.

def are_rotations(s1, s2):
    return len(s1) == len(s2) and s2 in (s1 + s1)


print(are_rotations("abcd", "cdab"))  
print(are_rotations("aab", "aba"))    
print(are_rotations("abcd", "acbd")) 
