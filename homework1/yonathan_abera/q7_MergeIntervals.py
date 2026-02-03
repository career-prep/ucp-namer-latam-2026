#Sort, then Solve
#O(nlogn) time complexity, O(n) space complexity

def merge_intervals(intervals):
    if not intervals:
        return[]
    intervals.sort(key = lambda x : x[0])
    result = [intervals[0]]

    for first, last in intervals[1:] :
        if result[-1][1] >= first:
            result[-1] = (result[-1][0], max(last, result[-1][1]))
        else:
            result.append((first, last))
    return result

print(merge_intervals([(2, 3), (4, 8), (1, 2), (5, 7), (9, 12)]))
print(merge_intervals([(1,4),(4,5)]))
print(merge_intervals([(5,7),(1,3),(2,6)]))
print(merge_intervals([(1,4),(0,2),(3,5)]))
print(merge_intervals([(1,10),(2,3),(4,8),(11,12)]))
print(merge_intervals([]))

#40 minutes