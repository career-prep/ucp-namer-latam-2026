# Data structure: Heap (min-heap)
# Time: O(n log k) where n is total number of elements
# Space: O(k)

import heapq


def merge_k_sorted_arrays(arrays):
    result = []
    heap = []  # (value, which_array, index_within_array)

    for arr_i in range(len(arrays)):
        if arrays[arr_i]:
            first_val = arrays[arr_i][0]
            heapq.heappush(heap, (first_val, arr_i, 0))

    while heap:
        value, arr_i, idx = heapq.heappop(heap)
        result.append(value)
        next_idx = idx + 1
        if next_idx < len(arrays[arr_i]):
            heapq.heappush(heap, (arrays[arr_i][next_idx], arr_i, next_idx))

    return result


print("Correct:", [1, 1, 2, 3, 3, 4, 5, 5, 7, 9])
print("Output: ", merge_k_sorted_arrays([[1, 2, 3, 4, 5], [1, 3, 5, 7, 9]]))
print()

print("Correct:", [1, 2, 3, 4, 6, 7, 7, 8, 9, 10, 11, 12, 13, 13, 15, 16])
print("Output: ", merge_k_sorted_arrays([[1, 4, 7, 9], [2, 6, 7, 10, 11, 13, 15], [3, 8, 12, 13, 16]]))
print()

print("Correct:", [])
print("Output: ", merge_k_sorted_arrays([]))
print()

# time taken: 18 min
