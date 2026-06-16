# Data Structure: Min-Heap (used as a k-way merge frontier)
#
# Push the first element of each of the k arrays onto a min-heap, tagged with
# (value, array_index, element_index). Repeatedly pop the smallest, append to
# the result, and push the next element from the same source array.
#
# Naively concatenating then sorting would be O(N log N) where N is the total
# number of elements; the heap approach takes advantage of the per-array sort
# to do it in O(N log k).
#
# Time complexity:  O(N log k), where N = total elements across all arrays.
# Space complexity: O(k) for the heap (plus O(N) for the output).

import heapq


def merge_k_sorted_arrays(k, arrays):
    heap = []
    for i in range(k):
        if arrays[i]:
            heapq.heappush(heap, (arrays[i][0], i, 0))

    result = []
    while heap:
        val, arr_idx, elem_idx = heapq.heappop(heap)
        result.append(val)
        next_idx = elem_idx + 1
        if next_idx < len(arrays[arr_idx]):
            heapq.heappush(heap, (arrays[arr_idx][next_idx], arr_idx, next_idx))
    return result


# test cases
if __name__ == "__main__":
    assert merge_k_sorted_arrays(2, [[1, 2, 3, 4, 5], [1, 3, 5, 7, 9]]) == \
        [1, 1, 2, 3, 3, 4, 5, 5, 7, 9]

    assert merge_k_sorted_arrays(
        3,
        [[1, 4, 7, 9], [2, 6, 7, 10, 11, 13, 15], [3, 8, 12, 13, 16]],
    ) == [1, 2, 3, 4, 6, 7, 7, 8, 9, 10, 11, 12, 13, 13, 15, 16]

    # edge cases
    assert merge_k_sorted_arrays(0, []) == []
    assert merge_k_sorted_arrays(1, [[1, 2, 3]]) == [1, 2, 3]
    assert merge_k_sorted_arrays(2, [[], [1, 2]]) == [1, 2]

    print("yay!!")

# Time spent: ~15 minutes
