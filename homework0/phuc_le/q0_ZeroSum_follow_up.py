'''
    Go through each elements in the inputs
    For each k elements, find the -k element in the hashmap
    If -k in in hashmap, pairs += count of -k in map
    else: increment the value of k in map
    Maintain a hashmap: {number: count}

    Check the for -k in map first then add because edge case: 0

    n: numbers of elements in the input
    Time: O(n)
    Space: O(n)
    
    Spend around 5 minutes
'''
from typing import List

def ZeroSum(nums: List[int]) -> int:
    mp = {}
    pairs = 0
    for n in nums:
        if -n in mp:
            pairs += mp[-n]
        if n in mp:
            mp[n] += 1
        else:
            mp[n] = 1
    return pairs

nums = [1, 10, 8, 3, 2, 5, 7, 2, -2, -1]
print(ZeroSum(nums))
nums = [1, 10, 8, -2, 2, 5, 7, 2, -2, -1]
print(ZeroSum(nums))
nums = [4, 3, 3, 5, 7, 0, 2, 3, 8, 6]
print(ZeroSum(nums))
nums = [4, 3, 3, 5, 7, 0, 2, 3, 8, 0]
print(ZeroSum(nums))