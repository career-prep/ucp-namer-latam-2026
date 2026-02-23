from typing import List

# ============================================================
# Technique: Fixed-size sliding window
# Time Complexity: O(n)
# Space Complexity: O(1)
# ============================================================

def max_mean_subarray(numbers: List[int], k: int) -> float:
    """
    Return the maximum mean (average) of any contiguous subarray of size k.
    """

    if k <= 0:
        raise ValueError("k must be a positive integer")
    if k > len(numbers):
        raise ValueError("k cannot be larger than the array length")

    current_window_sum = 0
    for index in range(k):
        current_window_sum += numbers[index]

    max_window_sum = current_window_sum

    for window_end_index in range(k, len(numbers)):
        window_start_index = window_end_index - k

        current_window_sum -= numbers[window_start_index]

        current_window_sum += numbers[window_end_index]

        if current_window_sum > max_window_sum:
            max_window_sum = current_window_sum

    return max_window_sum / k


def run_tests() -> None:
    # Given examples
    assert max_mean_subarray([4, 5, -3, 2, 6, 1], 2) == 4.5
    assert max_mean_subarray([4, 5, -3, 2, 6, 1], 3) == 3.0

    # Additional cases
    assert max_mean_subarray([1, 1, 1, -1, -1, 2, -1, -1], 3) == 1.0
    assert max_mean_subarray([1, 1, 1, -1, -1, 2, -1, -1, 6], 5) == 1.0

    print("All tests passed")


if __name__ == "__main__":
    run_tests()

