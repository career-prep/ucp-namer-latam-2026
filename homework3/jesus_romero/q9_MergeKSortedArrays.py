# Technique: K-Way Merge using a Min-Heap (Priority Queue)

import heapq

def mergeKSortedArrays(k, arrays): # Time Complexity: O(N log k), Space Complexity: O(N)
    # 1. Use a min-heap to keep track of the smallest current element from each of the k arrays
    # Store tuples: (value, array_index, element_index)
    min_heap = []
    
    # 2. Initial Step: Put the first element of each non-empty array into the heap
    for i in range(len(arrays)):
        if arrays[i]:
            heapq.heappush(min_heap, (arrays[i][0], i, 0))
    
    result = []
    
    # 3. While the heap is not empty, extract the minimum and move to the next element in that array
    while min_heap:
        val, arr_idx, element_idx = heapq.heappop(min_heap)
        result.append(val)
        
        # 4. If the array we just pulled from has more elements, push the next one into the heap
        if element_idx + 1 < len(arrays[arr_idx]):
            next_val = arrays[arr_idx][element_idx + 1]
            heapq.heappush(min_heap, (next_val, arr_idx, element_idx + 1))
            
    return result

class Test:
    def run_tests(self):
        # 1. Test Case: 2 arrays
        k1 = 2
        arrs1 = [[1, 2, 3, 4, 5], [1, 3, 5, 7, 9]]
        assert mergeKSortedArrays(k1, arrs1) == [1, 1, 2, 3, 3, 4, 5, 5, 7, 9]
        
        # 2. Test Case: 3 arrays of varying lengths
        k2 = 3
        arrs2 = [[1, 4, 7, 9], [2, 6, 7, 10, 11, 13, 15], [3, 8, 12, 13, 16]]
        expected2 = [1, 2, 3, 4, 6, 7, 7, 8, 9, 10, 11, 12, 13, 13, 15, 16]
        assert mergeKSortedArrays(k2, arrs2) == expected2
        
        # 3. Test Case: Empty arrays within list
        assert mergeKSortedArrays(2, [[], [1, 2]]) == [1, 2]

        print("MergeKSortedArrays tests passed")