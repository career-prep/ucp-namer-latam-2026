'''
    Unique elements -> set
    Make the input into a set 
    Return the sum of the set

    n: numbers of elements of the input
    Time: O(n)
    Space: O(n)

    Spend around 5 minutes
'''

from typing import List

def UniqueSum(nums: List[int]) -> int:
    return sum(set(nums))

nums = [1, 10, 8, 3, 2, 5, 7, 2, -2, -1]
print(UniqueSum(nums))
nums = [4, 3, 3, 5, 7, 0, 2, 3, 8, 6]
print(UniqueSum(nums))