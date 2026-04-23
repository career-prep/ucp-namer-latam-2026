"""
Technique Used: Fixed-size sliding window
Time Complexity: O(n)
Space Complexity: O(1)
"""

# Input: array of ints (name it nums), int k
# Output: maximum mean (float due to division)
# Approach: Use fixed-size sliding window since our size of window is dependent on k.
# Calculate the sums first by summing up the values within window
# Compare the sums computed to max_sum and see if it generates largest sum. If largest and all values
# have been checked, return that sum divided by k.
# Potential edge cases: k = 0 or a negative value, input array has 0 or only 1 integer, or subarray k
# is larger than the input array length (i.e [1, 2, 3] but k = 4)

def max_mean_sub_array(nums: list[int], k: int) -> float:
    if k <= 0 or not nums or len(nums) < k:
        return 0 
    
    curr_sum = 0

    for i in range(k):
        curr_sum += nums[i]
    
    max_sum = curr_sum

    for i in range(k, len(nums)):
        curr_sum += nums[i] - nums[i - k]

        if curr_sum > max_sum:
            max_sum = curr_sum
    
    return max_sum / k

print(max_mean_sub_array([4,5,-3,2,6,1],2))
print(max_mean_sub_array([4,5,-3,2,6,1],3))
print(max_mean_sub_array([1,1,1,1,-1,-1,2,-1,-1],3))
print(max_mean_sub_array([1,1,1,1,-1,-1,2,-1,-1,6],5))

#Time spent: 35 minutes