"""
Given an array of intervals, merge all overlapping intervals.

Examples:
Input: [(2,3), (4,8), (1,2), (5,7), (9,12)] -> Output: [(1,3), (4,8), (9,12)]
Input: [(5,8), (6,10), (2,4), (3,6)] -> Output: [(2,10)]
"""

def mergeIntervals(intervals):
    if not intervals:
        return []
    
    intervals.sort()
    merged = [intervals[0]]
    
    for i in range(1, len(intervals)):
        current_start, current_end = intervals[i]
        last_start, last_end = merged[-1]
        
        if current_start <= last_end:
            merged[-1] = (last_start, max(last_end, current_end))
        else:
            merged.append(intervals[i])
    
    return merged

# Time Complexity: O(n log n)
# Space Complexity: O(n)


test_cases = [
    [(2,3), (4,8), (1,2), (5,7), (9,12)],
    [(5,8), (6,10), (2,4), (3,6)]
]

for test in test_cases:
    print(mergeIntervals(test))
