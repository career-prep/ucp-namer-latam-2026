'''
    Hashing technique:

    Numbers of sub array sum to zero
    
    Use prefix sum hashmap
    Iterate through the array, keep trach of the current sum
    
    If we are at position j and there is already a sum at position i
    That means between i and j the sum is 0

    Time: O(n)
    Space: O(n)
    n: numbers of elements in the array

    Time spent: 35 mins
'''

from typing import List

def ZeroSumSubArrays(nums: List[int]) -> int:
    # Init the sum at the start to be 0
    prefixSum_map = {0 : 1}

    total, cnt = 0, 0

    for n in nums:
        total += n
        # Find a 0 subarray
        if total in prefixSum_map:
            cnt += prefixSum_map[total]
        # Increment in hashmap
        prefixSum_map[total] = prefixSum_map.get(total, 0) + 1
    
    return cnt

nums = [4, 5, 2, -1, -3, -3, 4, 6, -7]
print(ZeroSumSubArrays(nums))
nums = [1, 8, 7, 3, 11, 9]
print(ZeroSumSubArrays(nums))
nums = [8, -5, 0, -2, 3, -4]
print(ZeroSumSubArrays(nums))