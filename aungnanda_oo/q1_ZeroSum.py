# Question 1: ZeroSum
# Part1
# Given an array of integers, return the number of pairs of integers in the array that sum to O assuming you can use the element at each index at most once.

# Input Array: [1, 10, 8, 3, 2, 5, 7, 2, -2, -1]
# Output: 2
# (Pairs: (1, -1), (2, -2))


# Input Array: [1, 10, 8, -2, 2, 5, 7, 2, -2, -1]
# Output: 3
# (Pairs: (1, -1), (2, -2), (2, -2))


# Input Array: [4, 3, 3, 5, 7, 0, 2, 3, 8, 6]
# Output: 0


# Input Array: [4, 3, 3, 5, 7, 0, 2, 3, 8, 0]
# Output: 1
# (Pairs: (0, 0))

# Brute Force Solu

from collections import defaultdict
def ZeroSum(array):
    zero_pair_list = []
    used_index = defaultdict(int)
    for i in range(len(array)):
        for j in range(i+1, len(array)):
            if i in used_index or j in used_index:
                continue
            else:
                if array[i] + array[j] == 0:
                    used_index[i] = array[i]
                    used_index[j] = array[j]
                    zero_pair_list.append(tuple([array[i],array[j]]))

    return len(zero_pair_list)

# O(n^2) time, O(n) space
test_list = [[1, 10, 8, 3, 2, 5, 7, 2, -2, -1],[1, 10, 8, -2, 2, 5, 7, 2, -2, -1], [4, 3, 3, 5, 7, 0, 2, 3, 8, 6], [4, 3, 3, 5, 7, 0, 2, 3, 8, 0]]

for arr in test_list:
    print(ZeroSum(arr))

# Spent a total of 30 mins on this question