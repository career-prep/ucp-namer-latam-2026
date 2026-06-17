import heapq

# Data Structure: Min Heap
# Algorithm: K-way merge
# Time Complexity: O(n log k), where n is the total number of elements and k is the number of arrays
# Space Complexity: O(k) for the heap not counting the output array


def merge_k_sorted_arrays(sorted_arrays: list[list[int]]) -> list[int]:
    min_heap = []
    merged_values = []

    for array_index, current_array in enumerate(sorted_arrays):
        if current_array:
            first_value = current_array[0]
            heapq.heappush(min_heap, (first_value, array_index, 0))

    while min_heap:
        current_value, array_index, value_index = heapq.heappop(min_heap)
        merged_values.append(current_value)

        next_value_index = value_index + 1

        if next_value_index < len(sorted_arrays[array_index]):
            next_value = sorted_arrays[array_index][next_value_index]
            heapq.heappush(min_heap, (next_value, array_index, next_value_index))

    return merged_values


def run_tests() -> None:
    assert merge_k_sorted_arrays([
        [1, 2, 3, 4, 5],
        [1, 3, 5, 7, 9],
    ]) == [1, 1, 2, 3, 3, 4, 5, 5, 7, 9]

    assert merge_k_sorted_arrays([
        [1, 4, 7, 9],
        [2, 6, 7, 10, 11, 13, 15],
        [3, 8, 12, 13, 16],
    ]) == [1, 2, 3, 4, 6, 7, 7, 8, 9, 10, 11, 12, 13, 13, 15, 16]

    assert merge_k_sorted_arrays([]) == []
    assert merge_k_sorted_arrays([[]]) == []
    assert merge_k_sorted_arrays([[1, 2, 3]]) == [1, 2, 3]
    assert merge_k_sorted_arrays([[], [1], [], [0, 2]]) == [0, 1, 2]
    assert merge_k_sorted_arrays([[-3, -1], [-2, 0], [1]]) == [-3, -2, -1, 0, 1]

    print("All tests passed")


if __name__ == "__main__":
    run_tests()
