# Question 8 (Merge Intervals)
# Time Complexity: O(n log n)
# Space Complexity: O(n)
# Time spent: 35 mins 45s



def merge_intervals(intervals):
  
    intervals.sort()

    merged = []

   
    current_start = intervals[0][0]
    current_end = intervals[0][1]

   
    for i in range(1, len(intervals)):
        next_start = intervals[i][0]
        next_end = intervals[i][1]

        
        if next_start <= current_end:
            current_end = max(current_end, next_end)
        else:
            merged.append((current_start, current_end))
            current_start = next_start
            current_end = next_end


    merged.append((current_start, current_end))

    return merged



#Tests
print(merge_intervals([(2,3), (4,8), (1,2), (5,7), (9,12)]))
# [(1,3), (4,8), (9,12)]

print(merge_intervals([(1,4), (2,5), (3,6)]))
# [(1,6)]

print(merge_intervals([(1,2), (3,4), (5,6)]))
# [(1,2), (3,4), (5,6)]

print(merge_intervals([(1,10)]))
# [(1,10)]
