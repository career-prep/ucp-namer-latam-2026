from collections import defaultdict
class Solution:
    def zerosum(self, nums:list):
        dict = defaultdict(int)
        for num in nums:
            dict[num] += 1
        count = 0    
        seen = set()
        
        for key in dict:
            zero = 0 - key
            
            if key == 0:
                count += dict[0] // 2
            
            else:
                if zero in dict:
                    count += dict[zero] * dict[key]
                        
        return count

sol = Solution()

test_cases = [
    [1, 10, 8, 3, 2, 5, 7, 2, -2, -1],
    [1, 10, 8, -2, 2, 5, 7, 2, -2, -1],
    [4, 3, 3, 5, 7, 0, 2, 3, 8, 6],
    [4, 3, 3, 5, 7, 0, 2, 3, 8, 0]
]

for arr in test_cases:
    print(sol.zerosum(arr))
