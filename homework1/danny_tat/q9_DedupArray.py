# time: O(n)
# space: O(1)

"""
Given a sorted array of non-negative integers, modify the array by removing duplicates 
so each element only appears once. If arrays are static (aka, not dynamic/resizable) in 
your language of choice, the remaining elements should appear in the left-hand side of
the array and the extra space in the right-hand side should be padded with -1s

Examples:
Input Array: [1,2,2,3,3,3,4,4,4,4]
Modified Array : [1,2,3,4]

Input Array: [0, 0, 1, 4, 5, 5, 5, 8, 9, 9, 10, 11, 15, 15] 
Modified Array: [0, 1, 4, 5, 8, 9, 10, 11, 15] or [0, 1, 4, 5, 8, 9, 10, 11, 15, -1, -1, -1, -1, -1] (depending on language)

Input Array: [1, 3, 4, 8, 10, 12] 
Modified Array: [1, 3, 4, 8, 10, 12]

"""


def dedup(nums):
    n = len(nums)
    i = 0
    j = 1

    while j < n:
        if nums[i] == nums[j]:
            j += 1
        else:
            i += 1
            nums[i] = nums[j]
            j += 1

    return nums[:i + 1]


print(dedup([1, 2, 2, 3, 3, 3, 4, 4, 4, 4]))
print(dedup([0, 0, 1, 4, 5, 5, 5, 8, 9, 9, 10, 11, 15, 15]))
print(dedup([1, 3, 4, 8, 10, 12]))

# time: 10 minutes
