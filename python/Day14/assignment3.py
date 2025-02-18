from collections import Counter

def is_anagram_sort(str1, str2):
    return sorted(str1) == sorted(str2)

def is_anagram_counter(str1, str2):
    return Counter(str1) == Counter(str2)

def check_anagram(str1, str2):
    """Returns a message indicating whether the strings are anagrams"""
    str1, str2 = str1.replace(" ", "").lower(), str2.replace(" ", "").lower()
    
    if is_anagram_sort(str1, str2):
        return "It is an Anagram (Using Sorting)"
    if is_anagram_counter(str1, str2):
        return "It is an Anagram (Using Counter)"
    
    return "Not an Anagram"
