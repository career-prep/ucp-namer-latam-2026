# Runtime: O(klog(k))
# Space complexity: O(k)
# Data Structure: Heap
# Algorithm: N/A

import heapq
def mergeKSortedArrays(k, lists):
    heap = []
    res = []
    for i in range(k):
        if lists[i]:
            heapq.heappush(heap, (lists[i][0], i, 0))

    while heap:
        curr, i, idx = heapq.heappop(heap)
        res.append(curr)
        if idx+1 < len(lists[i]):
            heapq.heappush(heap, (lists[i][idx+1], i, idx+1))
    return res

print(mergeKSortedArrays( 2, [[1, 2, 3, 4, 5], [1, 3, 5, 7, 9]]) == [1, 1, 2, 3, 3, 4, 5, 5, 7, 9])
print(mergeKSortedArrays(3, [[1, 4, 7, 9], [2, 6, 7, 10, 11, 13, 15], [3, 8, 12, 13, 16]]) == [1, 2, 3, 4, 6, 7, 7, 8, 9, 10, 11, 12, 13, 13, 15, 16])
print(mergeKSortedArrays(0, []) == [])
print(mergeKSortedArrays(2, [[1,2,3,4], []]) == [1,2,3,4])
print(mergeKSortedArrays(3, [[1],[2],[1]]) == [1,1,2])

# Note: I feel like I'm supposed to use a tree for this, but I could not figure it out.
# Time Spent: 40:00
