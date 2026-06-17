# Data Structure: Heap
# Time Complexity: O(n log k)
# Space Complexity: O(n)

import heapq

def merge_k_arrays(arrays):
    heap = []
    result = []

    for i, arr in enumerate(arrays):
        if arr:
            heapq.heappush(heap, (arr[0], i, 0))

    while heap:
        val, i, j = heapq.heappop(heap)
        result.append(val)

        if j + 1 < len(arrays[i]):
            heapq.heappush(heap, (arrays[i][j+1], i, j+1))

    return result

# Time Taken: 15mins 34secs

# Test Cases
print(merge_k_arrays([[1,2,3,4,5],[1,3,5,7,9]]))
print(merge_k_arrays([[1,4,7,9],[2,6,7,10,11,13,15],[3,8,12,13,16]]))

# Edge Cases
print(merge_k_arrays([]))
print(merge_k_arrays([[]]))
print(merge_k_arrays([[1]]))