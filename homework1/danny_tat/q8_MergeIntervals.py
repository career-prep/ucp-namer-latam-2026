# time: O(n log n)
# space: O(n)
"""
Given a list of integer pairs representing the low and high end of an interval, inclusive, return a list in which overlapping intervals 
are merged.

Examples:
Input: [(2, 3), (4, 8), (1, 2), (5, 7), (9, 12)] 
Output: [(4, 8), (1, 3), (9, 12)]

Input: [(5, 8), (6, 10), (2, 4), (3, 6)] 
Output: [(2, 10)]

Input: [(10, 12), (5, 6), (7, 9), (1, 3)] 
Output: [(10, 12), (5, 6), (7, 9), (1, 3)]
"""


def mergeInterval(intervals):
    if not intervals:
        return []

    intervals.sort(key=lambda i: i[0])

    output = [list(intervals[0])]

    for start, end in intervals[1:]:
        lastEnd = output[-1][1]

        if start <= lastEnd:
            output[-1][1] = max(lastEnd, end)
        else:
            output.append([start, end])

    return output


print(mergeInterval([(2, 3), (4, 8), (1, 2), (5, 7), (9, 12)]))
print(mergeInterval([(5, 8), (6, 10), (2, 4), (3, 6)]))
print(mergeInterval([(10, 12), (5, 6), (7, 9), (1, 3)]))

# time: 35 minutes
