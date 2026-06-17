import heapq

def mergeKSortedArrays(k, arrays):
    result = []
    heap = []

    for i, arr, in enumerate(arrays):
        if arr:
            heapq.heappush(heap, (arr[0], i, 0))

    while heap:
        val, arr_idx, elem_idx = heapq.heappop(heap)
        result.append(val)

        next_idx = elem_idx + 1
        if next_idx < len(arrays[arr_idx]):
            heapq.heappush(heap, (arrays[arr_idx][next_idx], arr_idx, next_idx))

    return result

if __name__ == "__main__":

    print("Test 1:")
    print("Got:     ", mergeKSortedArrays(2, [[1, 2, 3, 4, 5], [1, 3, 5, 7, 9]]))
    print("Expected: [1, 1, 2, 3, 3, 4, 5, 5, 7, 9]")

    print("\nTest 2:")
    print("Got:     ", mergeKSortedArrays(3, [[1, 4, 7, 9], [2, 6, 7, 10, 11, 13, 15], [3, 8, 12, 13, 16]]))
    print("Expected: [1, 2, 3, 4, 6, 7, 7, 8, 9, 10, 11, 12, 13, 13, 15, 16]")
