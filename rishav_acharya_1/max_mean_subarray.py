"""
Given an array of integers and an integer k, find the maximum mean of any subarray of size k.

Time Complexity: O(n) - single pass through array
Space Complexity: O(1) - constant extra space
"""

class Solution:
    def findMaxMean(self, arr, k):
        window_sum = sum(arr[:k])
        max_mean = window_sum / k
        
        for i in range(k, len(arr)):
            window_sum += arr[i] - arr[i - k]
            max_mean = max(max_mean, window_sum / k)
        
        return max_mean


solution = Solution()

test_cases = [
    ([4, 5, -3, 2, 6, 1], 2),
    ([4, 5, -3, 2, 6, 1], 3),
    ([1, 1, 1, 1, -1, -1, 2, -1, -1], 3),
    ([1, 1, 1, 1, -1, -1, 2, -1, -1, 6], 5),
    ([5], 1),
    ([2, 4, 6], 3),
    ([-5, -2, -9], 1),
    ([0, 0, 0, 0], 2),
    ([-8, -3, -6, -2], 2),
    ([-1, 10, -2, 9, -3], 2),
    ([5, 5, 5, 5], 2),
    ([1, 2, 1, 2], 2),
    ([3, -1, 2, -1, 4], 4),
    ([1, 2, 3, 4, 5], 3),
    ([5, 4, 3, 2, 1], 3),
]

for arr, k in test_cases:
    print(solution.findMaxMean(arr, k))
