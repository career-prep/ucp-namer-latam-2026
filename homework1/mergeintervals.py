# Question 8: MergeIntervals
# Given a list of integer pairs representing the low and high end of an interval, inclusive, return a list in which overlapping intervals are merged.


# Examples:
# Input: [(2, 3), (4, 8), (1, 2), (5, 7), (9, 12)]
# Output: [(4, 8), (1, 3), (9, 12)]
# Input: [(5, 8), (6, 10), (2, 4), (3, 6)]
# Output: [(2, 10)]
# Input: [(10, 12), (5, 6), (7, 9), (1, 3)]
# Output: [(10, 12), (5, 6), (7, 9), (1,3)]


def mergeintervals(arrs):
    if not arrs:
        return []

    # helper function
    def get_start(interval):
        return interval[0]

    # sort intervals by start
    intervals = sorted(arrs, key=get_start)

    merged = [intervals[0]]

    for start, end in intervals[1:]:
        last_start, last_end = merged[-1]

        if start <= last_end:
            merged[-1] = (last_start, max(last_end, end))
        else:
            merged.append((start, end))

    return merged

print(mergeintervals([(2, 3), (4, 8), (1, 2), (5, 7), (9, 12)]))
print(mergeintervals([(5, 8), (6, 10), (2, 4), (3, 6)]))
