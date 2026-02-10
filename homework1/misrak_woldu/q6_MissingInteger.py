# ============================================================
# Technique: Binary Search Variation (sorted array with one missing number)
# Time: O(log n)
# Space: O(1)
# ============================================================

from typing import List

def missing_integer(sorted_nums: List[int], n: int) -> int:
    """
    Return the missing integer from the range 1..n. We are given a sorted list of length n-1 that contains all numbers 1..n
    except one missing number.
    """
    left_index = 0
    right_index = len(sorted_nums) - 1

    while left_index <= right_index:
        middle_index = (left_index + right_index) // 2
        expected_value = middle_index + 1
        actual_value = sorted_nums[middle_index]

        if actual_value == expected_value:
            left_index = middle_index + 1
        else:
            
            right_index = middle_index - 1

    return left_index + 1


def run_tests() -> None:
    # examples from the prompt
    assert missing_integer([1, 2, 3, 4, 6, 7], 7) == 5
    assert missing_integer([1], 2) == 2
    assert missing_integer([1, 2, 3, 4, 5, 6, 7, 8, 10, 11, 12], 12) == 9

    # edge cases
    assert missing_integer([2, 3, 4, 5], 5) == 1          # missing first number
    assert missing_integer([1, 2, 3, 4], 5) == 5          # missing last number
    assert missing_integer([1, 3], 3) == 2                # small input, missing middle
    assert missing_integer([2], 2) == 1                   # smallest missing 1

    print("All tests passed")


if __name__ == "__main__":
    run_tests()
