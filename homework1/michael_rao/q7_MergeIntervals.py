# method: sort then solve
# time: O(nlog(n))
# space: O(n)

def mergeIntervals(intervals):
    intervals.sort(key=lambda x: (x[0], x[1]))
    merged = [intervals[0]]

    for start, end in intervals[1:]:
        lastStart, lastEnd = merged[-1]
        if start <= lastEnd:
            merged[-1] = (lastStart, max(lastEnd, end))
        else:
            merged.append((start, end))
    
    return merged

def checkSolution(intervals, correct):
    print("Input:", intervals)
    print("Correct:", correct)
    print("Output: ", mergeIntervals(intervals))
    print()

checkSolution([(2,3),(4,8),(1,2),(5,7),(9,12)],[(1,3), (4,8), (9,12)])
checkSolution([(5,8),(6,10),(2,4),(3,6)],[(2,10)])
checkSolution([(10,12),(5,6),(7,9),(1,3)],[(1,3),(5,6),(7,9),(10,12)])

# time taken # 15 min