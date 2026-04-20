'''
    Hashing technique:

    Check if the first number = 1 and last number = n
    Check the different between each elemetns in nums if = 1

    Time: O(n)
    Space: O(1)
    n: numbers of array elements

    Time spent: 15 mins
'''

from typing import List

def MissingInteger(nums: List[int], n: int) -> int:
    # Check the array is empty or first number != 1
    if not nums or nums[0] != 1:
        return 1
    # Check the middle missing number
    for i in range(1, len(nums)):
        if nums[i] - nums[i - 1] != 1:
            return nums[i - 1] + 1
    # Check the last number
    return n

nums, n = [1, 2, 3, 4, 6, 7], 7
print(MissingInteger(nums, n))
nums, n = [1], 2
print(MissingInteger(nums, n))
nums, n = [1, 2, 3, 4, 5, 6, 7, 8, 10, 11, 12], 12
print(MissingInteger(nums, n))