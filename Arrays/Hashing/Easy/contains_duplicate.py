# 217. Contains Duplicate
# Given an integer array nums, return true if any value appears at least twice in the array, and return false if every element is distinct.

 
# Example 1:

# Input: nums = [1,2,3,1]

# Output: true

# Explanation:

# The element 1 occurs at the indices 0 and 3.

#o(n) in time comp...
def contains_duplicate(arr):
    have_seen = {}

    for i , nums in enumerate(arr):
        if nums in have_seen:
            # return True # for returning true or not
            return have_seen[nums] , i # for returning the index positions
        
        else:
            have_seen[nums] = i


print(contains_duplicate([1,2,3,1]))
