# Question 3: ZeroSumSubArrays

# Given an array of integers, count the number of subarrays that sum to zero.

# Examples:

# Input Array: [4, 5, 2, -1, -3, -3, 4, 6, -7]
# Output: 2
# (Subarrays: [5, 2, -1, -3, -3], [-3, 4, 6, -7])

# Input Array: [1, 8, 7, 3, 11, 9]
# Output: 0

# Input Array: [8, -5, 0, -2, 3, -4]
# Output: 2
# (Subarrays: [0], [8, -5, 0, -2, 3, -4])

# Brute Force Solu
def ZeroSumSubArrays_1(array: list[int]) -> int:
    count = 0

    for i in range(len(array)):
        window_sum = 0
        for j in range(i, len(array)):
            window_sum += array[j]
            if window_sum == 0:
                count += 1

    return count

# Optimal Solu
from collections import defaultdict
def ZeroSumSubArrays_2(array: list[int]) -> int:
    prefix_sum = 0
    count = 0
    freq = defaultdict(int)

    freq[0] = 1  # important: prefix sum 0 seen once

    for num in array:
        prefix_sum += num

        # if we've seen this prefix_sum before,
        # it means subarrays between those indices sum to 0
        count += freq[prefix_sum]

        freq[prefix_sum] += 1

    return count

test_cases = [[4, 5, 2, -1, -3, -3, 4, 6, -7], [1, 8, 7, 3, 11, 9], [8, -5, 0, -2, 3, -4]]
print("Brute Force Solu Output")
for test_case in test_cases:
    print(ZeroSumSubArrays_1(test_case))

# Time Complexity = O(n^2)
# Space Complexity = O(1)

print("Optimal Solu Output")
for test_case in test_cases:
    print(ZeroSumSubArrays_2(test_case))


# Obvious input example for how prefix sum works here [4,2,-3,1,6], 4 and [2,-3,1] = 0, then becoming prefix sum 4 means there must be sub array

# Time Complexity = O(n)
# Space Complexity = O(n)


# Spent a total of 40 mins on this question