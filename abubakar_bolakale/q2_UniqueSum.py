class Solution:
    def uniquesum(self, nums:list):
        unique_element = set(nums)
        count = 0
        for num in unique_element:
            count += num
        return count

sol = Solution()

test_cases = [
    [1, 10, 8, 3, 2, 5, 7, 2, -2, -1],
    [4, 3, 3, 5, 7, 0, 2, 3, 8, 6],
]

for arr in test_cases:
    print(sol.uniquesum(arr))

# Spent a total of 3 mins on this question