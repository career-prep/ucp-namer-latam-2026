def merge_intervals(intervals):
    res = []
    intervals.sort(key=lambda x : x[0])
    print(intervals)
    
    interval = intervals[0]
    for i in range(1, len(intervals)):
        if interval[1] >= intervals[i][0]:
            interval = interval[0], max(intervals[i][1], interval[1])
        else:
            res.append(interval)
            interval = intervals[i]
    
    res.append(interval)       
    return res            
            
            
intervals = [(10,12), (5,6), (7,9), (1,3)]
print(merge_intervals(intervals))



'''
[(2,3), (4,8), (1,2), (5,7), (9,12)]
(2,8)

[(1,2), (2,3), (4,8), (5,7), (9,12)]
interval = 1, 3

res = [(1,3)]
'''