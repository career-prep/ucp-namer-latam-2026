# Sort the array of tuples then solve.
# O(nlog(n)) Time complexity because we needed to sort the array of n tuples
# O(n) Space complexity where n is the original size of the input tuple array

inter1 = [(2, 3), (4, 8), (1, 2), (5, 7), (9, 12)]
inter2 = [(5, 8), (6, 10), (2, 4), (3, 6)]
inter3 = [(10, 12), (5, 6), (7, 9), (1, 3)]

def MergeIntervals(intervals):

    if len(intervals) == 1:
        return intervals

    # Sort the intervals based on start of each interval
    sortedIntervals = sorted(intervals)

    # This will hold the merged intervals
    merged = []

    curr_start, curr_end = sortedIntervals[0]

    scan = 1

    while scan < len(sortedIntervals):

        next_start, next_end = sortedIntervals[scan]

        # Overlap
        if next_start <= curr_end:

            if next_end > curr_end:
                curr_end = next_end
            
        else:
            # No overlap

            # Add our current interval to merged array
            merged.append((curr_start, curr_end))

            curr_start = next_start
            curr_end = next_end

        scan += 1 # Keep scanning

    # Append final interval
    merged.append((curr_start, curr_end))

    
    # Now I need to sort all merged intervals based on their original position in the input array...
    # Perhaps I should have attached the index of the tuple to the tuples before merging, then somehow sorted based on that original index
    # and then stripped the tuples of the index I attached to them earlier?


    return merged



print(MergeIntervals(inter1))
print(MergeIntervals(inter2))
print(MergeIntervals(inter3))



# 40 minutes