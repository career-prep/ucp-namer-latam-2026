# Technique: Reset/catch-up two-pointer
# Time Complexity: O(n)
# Space Complexity: O(1)

def dedup_array(nums):
    if not nums:
        return nums

    index = 1
    for i in range(1, len(nums)):
        if nums[i] != nums[i - 1]:
            nums[index] = nums[i]
            index += 1

    return nums[:index]

print(dedup_array([1, 2, 2, 3, 3, 3, 4, 4, 4, 4]))
print(dedup_array([0, 0, 1, 4, 5, 5, 5, 8, 9, 9, 10, 11, 15, 15]))
print(dedup_array([1, 3, 4, 8, 10, 12]))

# My Edge Testcases:
print(dedup_array([])) # Empty array
print(dedup_array([7, 7, 7, 7])) # All duplicates
print(dedup_array([0])) # Single element
print(dedup_array([0, 1, 2, 3])) # All unique

# Time Spent: 8mins 34secs