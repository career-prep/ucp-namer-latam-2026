import heapq
def mergeKSortedArrays(k, arr):
    """
    idea:
    use heap to push all elements in array under format (value, index of array, value index in that array)
    keep popping element out of the heap and append that into result 
        if element idex + 1 < length of that array -> push new element into heap with updated value, idex, and value index
    
    Time complexity: O(nlogk) (n: number of elements in all arrays)
    Space complexity: O(n + k)
    """
    heap = []
    res = []
    for i in range(k):
        if arr[i]:
            heapq.heappush(heap, (arr[i][0], i, 0))
    
    while heap:
        value, idx, eleIdx = heapq.heappop(heap)
        res.append(value)
        if eleIdx + 1 < len(arr[idx]):
            heapq.heappush(heap, (arr[idx][eleIdx + 1], idx, eleIdx + 1))
    return res


if __name__ == "__main__":
    example1 = [[1, 2, 3, 4, 5], [1, 3, 5, 7, 9]]
    example2 = [[1, 4, 7, 9], [2, 6, 7, 10, 11, 13, 15], [3, 8, 12, 13, 16]]

    print(mergeKSortedArrays(2, example1))  # Expected: [1, 1, 2, 3, 3, 4, 5, 5, 7, 9]
    print(mergeKSortedArrays(3, example2))  # Expected: [1, 2, 3, 4, 6, 7, 7, 8, 9, 10, 11, 12, 13, 13, 15, 16]
