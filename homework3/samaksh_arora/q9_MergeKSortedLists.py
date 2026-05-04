# Merge K Sorted Arrays
# Data Structure: Min Heap
# Time Complexity: O(N log K) where N is total number of elements and K is number of arrays
# Space Complexity: O(N + K) where N is the size of the result array and K is the heap size

import heapq

def MergeKSortedArrays(k, list_of_sorted_arrays):
    if not list_of_sorted_arrays:
        return []
    
    result_array = []
    min_heap = []

    for idx in range(k):
        if list_of_sorted_arrays[idx]:
            first_element_value = list_of_sorted_arrays[idx][0]
        heapq.heappush(min_heap, (first_element_value, idx, 0))

    while min_heap:
        min_value, array_idx, element_idx = heapq.heappop(min_heap)
        result_array.append(min_value)

        next_element_idx = element_idx + 1
        if (next_element_idx < len(list_of_sorted_arrays[array_idx])):
            next_element_value = list_of_sorted_arrays[array_idx][next_element_idx]
            heapq.heappush(min_heap, (next_element_value, array_idx, next_element_idx))

    return result_array


#Test Cases
print(MergeKSortedArrays(2, [[1, 2, 3, 4, 5], [1, 3, 5, 7, 9]]))
# expected: [1, 1, 2, 3, 3, 4, 5, 5, 7, 9]

print(MergeKSortedArrays(3, [[1, 4, 7, 9], [2, 6, 7, 10, 11, 13, 15], [3, 8, 12, 13, 16]]))
# expected: [1, 2, 3, 4, 6, 7, 7, 8, 9, 10, 11, 12, 13, 13, 15, 16]