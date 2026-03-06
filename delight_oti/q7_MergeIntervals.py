# sort then solve

def MergeIntervals(intervals):
    '''
    sort then solve

    Time Complexity: O(n)
    Space Complexity: O(n)
    '''

    intervals.sort(key=lambda x:x[0])

    merged = [intervals[0]]

    for start, end in intervals[1:]:
        last_start, last_end = merged[-1]

        if last_end >= start:
            merged[-1] = [last_start, max(end, last_end)]
        else:
            merged.append([start, end])
    return merged


# Time taken: 25mins

# nums=[(10, 12), (5, 6), (7, 9), (1, 3)]
# output = [(1, 3), (5, 6), (7, 9), (10, 12)]

# intervals = [(1, 4), (2, 6), (8, 10), (9, 12)]
# output= [(1, 6), (8, 12)]

# print(MergeIntervals(nums))