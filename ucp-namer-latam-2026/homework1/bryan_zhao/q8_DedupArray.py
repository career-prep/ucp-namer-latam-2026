"""
Technique Used: Variable-size sliding window
Time Complexity: O(n)
Space Complexity: O(1)
"""

# Input: list of integers
# Output: same list of integers, just with duplicates removed
# Approach: Check that the list is not empty first. Then, set left pointer to the start
# of the list and right pointer one position after to check if the next integer is a dupe
# or not. If it is not a dupe, increment the left pointer by 1 and set the left pointer's
# number to the right pointer's number and repeat.
# Edge cases: Empty list

def dedup_array(nums: list[int]) -> list[int]:
    if not nums:
        return []
    
    left, right = 0, 1

    while right < len(nums):
        if nums[right] != nums[left]:
            left += 1
            nums[left] = nums[right]
        right += 1

    for i in range(left + 1, len(nums)):
        nums[i] = -1
    
    return nums

print(dedup_array([1,2,2,3,3,3,4,4,4,4]))
print(dedup_array([0,0,1,4,5,5,5,8,9,9,10,11,15,15]))
print(dedup_array([1,3,4,8,10,12]))

# Time Spent: 10 minutes