# ============================================================
# Technique: Sort the array, then solve (merge in one pass)
# Time: O(n log n) because we sort the intervals first
# Space: O(n) for the output list of merged intervals
# ============================================================

from typing import List, Tuple

def merge_intervals(intervals: List[Tuple[int, int]]) -> List[Tuple[int, int]]:
    """
    Given a list of (start, end) intervals (inclusive),
    return a list where all overlapping intervals are merged.
    """

    if not intervals:
        return []

    sorted_intervals = sorted(intervals, key=lambda interval: interval[0])

    merged: List[Tuple[int, int]] = []

    current_start, current_end = sorted_intervals[0]

    for next_start, next_end in sorted_intervals[1:]:
    
        if next_start <= current_end:
            
            current_end = max(current_end, next_end)
        else:
            
            merged.append((current_start, current_end))
            current_start, current_end = next_start, next_end

    merged.append((current_start, current_end))

    return merged


def run_tests() -> None:
    # examples from prompt
    assert merge_intervals([(2, 3), (4, 8), (1, 2), (5, 7), (9, 12)]) == [(1, 3), (4, 8), (9, 12)]
    assert merge_intervals([(5, 8), (6, 10), (2, 4), (3, 6)]) == [(2, 10)]
    assert merge_intervals([(10, 12), (5, 6), (7, 9), (1, 3)]) == [(1, 3), (5, 6), (7, 9), (10, 12)]

    # edge cases
    assert merge_intervals([]) == []
    assert merge_intervals([(1, 1)]) == [(1, 1)]
    assert merge_intervals([(1, 2), (2, 3)]) == [(1, 3)]  # touching counts as overlap
    assert merge_intervals([(1, 5), (2, 3)]) == [(1, 5)]  # fully contained
    assert merge_intervals([(3, 4), (1, 2)]) == [(1, 2), (3, 4)]  # no overlap unsorted input

    print("All tests passed")


if __name__ == "__main__":
    run_tests()
