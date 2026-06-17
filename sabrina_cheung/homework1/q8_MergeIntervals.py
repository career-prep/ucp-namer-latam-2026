"""
Technique Used: Sort then solve
Time Complexity: O(n logn)
Space Complexity: O(n)

Intuition: Sort the intervals by the first value. 
If the current interval starts before or at the same time the previous one ends, then it overlaps.
Otherwise it doesn't overlap.
"""

def MergeIntervals(intervals):
    if not intervals:
        return []

    # 1. Sort based on the start of each interval
    intervals.sort()

    merged = [intervals[0]]

    for start, end in intervals[1:]:
        last_end = merged[-1][1]

        if start <= last_end:
            merged[-1][1] = max(last_end, end)
        else:
            merged.append([start, end])

    return merged


test = [[[1, 3], [2, 6], [8, 10], [15, 18]],
             [[2, 3], [4, 8], [1, 2], [5, 7], [9, 12]]]
for i in test:
    print(MergeIntervals(i))

# Time Spent: 35 mins