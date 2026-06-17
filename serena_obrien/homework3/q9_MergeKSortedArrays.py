# Time complexity: O(n log k), k = # of arrays, n = # of elements
# Space complexity: O(k) 

# Technique: Heap
import heapq

def MergeKSortedArrays(k, arr):
    heap = []
    res = []

    for i in range(k):
        if arr[i]:
            heapq.heappush(heap, (arr[i][0], i, 0))

    while heap:
        val, i, j = heapq.heappop(heap)
        res.append(val)

        if j + 1 < len(arr[i]):
            heapq.heappush(heap, (arr[i][j+1], i, j+1))

    return res

if __name__ == "__main__":
    inputs = (
        (2, [[1, 2, 3, 4, 5], [1, 3, 5, 7, 9]]),
        (3, [[1, 4, 7, 9], [2, 6, 7, 10, 11, 13, 15], [3, 8, 12, 13, 16]])
    )

    for k, arr in inputs:
        print(MergeKSortedArrays(k, arr))

# ~ time spent: 35 minutes