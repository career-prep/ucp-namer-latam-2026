# Question 6: MissingInteger

# Given an integer n and a sorted array of integers of size n - 1 which contains all but one of the integers in the range 1 - n, find the missing integer.

# Examples:

# Input Array: [1, 2, 3, 4, 6, 7]
# Input n: 7
# Output: 5

# Input Array: [1]
# Input n: 2
# Output: 2

# Input Array: [1, 2, 3, 4, 5, 6, 7, 8, 10, 11, 12]
# Input n: 12
# Output: 9

def MissingInteger(arr, n):
    # Sum of 1 to n = n * (n + 1) / 2
    expected_sum = n * (n + 1) // 2
    actual_sum = sum(arr)
    return expected_sum - actual_sum

# Time Complexity: O(n)
# Space Complexity: O(1)

test_cases = [
    ([1, 2, 3, 4, 6, 7], 7),
    ([1], 2),
    ([1, 2, 3, 4, 5, 6, 7, 8, 10, 11, 12], 12)
]
for arr, n in test_cases:
    print(MissingInteger(arr, n))


# Spent a total of 40 mins on this question, its just math thing :)