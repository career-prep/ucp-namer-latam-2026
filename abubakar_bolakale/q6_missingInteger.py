""" 
Given an integer n and a sorted array of size n-1 which contain all but th eonne o fthe integers in the range 1-n, find the missing integer
"""
# using binary search,
# nums[i] = i + 1. so if a value is missing, it will shift the balance to the left and becomes nums[i] > i + 1
# so if the value of the middle index array is correct, shift the pointer to the left, else, shift it to the right (this continue untile left > right)
# return left + 1

#time complexity O(log n)
#space complexity O(1)
class Solution():
    def missinginteger(self, nums, n):
        """
        seen = set(nums)
        
        for i in range(1, n + 1):
            if i not in seen:
                return i
        """
        left = 0
        right = len(nums) - 1
        
        while left <= right:
            mid = (left + right) // 2
            
            if nums[mid] == mid + 1:
                left += 1
            else:
                right -= 1
        return left + 1
                
sol = Solution()
test_cases = [
            ([1, 2, 3, 4, 6, 7], 7),
            ([1], 2),
            ([1, 2, 3, 4, 5, 6, 7, 8, 10, 11, 12], 12),

            ([], 1),
            ([2], 2),
            ([2, 3, 4, 5], 5),
            ([1, 2, 3, 4], 5),

            ([1, 3, 4, 5], 5),
            ([1, 2, 4, 5], 5),
            ([1, 2, 3, 5], 5),

            ([1, 2], 3),
            ([1, 3], 3),

            ([1, 2, 3, 4, 5, 6, 7, 8, 9], 10),
            ([2, 3, 4, 5, 6, 7, 8, 9, 10], 10),

            ([1, 2, 3, 4, 5, 7, 8, 9, 10], 10),
            ([1, 2, 3, 4, 6, 7, 8, 9, 10], 10),
            ([1, 2, 3, 5, 6, 7, 8, 9, 10], 10),

            (list(range(1, 1000)), 1000),
            (list(range(2, 1001)), 1000),
            (list(range(1, 500)) + list(range(501, 1001)), 1000),
        ]

for nums, n in test_cases:
    print(sol.missinginteger(nums, n))
    
# 30 mins