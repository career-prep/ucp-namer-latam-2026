""" 
Given an array of integers, count the number of subarrays that sum to zero
"""
#Using prfix-sum and hashmap
# I use a hashmap to store how many times each prefix sum has appeared.
# I iterate through the array while maintaining a running sum.
# If the same running sum appears again, then the elements between the previous occurrence and the current index sum to zero.
# For each prefix sum value, if it has appeared k times before, it contributes k new zero-sum subarrays ending at the current index.
# I add that to the count and then update the hashmap.
class solution:
    def zerosumsubarrays(nums):
        freq = {}
        prefix_sum = 0
        count = 0
        for num in nums:
            prefix_sum += num
            
            if prefix_sum in freq:
                count += freq[prefix_sum]
                freq[prefix_sum] += 1
            else:
                freq[prefix_sum] = 1
        return count
              
sol = solution
tests = [
    [4, 5, 2, -1, -3, -3, 4, 6, -7],
    [1, 8, 7, 3, 11, 9],
    [8, -5, 0, -2, 3, -4],
    [],
    [0],
    [5],
    [-5],
    [0, 0],
    [0, 0, 0],
    [1, -1],
    [-2, 2],
    [1, -1, 1, -1],
    [2, -2, 2, -2, 2, -2],
    [1, -1, 0],
    [3, -3, 3, -3],
    [4, 1, -1, 2, -2],
    [0, 1, -1],
    [1, 0, -1],
    [0, -1, 1, 0],
    [3, 4, -7, 1, 3, 3, 1, -4],
    [6, 3, -1, -3, 4, -2, 2, 4, 6, -12, -7],
    [1, 2, 3, 4],
    [-1, -2, -3, -4],
    [10**9, -10**9],
    [10**9, 1, -1, -10**9]
]

for arr in tests:
    print(arr, "=", sol.zerosumsubarrays(arr))
            