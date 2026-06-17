# Technique: Dynamic Programming - Tabulation
# Data Structure: Array
# Time Complexity: O(n^2)
# Space Complexity: O(n)


def catalan_numbers(n: int) -> list[int]:
    if n < 0:
        return []

    catalan = [0] * (n + 1)

    catalan[0] = 1

    for current_number in range(1, n + 1):
        total = 0

        for left_index in range(current_number):
            right_index = current_number - 1 - left_index
            total += catalan[left_index] * catalan[right_index]

        catalan[current_number] = total

    return catalan


def run_tests() -> None:
    assert catalan_numbers(0) == [1]

    assert catalan_numbers(1) == [1, 1]

    assert catalan_numbers(2) == [1, 1, 2]

    assert catalan_numbers(3) == [1, 1, 2, 5]

    assert catalan_numbers(5) == [1, 1, 2, 5, 14, 42]

    assert catalan_numbers(-1) == []

    print("All tests passed")


if __name__ == "__main__":
    run_tests()
