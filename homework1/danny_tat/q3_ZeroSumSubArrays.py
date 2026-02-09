# time: O(n)
# space: O(n)
"""
Given an array of integers, count the number of subarrays that sum to zero.

Examples:
Input Array: [4, 5, 2, -1, -3, -3, 4, 6, -7] 
Output: 2 
(Subarrays: [5, 2, -1, -3, -3], [-3, 4, 6, -7])

Input Array: [1, 8, 7, 3, 11, 9] 
Output: 0

Input Array: [8, -5, 0, -2, 3, -4] Output: 2 (Subarrays: [0], [8, -5, 0, -2, 3, -4])

"""


def zeroSum(nums):
    count = 0
    sum = 0
    map = {0: 1}

    for num in nums:
        sum += num

        if sum in map:
            count += map[sum]

        map[sum] = map.get(sum, 0) + 1

    return count


print(zeroSum([4, 5, 2, -1, -3, -3, 4, 6, -7]))
print(zeroSum([1, 8, 7, 3, 11, 9]))
print(zeroSum([8, -5, 0, -2, 3, -4]))

# time: 35 minutes
