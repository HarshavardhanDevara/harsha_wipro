# 2 .Group Anagrams Together:
# Given an array of words arr[], the task is to groups strings that are anagrams.
# An anagram is a word or phrase formed by rearranging the letters of another,
# using all the original letters exactly once.
# Example:
# Input: arr[] = [“act”, “god”, “cat”, “dog”, “tac”]
# Output: [[“act”, “cat”, “tac”], [“god”, “dog”]]
# Explanation: There are 2 groups of anagrams “god”, “dog” make group 1. “act”, “cat”, “tac” make group 2.
# Input: arr[] = [“listen”, “silent”, “enlist”, “abc”, “cab”, “bac”, “rat”, “tar”, “art”]
# Output: [[“abc”, “cab”, “bac”], [“listen”, “silent”, “enlist”],[“rat”, “tar”, “art”]]
# Explanation: 
# Group 1: “abc”, “bac” and “cab” are anagrams.
# Group 2: “listen”, “silent” and “enlist” are anagrams.
# Group 3: “rat”, “tar” and “art” are anagrams

from collections import defaultdict
 
def group_anagrams(words):
    anagrams = defaultdict(list)
 
    for word in words:
        # Sort the word and use it as a key
        sorted_word = ''.join(sorted(word))
        anagrams[sorted_word].append(word)
 
    # Convert the dictionary values to a list
    return list(anagrams.values())
 
words_list = ["eat", "tea", "tan", "ate", "nat", "bat"]
print(group_anagrams(words_list))
print(group_anagrams(["act", "god", "cat", "dog", "tac"]))  
print(group_anagrams(["listen", "silent", "enlist", "abc", "cab", "bac", "rat", "tar", "art"]))

