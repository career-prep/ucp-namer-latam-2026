"""
Technique Used: Binary Search Variation
Time Complexity: O(log n)
Space Complexity: O(1)
"""
# Input: integer n and sorted array of ints of size n-1
# Output: integer that's missing from the array
# Approach: Since the array is sorted in ascending order, I can solve for the missing integer
# in logarithmic time by doing binary search. The desired value in binary search for a complete
# sorted array can be found using the formula value = index + 1. Use binary search to find first
# index where value doesn't match the formula.
# Edge Cases: missing number is at the start/end 

def missing_integer(nums: list[int], n: int) -> int:
    if not nums or nums[0] != 1:
        return 1
    
    if nums[-1] != n:
        return n
    
    left, right = 0, len(nums) - 1

    while left <= right:
        mid = left + (right - left) // 2

        if nums[mid] == mid + 1:
            left = mid + 1
        else:
            right = mid - 1
    
    return left + 1

print(missing_integer([1,2,3,4,6,7],7))
print(missing_integer([1],2))
print(missing_integer([1,2,3,4,5,6,7,8,10,11,12],12))

# Time Spent: 8 minutes