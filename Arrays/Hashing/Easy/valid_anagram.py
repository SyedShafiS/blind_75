# 242. Valid Anagram

# Given two strings s and t, return true if t is an anagram of s, and false otherwise.

 

# Example 1:

# Input: s = "anagram", t = "nagaram"

# Output: true

# Example 2:

# Input: s = "rat", t = "car"

# Output: false


# 3 ways to approach 
# -> using Counter()
# -> using sorted()
# -> using loop

#using Counter()
from collections import Counter
def valid_anagram(string_1 , string_2):
    if Counter(string_1) == Counter(string_2):
        return True
    
#using sorted()
def valid_anagram(string_1 , string_2):
    if sorted(string_1) == sorted(string_2):
        return True
    

# using for loop manually