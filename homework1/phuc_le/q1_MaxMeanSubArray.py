'''
    Two pointers technique:

    Maintain a sum variable for the sum
    Using sliding window technique, when move the window, - the number of the left and + number on the right of the window

    Time: O(n)
    Space: O(1)
    n: numbers of element in the array

    Time spent: 25 mins
'''

from typing import List

def MaxMeanSubArray(nums: List[int], k: int) -> float:
    n = len(nums)
    # Not enough elements in the array
    if (n < k):
        return 0
    # Keep track of the elements of the array
    totalSum = 0
    l = 0
    maxMean = -float("inf")
    # Loop and find the mean in place
    for r in range(n):
        totalSum += nums[r]
        if (r - l + 1) == k:
            maxMean = max(totalSum / k, maxMean)
            totalSum -= nums[l]
            l += 1
        
    return maxMean

nums = [4, 5, -3, 2, 6, 1]
k = 2
print(MaxMeanSubArray(nums, k))
nums = [4, 5, -3, 2, 6, 1]
k = 3
print(MaxMeanSubArray(nums, k))
nums = [1, 1, 1, 1, -1, -1, 2, -1, -1]
k = 3
print(MaxMeanSubArray(nums, k))
nums = [1, 1, 1, 1, -1, -1, 2, -1, -1, 6]
k = 5
print(MaxMeanSubArray(nums, k))
