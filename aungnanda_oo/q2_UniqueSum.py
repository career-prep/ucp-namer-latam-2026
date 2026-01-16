# Given an array of integers, return the sum of unique elements in the array.

# Examples:

# Input Array: [1, 10, 8, 3, 2, 5, 7, 2, -2, -1]
# Output: 33 (1 + 10 + 8 + 3 + 2 + 5 + 7 + -2 + -1)

# Input Array: [4, 3, 3, 5, 7, 0, 2, 3, 8, 6]
# Output: 35 (4 + 3 + 5 + 7 + 0 + 2 + 8 + 6)

# Brute Force
def UniqueSum(arr: list[int]) -> int:
    set_arr = set(arr)
    return sum(set_arr)

# O(n) time, O(n) space

# same complexity, less memory overhead
def UniqueSum(arr: list[int]) -> int:
    seen = set()
    total = 0
    for num in arr:
        if num not in seen:
            seen.add(num)
            total += num
    return total

# O(n) time, O(n) space
test_list = [[1, 10, 8, 3, 2, 5, 7, 2, -2, -1],[4, 3, 3, 5, 7, 0, 2, 3, 8, 6]]
for test in test_list:
    print(UniqueSum(test))

# Spent a total of 7 mins on this question