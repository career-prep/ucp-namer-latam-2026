# Method: Heap
# Space Complexity: O(N + K)
# Time Complexity: O(N log K)
# Total Time Taken: 30 mins

import heapq

def MergeKSortedArrays(num, arr):
    heap = []
    result = []

# Add first element of each array to heap
    for i in range(num):
        heapq.heappush(heap, (arr[i][0], i, 0))
    
    while heap: # Remove first item from heap
        val, arr_id, elm_id = heapq.heappop(heap)
        result.append(val)
# Add the next element from the array of element we just removed from heap
        next_elm = elm_id + 1
        if next_elm < len(arr[arr_id]):
            heapq.heappush(heap, (arr[arr_id][next_elm], arr_id, next_elm))
    return result

print(MergeKSortedArrays(2, [[1, 2, 3, 4, 5], [1, 3, 5, 7, 9]])) # Expected: [1, 1, 2, 3, 3, 4, 5, 5, 7, 9]
print(MergeKSortedArrays(3, [[1, 4, 7, 9], [2, 6, 7, 10, 11, 13, 15], [3, 8, 12, 13, 16]])) # Expected: [1, 2, 3, 4, 6, 7, 7, 8, 9, 10, 11, 12, 13, 13, 15, 16]