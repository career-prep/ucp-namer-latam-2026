# ============================================================
# Technique: Forward two-pointer
# Time: O(n)
# Space: O(1)
# ============================================================

from typing import List

def dedup_array(numbers: List[int]) -> List[int]:
    """
    Given a sorted array of non-negative integers, remove duplicates in-place.
    Unique values are moved to the left, and remaining positions are filled with -1.
    """

    if not numbers:
        return numbers

    write_index = 1

    for read_index in range(1, len(numbers)):
        
        if numbers[read_index] != numbers[read_index - 1]:
            numbers[write_index] = numbers[read_index]
            write_index += 1

    for fill_index in range(write_index, len(numbers)):
        numbers[fill_index] = -1

    return numbers

def run_tests() -> None:
    # examples from the prompt
    assert dedup_array([1, 2, 2, 3, 3, 3, 4, 4, 4]) == [1, 2, 3, 4, -1, -1, -1, -1, -1]
    assert dedup_array([0, 0, 1, 4, 5, 5, 8, 9, 9, 10, 11, 15, 15]) == [
        0, 1, 4, 5, 8, 9, 10, 11, 15, -1, -1, -1, -1
    ]
    assert dedup_array([1, 3, 4, 8, 10, 12]) == [1, 3, 4, 8, 10, 12]

    # edge cases
    assert dedup_array([]) == []
    assert dedup_array([5, 5, 5]) == [5, -1, -1]
    assert dedup_array([0]) == [0]

    print("All tests passed")


if __name__ == "__main__":
    run_tests()
