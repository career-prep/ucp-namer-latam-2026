import heapq

# Data Structure: Heap
# Algorithm: Push the first element of each array into the heap; repeatedly extract
#            the minimum, append to result, then push the next element from that same
#            array — heap size never exceeds k
# Time Complexity: O(n log k) — n total elements, each push/pop costs O(log k)
# Space Complexity: O(k)
# Given an array of k sorted arrays, merge them into a single sorted array.


def mergeKSortedArrays(k, arrays):
    heap = []
    for i in range(k):
        if arrays[i]:
            heapq.heappush(heap, (arrays[i][0], i, 0))

    result = []
    while heap:
        val, arr_i, elem_i = heapq.heappop(heap)
        result.append(val)
        if elem_i + 1 < len(arrays[arr_i]):
            heapq.heappush(
                heap, (arrays[arr_i][elem_i + 1], arr_i, elem_i + 1))

    return result


# Testing:
print(mergeKSortedArrays(2, [[1, 2, 3, 4, 5], [1, 3, 5, 7, 9]]))
# [1,1,2,3,3,4,5,5,7,9]
print(mergeKSortedArrays(
    3, [[1, 4, 7, 9], [2, 6, 7, 10, 11, 13, 15], [3, 8, 12, 13, 16]]))
