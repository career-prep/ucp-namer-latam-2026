"""
Technique Used: Sort the array, then solve
Time Complexity: O(n log n)
Space Complexity: O(n)
"""

# Input: list of integer pairs
# Output: same list but overlapping intervals are merged
# Approach: First sort the integer pairs so that they are in ascending order. Start with
# the first interval in the sorted list and add it to a merged list. Look at the next 
# interval and compare its start time to the end time of the interval in merged. If they
# overlap, update the end of the current interval in merged list to be the max of the two
# ends so that the interval covers both of them.
# Edge Cases: Empty lists, identical intervals

def merge_intervals(intervals: list[list[int]]) -> list[list[int]]:
    if not intervals:
        return []
    
    intervals = [list(i) for i in intervals]
    intervals.sort(key=lambda x: x[0])

    merged = []

    curr_interval = intervals[0]
    merged.append(curr_interval)

    for i in range(1, len(intervals)):
        next_start, next_end = intervals[i]
        last_start, last_end = merged[-1]

        if next_start <= last_end:
            merged[-1][1] = max(last_end, next_end)
        else:
            merged.append([next_start, next_end])
    
    return merged

print(merge_intervals([(2,3),(4,8),(1,2),(5,7),(9,12)]))
print(merge_intervals([(5,8),(6,10),(2,4),(3,6)]))
print(merge_intervals([(10,12),(5,6),(7,9),(1,3)]))

# Time Spent: 40 minutes