# time:
# space:

"""
Given a sorted array of non-negative integers, modify the array by removing duplicates 
so each element only appears once. If arrays are static (aka, not dynamic/resizable) in 
your language of choice, the remaining elements should appear in the left-hand side of
the array and the extra space in the right-hand side should be padded with -1s

Examples:
input array: [1,2,2,3,3,3,4,4,4,4]
modified array: [1,2,3,4]

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
