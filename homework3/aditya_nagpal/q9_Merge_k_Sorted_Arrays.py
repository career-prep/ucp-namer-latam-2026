# Time Taken: 28 mins
# Time Complexity: O(N log k)
# N = total number of elements across all arrays
# k = number of sorted arrays
#
# Why?
# - We push at most k elements into the heap at the start.
# - For every element, we pop once from the heap.
# - Each heap operation costs O(log k).


import heapq

def mergeKSortedArrays(k, arrays):
    min_heap = []
    result = []

    # Put the first element of each array into the heap
    # Store: (value, array_index, element_index)
    for i in range(k):
        if len(arrays[i]) > 0:
            heapq.heappush(min_heap, (arrays[i][0], i, 0))

    # Keep taking the smallest current element
    while min_heap:
        value, array_index, element_index = heapq.heappop(min_heap)

        # Add smallest value to final result
        result.append(value)

        # Move to the next element in the same array
        next_index = element_index + 1

        # If next element exists, push it into heap
        if next_index < len(arrays[array_index]):
            next_value = arrays[array_index][next_index]
            heapq.heappush(min_heap, (next_value, array_index, next_index))

    return result


print(mergeKSortedArrays(
    2,
    [[1, 2, 3, 4, 5], [1, 3, 5, 7, 9]]
))


print(mergeKSortedArrays(
    3,
    [[1, 4, 7, 9], [2, 6, 7, 10, 11, 13, 15], [3, 8, 12, 13, 16]]
))
