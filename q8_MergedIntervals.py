# Time: 10 minutes
# Technqiue: Sort then Solve

def MergedIntervals(a):
    result = []
    b = sorted(a)
    start, end = b[0]
    for c, d in b[1:]:
        if c <= end:
            start = min(start,c)
            end = max(d,end)
        else:
            result.append((start,end))
            start, end = c, d
    result.append((start,end))
    return result

print(MergedIntervals([(2,3),(4,8),(1,2),(5,7),(9,12)]))
print(MergedIntervals([(5,8),(6,10),(2,4),(3,6)]))
print(MergedIntervals([(10,12),(5,6),(7,9),(1,3)]))