# Time Taken: 30 minutes 
# Time Complexity: O(klog(N)), where N is the max length for any sub array in arrays
# Space Complexity: O(k)
# Algorith: Heap

import heapq

def merge_k_sorted_arrays(k, arrays):
    """
    Given k sorted arrays, merge them into one sorted array.
    """
    minH = []
    heapq.heapify(minH)
    for i in range(len(arrays)):
        heapq.heappush(minH, (arrays[i][0], i, 0))
    ans = []
    while minH:
        num, arr_i, i = heapq.heappop(minH)
        ans.append(num)
        if i < len(arrays[arr_i])-1:
            heapq.heappush(minH, (arrays[arr_i][i+1], arr_i, i+1))
    return ans
    
if __name__ == "__main__":
    arrays_1 = [
        [1, 2, 3, 4, 5],
        [1, 3, 5, 7, 9],
    ]

    arrays_2 = [
        [1, 4, 7, 9],
        [2, 6, 7, 10, 11, 13, 15],
        [3, 8, 12, 13, 16],
    ]

    print(merge_k_sorted_arrays(2, arrays_1))  # Expected: [1, 1, 2, 3, 3, 4, 5, 5, 7, 9]
    print(merge_k_sorted_arrays(3, arrays_2))  # Expected: [1, 2, 3, 4, 6, 7, 7, 8, 9, 10, 11, 12, 13, 13, 15, 16]
