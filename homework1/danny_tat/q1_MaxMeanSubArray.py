# time: O(n)
# space: O(1)

"""
Given an array of integers and an integer, k, find the maximum mean of a subarray of size k.

Examples:
Input Array: [4, 5, -3, 2, 6, 1] 
Input k = 2 
Output: 4.5

Input Array: [4, 5, -3, 2, 6, 1] 
Input k = 3 
Output: 3

Input Array: [1, 1, 1, 1, -1, -1, 2, -1, -1] 
Input k = 3 
Output: 1

Input Array: [1, 1, 1, 1, -1, -1, 2, -1, -1, 6] 
Input k = 5 
Output: 1

"""


def maxMean(nums, k):
    n = len(nums)
    curr_sum = 0

    for i in range(k):
        curr_sum += nums[i]

    max_avg = curr_sum / k

    for i in range(k, n):
        curr_sum += nums[i]
        curr_sum -= nums[i-k]

        avg = curr_sum / k
        max_avg = max(max_avg, avg)

    return max_avg


print(maxMean([4, 5, -3, 2, 6, 1], 2))
print(maxMean([4, 5, -3, 2, 6, 1], 3))
print(maxMean([1, 1, 1, 1, -1, -1, 2, -1, -1], 3))
print(maxMean([1, 1, 1, 1, -1, -1, 2, -1, -1, 6], 5))

# time: 7 minutes
