def mergeIntervals(intervals):
    intervals.sort(key = lambda a : a[0])

    res = [intervals[0]]

    for start, end in intervals:
        last = res[-1][1]

        if start <= last:
            res[-1][1] = max(last, end)

        else:
            res.append([start, end])

    return res

print(mergeIntervals([[2, 3], [4, 8], [1, 2], [5, 7], [9, 12]]))
print(mergeIntervals([[1, 5], [2, 3], [4, 6], [8, 10], [9, 12]]))
