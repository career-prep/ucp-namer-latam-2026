# Time complexity: O(n log n)
# Space complexity: O(n)

# Technique: Sort the array, then solve

def MergeIntervals(intervals):
    if not intervals:
        return []
    
    intervals.sort()
    mergedIntervals = [intervals[0]]

    for i in range(1, len(intervals)):
        prevInterval = mergedIntervals[-1]
        currInterval = intervals[i]

        if currInterval[0] <= prevInterval[1]:
            mergedIntervals[-1] = (prevInterval[0], max(prevInterval[1], currInterval[1])) # necessary because tuples are immutable
        else:
            mergedIntervals.append(currInterval)

    return mergedIntervals
        
if __name__ == '__main__':

    # inputList = [(2, 3), (4, 8), (1, 2), (5, 7), (9, 12)]
    #     # Output: [(4, 8), (1, 3), (9, 12)]
    # inputList = [(5, 8), (6, 10), (2, 4), (3, 6)]
    #     #Output: [(2, 10)]
    inputList = [(10, 12), (5, 6), (7, 9), (1,3)]
        #Output: [(10, 12), (5, 6), (7, 9), (1,3)]
    print("Input:", inputList)
    print("Output:", MergeIntervals(inputList))

# ~ time spent: 20 minutes