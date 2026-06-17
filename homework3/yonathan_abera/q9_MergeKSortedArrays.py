# Data Structure: Heap
# Seed heap with first element of each array, then pop min and push next from same array.
# Time Complexity: O(N log k) where N = total elements, k = number of arrays
# Space Complexity: O(k) for the heap

import heapq

def mergeKSortedArrays(k, arrays):
    result = []
    heap = []

    for i in range(k):
        if arrays[i]:
            heapq.heappush(heap, (arrays[i][0], i, 0))
    while heap:
        val, arr_idx, elem_idx = heapq.heappop(heap)
        result.append(val)
        next_idx = elem_idx + 1
        if next_idx < len(arrays[arr_idx]):
            heapq.heappush(heap, (arrays[arr_idx][next_idx], arr_idx, next_idx))

    return result


print(mergeKSortedArrays(2, [[1, 2, 3, 4, 5], [1, 3, 5, 7, 9]]))
print(mergeKSortedArrays(3, [[1, 4, 7, 9], [2, 6, 7, 10, 11, 13, 15], [3, 8, 12, 13, 16]]))

# Time spent: ~20 minutes
