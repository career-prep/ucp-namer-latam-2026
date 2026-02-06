# Question: MergeIntervals
#
# Given a list of integer pairs representing intervals, where each pair
# contains a low and high value (inclusive), return a list in which all
# overlapping intervals are merged.
#
# Examples:
#
# Input: [(2, 3), (4, 8), (1, 2), (5, 7), (9, 12)]
# Output: [(1, 3), (4, 8), (9, 12)]
#
# Input: [(5, 8), (6, 10), (2, 4), (3, 6)]
# Output: [(2, 10)]
#
# Input: [(10, 12), (5, 6), (7, 9), (1, 3)]
# Output: [(1, 3), (5, 6), (7, 9), (10, 12)]

def merge_intervals(arr):
    if not arr:
        return [] 
    
    arr.sort()
    merged = [arr[0]]
    for start, end in arr[1:]:
        last_start, last_end = merged[-1]
        
        if start <= last_end:
            merged[-1] = (last_start, max(last_end, end))
        else:
            merged.append((start, end))
    
    return merged

print(merge_intervals([(5, 8), (6, 10), (2, 4), (3, 6)]))
print(merge_intervals([(2, 3), (4, 8), (1, 2), (5, 7), (9, 12)]))
print(merge_intervals([(10, 12), (5, 6), (7, 9), (1, 3)]))