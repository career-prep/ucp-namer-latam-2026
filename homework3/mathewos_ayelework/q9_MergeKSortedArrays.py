# Algorithm: k-way merge using a min heap of (value, source_array_index, element_index)
# Time Complexity: O(N log k)  where N is the total number of elements
# Space Complexity: O(k) for the heap

import heapq


def mergeKSortedArrays(arrays):
    heap = []
    for i, arr in enumerate(arrays):
        if arr:
            heapq.heappush(heap, (arr[0], i, 0))

    result = []
    while heap:
        val, i, j = heapq.heappop(heap)
        result.append(val)
        if j + 1 < len(arrays[i]):
            heapq.heappush(heap, (arrays[i][j + 1], i, j + 1))
    return result


print("MergeKSortedArrays Results:")

print(mergeKSortedArrays([[1, 2, 3, 4, 5], [1, 3, 5, 7, 9]]))
print(mergeKSortedArrays([[1, 4, 7, 9], [2, 6, 7, 10, 11, 13, 15], [3, 8, 12, 13, 16]]))
print(mergeKSortedArrays([]))
print(mergeKSortedArrays([[]]))
print(mergeKSortedArrays([[1], [2], [3]]))
print(mergeKSortedArrays([[], [1, 2, 3], []]))
