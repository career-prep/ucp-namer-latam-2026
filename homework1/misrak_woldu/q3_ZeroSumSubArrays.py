from typing import List, Dict

# ============================================================
# Technique: Hashing (one-directional running computation/total)
# Time Complexity: O(n)
# Space Complexity: O(n)
# ============================================================

def zero_sum_subarrays(numbers: List[int]) -> int:
    """
    Count how many subarrays sum to 0. A subarray means a continuous chunk of the array (like numbers[i:j+1]).
    """
    running_total = 0

    prefix_sum_counts: Dict[int, int] = {}

    prefix_sum_counts[0] = 1

    subarray_count = 0

    # Go through each value in the list one by one.
    for value in numbers:
        running_total += value

        subarray_count += prefix_sum_counts.get(running_total, 0)

        prefix_sum_counts[running_total] = prefix_sum_counts.get(running_total, 0) + 1

    return subarray_count


def run_tests() -> None:
    # Examples from the prompt
    assert zero_sum_subarrays([4, 5, 2, -1, -3, -3, 4, 6, -7]) == 2
    assert zero_sum_subarrays([1, 8, 7, 3, 11, 9]) == 0
    assert zero_sum_subarrays([8, -5, 0, -2, 3, -4]) == 2

    # Edge cases
    assert zero_sum_subarrays([]) == 0
    assert zero_sum_subarrays([0]) == 1
    assert zero_sum_subarrays([0, 0]) == 3 
    assert zero_sum_subarrays([1, -1]) == 1
    assert zero_sum_subarrays([1, -1, 1, -1]) == 4

    print("All tests passed")


if __name__ == "__main__":
    run_tests()
