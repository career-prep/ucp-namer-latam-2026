"""
Technique Used: One-directional running computation/total
Time Complexity: O(n)
Space Complexity: O(n)
"""

# Input: array of integers (list[int])
# Output: # of subarrays that sum to zero (int)
# Approach: Create a hashmap that stores 0 and keep a running total of what the sum of the 
# subarray is after expanding the pointer by 1. If that current sum is a sum that equals 0
# (seen in the hashmap), store it in the hashmap and add 1 to the count
# Edge cases: Empty array

def zero_sum_sub_arrays(nums: list[int]) -> int:
    cumulative_sum_map = {0: 1} # Initialized to 0 in case we do not find any subarrays
    count = 0
    curr_sum = 0
    
    for num in nums:
        curr_sum += num

        if curr_sum in cumulative_sum_map:
            count += cumulative_sum_map[curr_sum]
        
        cumulative_sum_map[curr_sum] = cumulative_sum_map.get(curr_sum, 0) + 1
    
    return count

print(zero_sum_sub_arrays([4, 5, 2, -1, -3, -3, 4, 6, -7]))
print(zero_sum_sub_arrays([1, 8, 7, 3, 11, 9]))
print(zero_sum_sub_arrays([8, -5, 0, -2, 3, -4]))

#Time Spent: 40 minutes