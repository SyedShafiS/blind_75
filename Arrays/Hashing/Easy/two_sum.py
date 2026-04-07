# Input: nums = [2,7,11,15], target = 9
# Output: [0,1]
# Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].

# o(n) in time complexity
def findTarget(arr , target):
    have_seen = {} # declare dict for storing the index value

    for i , nums in enumerate(arr): #enum() is the property to return an iterable obj with valid indices also

        x = target - nums

        if x in have_seen: # we re returning index position only 
            return (have_seen[x] , i)
        
        else:
            have_seen[nums] = i


print(findTarget([2,7,11,15] , 9))