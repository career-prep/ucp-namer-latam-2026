class Solution:
    def deduparray(self, nums):
        seen = set()
        result = []

        for num in nums:
            if num not in seen:
                seen.add(num)
                result.append(num)

        return result
    
sol = Solution()
test_cases = [
            [1, 2, 2, 3, 3, 3, 4, 4, 4, 4],
            [0, 0, 1, 4, 5, 5, 5, 8, 9, 9, 10, 11, 15, 15],
            [1, 3, 4, 8, 10, 12],
            [],
            [1],
            [2, 2, 2, 2],
            [1, 2, 3, 4, 5],
            [5, 5, 5, 5, 5, 5],
            [-3, -3, -2, -1, -1, 0, 0, 1],
            [0, 0, 0, 0],
            [1, 1, 2]
        ]
for test in test_cases:
    print(sol.deduparray(test))
    
#Time and space complexity 0(n)
#10 mins spent