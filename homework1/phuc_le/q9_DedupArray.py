'''
    Two pointer technique:

    Maintain 2 pointers, one for the start of the ans list and one to go through the array
    Skip all element the same as the left pointer
    The answer array will be from 0 to l pointer

    Time: O(n)
    Space: O(1)
    n: numbers of elements in the array

    Time spent: 25 mins
'''

from typing import List

def DedupArray(nums: List[int]) -> List[int]:
    # Edge case:
    if len(nums) == 0:
        return []

    l = 0
    for r in range(1, len(nums)):
        if nums[l] != nums[r]:
            l += 1
            nums[l] = nums[r]
    
    return nums[:l + 1]

nums = [1, 2, 2, 3, 3, 3, 4, 4, 4, 4]
print(DedupArray(nums))
nums = [0, 0, 1, 4, 5, 5, 5, 8, 9, 9, 10, 11, 15, 15]
print(DedupArray(nums))
nums = [1, 3, 4, 8, 10, 12]
print(DedupArray(nums))