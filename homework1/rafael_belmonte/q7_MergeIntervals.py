#sort the array, then solve
#time complexity: O(n log n) due to sorting
#space complexity: O(n)
#18 minutes
#I assumed it is okay for the output to be sorted as well

def merge_intervals(arr):
    arr.sort(key=lambda x: x[0])
    merged = []
    for interval in arr:
        if not merged or merged[-1][1] < interval[0]: # no overlap
            merged.append(interval)
        else: # overlap
            merged[-1][1] = max(merged[-1][1], interval[1])
    return merged

# test cases

array1 = [[2,3],[4,8],[1,2],[5,7],[9,12]]
assert merge_intervals(array1) == [[1,3],[4,8],[9,12]]

array2 = [[5,8],[6,10],[2,4],[3,6]]
assert merge_intervals(array2) == [[2,10]]

array3 = [[10,12],[5,6],[7,9],[1,3]]
assert merge_intervals(array3) == [[1,3],[5,6],[7,9],[10,12]]

print("yippie yoopie!")