def mergeIntervals(intervals):
    """
    # Techniue used: sort the array, then solve 

    # Idea:
    sort the intervals
    
    walk through each interval 
        - if the current interval overlaps the last merged one, extend the end
        - otherwise, start a new merged interval 

    # Complexity:
    time: O(nlogn)
    space: O(n)

    # Time spent: 15mins
    """
    intervals.sort()
    res = []
    for s, e in intervals:
        if res and s <= res[-1][1]:
            s = min(res[-1][0], s)
            e = max(res[-1][1], e)
            res.pop()
        res.append((s, e))

    return res

i1 = [(2, 3), (4, 8), (1, 2), (5, 7), (9, 12)]
print(mergeIntervals(i1))

i2 = [(5, 8), (6, 10), (2, 4), (3, 6)]
print(mergeIntervals(i2))

i3 = [(10, 12), (5, 6), (7, 9), (1, 3)]
print(mergeIntervals(i3))