# Question 1: ZeroSum
# Part2
# Follow-Up: Now assume you can re-use elements in different pairs (i.e., the elements in a pair must be from different indices but different pairs may use an element form the same index).


# Examples:

# Input Array: [1, 10, 8, 3, 2, 5, 7, 2, -2, -1]
# Output: 3
# (Pairs: (1, -1), (2, -2), (2, -2))

# Input Array: [1, 10, 8, -2, 2, 5, 7, 2, -2, -1]
# Output: 5
# (Pairs: (1, -1), (2, -2), (2, -2), (2, -2), (2, -2))

# Input Array: [4, 3, 3, 5, 7, 0, 2, 3, 8, 6]
# Output: 0

# Input Array: [4, 3, 3, 5, 7, 0, 2, 3, 8, 0]
# Output: 1
# (Pairs: (0, 0))

from collections import defaultdict
def ZeroSum(array):
    freq = defaultdict(int)
    pairs = []

    for num in array:
        target = -num

        # Each previous target forms a valid pair
        for _ in range(freq[target]):
            pairs.append((target, num))

        freq[num] += 1

    return len(pairs)

# O(n) time, O(n) space
test_list = [[1, 10, 8, 3, 2, 5, 7, 2, -2, -1],[1, 10, 8, -2, 2, 5, 7, 2, -2, -1],[4, 3, 3, 5, 7, 0, 2, 3, 8, 6],[4, 3, 3, 5, 7, 0, 2, 3, 8, 0]]
for test in test_list:
    print(ZeroSum(test))

# Spent a total of 50 mins on this question