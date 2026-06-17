
#Not finished

def mergeIntervals(intervals):
    if not intervals:
        return []

    # Correctly identified Technique->Sort the array, then solve

    #1. Sorting by the start time?
    
    result = []
    
    #2. Iterate over the intervals
    for i in range(len(intervals) - 1):
        curr_start = intervals[i][0]
        curr_end = intervals[i][1]
        
        next_start = intervals[i+1][0]
        next_end = intervals[i+1][1]
        
        #  overlap condition feels weird
        if next_start <= curr_end:
            # I'm trying to merge them here, but I don't know 

            new_interval = (curr_start, max(curr_end, next_end))
            result.append(new_interval)
            
        else:
            # If they don't overlap, just add the current one
            result.append(intervals[i])
            
    # out of time
    return result

def test_MI():
    input_intervals = [(2, 3), (4, 8), (1, 2), (5, 7), (9, 12)]
    expected = [(4, 8), (1, 3), (9, 12)]
    result = mergeIntervals(input_intervals)
    assert result == expected, f"Expected {expected}, got {result}"

    input_intervals = [(5, 8), (6, 10), (2, 4), (3, 6)]
    expected = [(2, 10)]
    result = mergeIntervals(input_intervals)
    assert result == expected, f"Expected {expected}, got {result}"

    input_intervals = [(10, 12), (5, 6), (7, 9), (1, 3)]
    expected = [(10, 12), (5, 6), (7, 9), (1, 3)]
    result = mergeIntervals(input_intervals)
    assert result == expected, f"Expected {expected}, got {result}"


if __name__ == "__main__":
    test_MI()