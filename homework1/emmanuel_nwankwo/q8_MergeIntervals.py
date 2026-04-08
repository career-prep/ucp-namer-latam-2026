# Technique: Sort the array, then solve
# Time Complexity: O(n)
# Space Complexity: O(n)

def merge_intervals(intervals):
    if not intervals:
        return []

    # Sort
    intervals.sort(key=lambda x: x[0])

    out = []
    start, end = intervals[0]

    for a, b in intervals[1:]:
        if a <= end:
            # extend current range if needed for overlapping interval
            if b > end:
                end = max(end, b)
        else:
            out.append((start, end))
            start, end = a, b

    # Add final merged interval
    out.append((start, end))
    return out

print(merge_intervals([(2, 3), (4, 8), (1, 2), (5, 7), (9, 12)]))
print(merge_intervals([(5, 8), (6, 10), (2, 4), (3, 6)]))
print(merge_intervals([(10, 12), (5, 6), (7, 9), (1, 3)]))

# My Edge Testcases:
print(merge_intervals([])) # Empty array
print(merge_intervals([(1, 1)])) # Single interval
print(merge_intervals([(1, 2), (2, 3)])) # Intervals with same value as low and high

# Time Spent: 11mins 9secs