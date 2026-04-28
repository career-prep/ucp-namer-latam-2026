# Question 9: MergeKSortedArrays

# Data Structure: Heap (min-heap)
# Seed the heap with the first element of each array, then repeatedly
# extract the minimum and push the next element from the same array.
# Time Complexity: O(n log k) where n = total elements, k = number of arrays
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


# --- Tests ---

print("Test 1:", mergeKSortedArrays(2, [[1, 2, 3, 4, 5], [1, 3, 5, 7, 9]]))
# [1, 1, 2, 3, 3, 4, 5, 5, 7, 9]

print("Test 2:", mergeKSortedArrays(3, [[1, 4, 7, 9], [2, 6, 7, 10, 11, 13, 15], [3, 8, 12, 13, 16]]))
# [1, 2, 3, 4, 6, 7, 7, 8, 9, 10, 11, 12, 13, 13, 15, 16]

print("Test 3 (k=1):", mergeKSortedArrays(1, [[1, 2, 3]]))
# [1, 2, 3]

print("Test 4 (empty array):", mergeKSortedArrays(2, [[], [1, 2]]))
# [1, 2]

print("Test 5 (all empty):", mergeKSortedArrays(2, [[], []]))
# []

# Spent a total of 25 mins on this question
