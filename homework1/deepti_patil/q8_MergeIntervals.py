def merge_intervals(intervals):
    """
    Merge overlapping intervals.

    Time Complexity: O(n log n)
        - Sorting the intervals dominates.

    Space Complexity: O(n)
        - Used to store the merged intervals.
    """

    if not intervals:
        return []

    # Sort intervals by starting value
    intervals.sort(key=lambda x: x[0])

    merged = [intervals[0]]

    for start, end in intervals[1:]:
        last_start, last_end = merged[-1]

        # If intervals overlap or touch, merge them
        if start <= last_end:
            merged[-1] = (last_start, max(last_end, end))
        else:
            merged.append((start, end))

    return merged
