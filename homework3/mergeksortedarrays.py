# Data Structure: Min Heap (Priority Queue)
# Technique: Push the first element of each array into the heap with its
#             array index and element index, then pop min and push next element
#             from that same array until all elements are merged
# Time Complexity: O(n log k) where n = total elements, k = number of arrays
# Space Complexity: O(n + k)

import heapq

def mergeKSortedArrays(k, arrays):
    result = []
    # min heap stores (value, array_index, element_index)
    heap = []

    for i in range(k):
        if arrays[i]:
            heapq.heappush(heap, (arrays[i][0], i, 0))

    while heap:
        val, arrIdx, elemIdx = heapq.heappop(heap)
        result.append(val)
        nextIdx = elemIdx + 1
        if nextIdx < len(arrays[arrIdx]):
            heapq.heappush(heap, (arrays[arrIdx][nextIdx], arrIdx, nextIdx))

    return result


# Test 1: k=2, [[1,2,3,4,5],[1,3,5,7,9]] -> [1,1,2,3,3,4,5,5,7,9]
print(mergeKSortedArrays(2, [[1, 2, 3, 4, 5], [1, 3, 5, 7, 9]]))

# Test 2: k=3, [[1,4,7,9],[2,6,7,10,11,13,15],[3,8,12,13,16]] -> [1,2,3,4,6,7,7,8,9,10,11,12,13,13,15,16]
print(mergeKSortedArrays(3, [[1, 4, 7, 9], [2, 6, 7, 10, 11, 13, 15], [3, 8, 12, 13, 16]]))

# Test 3: k=1, single array passthrough
print(mergeKSortedArrays(1, [[1, 2, 3]]))          # [1, 2, 3]

# Test 4: arrays with one element each
print(mergeKSortedArrays(3, [[5], [1], [3]]))       # [1, 3, 5]

# Test 5: one empty array in the mix
print(mergeKSortedArrays(3, [[1, 4], [], [2, 3]])) # [1, 2, 3, 4]

# Time spent: ~30 minutes