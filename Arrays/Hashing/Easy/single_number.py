#single Number in an array
from collections import defaultdict

def singleNumber(arr):
    freq = defaultdict(int)

    for num in arr:
        freq[num] += 1

    for num , count in freq.items():
        if count == 1:
            return num
        

print(singleNumber([1,1,2,2,3]))