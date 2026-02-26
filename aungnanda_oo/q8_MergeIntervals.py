# Question 8: MergeIntervals

# Given a list of integer pairs representing the low and high end of an interval, inclusive, return a list in which overlapping intervals are merged.

# Examples:

# Input: [(2, 3), (4, 8), (1, 2), (5, 7), (9, 12)]
# Output: [(1, 3), (4, 8), (9, 12)]

# Input: [(5, 8), (6, 10), (2, 4), (3, 6)]
# Output: [(2, 10)]

# Input: [(10, 12), (5, 6), (7, 9), (1, 3)]
# Output: [(10, 12), (5, 6), (7, 9), (1, 3)]


def MergeIntervals(intervals):

    # [(2, 3), (4, 8), (1, 2), (5, 7), (9, 12)]
    sorted_intervals = sorted(intervals)
    # [(1, 2), (2, 3), (4, 8), (5, 7), (9, 12)]
    res = []
    for interval in sorted_intervals:
        if not res or res[-1][1] < interval[0]:
            res.append(interval)
        else:
            res[-1] = (res[-1][0], max(res[-1][1], interval[1]))

    return res


# Time Complexity: O(n log n)
# Space Complexity: O(n)

test_cases = [[(2, 3), (4, 8), (1, 2), (5, 7), (9, 12)],
              [(5, 8), (6, 10), (2, 4), (3, 6)],
              [(10, 12), (5, 6), (7, 9), (1, 3)]
              ]

for test_case in test_cases:
    print(MergeIntervals(test_case))


# Spent a total of 20 mins on this question