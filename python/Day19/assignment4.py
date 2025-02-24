# Isomorphic Strings Check
# Two strings s1 and s2 are called isomorphic if there is a one-to-one mapping possible
# for every character of s1 to every character of s2. And all occurrences of every 
# character in ‘s1’ map to the same character in ‘s2’.
# Examples:
# Input:  s1 = “aab”, s2 = “xxy”
# Output: True
# Explanation: ‘a’ is mapped to ‘x’ and ‘b’ is mapped to ‘y’.
# Input:  s1 = “aab”, s2 = “xyz”
# Output: False
# Explanation: One occurrence of ‘a’ in s1 has ‘x’ in s2 and other occurrence of ‘a’ has ‘y’
def is_isomorphic(s1, s2):
    return len(set(s1)) == len(set(s2)) == len(set(zip(s1, s2)))

print(is_isomorphic("aab", "xxy"))  
print(is_isomorphic("aab", "xyz"))  
