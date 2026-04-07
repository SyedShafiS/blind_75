# 219. Contains Duplicate II

# Given an integer array nums and an integer k, return true if there are two distinct indices i and j in the array such that nums[i] == nums[j] and abs(i - j) <= k.

 

# Example 1:

# Input: nums = [1,2,3,1], k = 3
# Output: true
# Example 2:

# Input: nums = [1,0,1,1], k = 1
# Output: true
# Example 3:

# Input: nums = [1,2,3,1,2,3], k = 2
# Output: false


def contains_duplicate_2(arr , target):
    have_seen = {}

    for i , nums in enumerate(arr):
        if nums in have_seen:
            if abs(i - have_seen[nums]) <= target:
                return True
            
        have_seen[nums] = i


    else:
        return False
    

print(contains_duplicate_2([1,2,3,1,2,3],2))