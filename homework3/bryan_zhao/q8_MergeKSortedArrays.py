# Data Structure: Heap
# Time Complexity: O(N * k)? N is the total # of elements and k is the # of arrays
# Space Complexity: O(k) to store an element for each of the k arrays

import heapq

def merge_k_sorted_arrays(k, arrays):
    min_heap = []

    for i in range(k):
        if arrays[i]:
            heapq.heappush(min_heap, (arrays[i][0], i, 0))
        
    result = []

    while min_heap:
        val, arr_index, elem_index = heapq.heappop(min_heap)
        result.append(val)

        if elem_index + 1 < len(arrays[arr_index]):
            next_val = arrays[arr_index][elem_index + 1]
            heapq.heappush(min_heap, (next_val, arr_index, elem_index + 1))
        
    return result

test_arr_1 = [[1, 2, 3, 4, 5], [1, 3, 5, 7, 9]]
test_arr_2 = [[1, 4, 7, 9], [2, 6, 7, 10, 11, 13, 15], [3, 8, 12, 13, 16]]

print(merge_k_sorted_arrays(2, test_arr_1))
print(merge_k_sorted_arrays(3, test_arr_2))

# Time Spent: 38 min