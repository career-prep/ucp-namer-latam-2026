import heapq

# Technique: Maintain two heaps
# Data Structure: Max Heap + Min Heap
# Time Complexity: O(n log n)
# Space Complexity: O(n)


def running_median(numbers: list[int]) -> list[float | int]:
    if not numbers:
        return []

    lower_half = []  # max heap using negative numbers
    upper_half = []  # min heap
    medians = []

    for number in numbers:
        add_number(number, lower_half, upper_half)
        rebalance_heaps(lower_half, upper_half)
        medians.append(get_median(lower_half, upper_half))

    return medians


def add_number(number: int, lower_half: list[int], upper_half: list[int]) -> None:
    if not lower_half or number <= -lower_half[0]:
        heapq.heappush(lower_half, -number)
    else:
        heapq.heappush(upper_half, number)


def rebalance_heaps(lower_half: list[int], upper_half: list[int]) -> None:
    if len(lower_half) > len(upper_half) + 1:
        moved_number = -heapq.heappop(lower_half)
        heapq.heappush(upper_half, moved_number)

    elif len(upper_half) > len(lower_half):
        moved_number = heapq.heappop(upper_half)
        heapq.heappush(lower_half, -moved_number)


def get_median(lower_half: list[int], upper_half: list[int]) -> float | int:
    if len(lower_half) == len(upper_half):
        median = (-lower_half[0] + upper_half[0]) / 2

        if median.is_integer():
            return int(median)

        return median

    return -lower_half[0]


def run_tests() -> None:
    assert running_median([1, 11, 4, 15, 12]) == [1, 6, 4, 7.5, 11]

    assert running_median([]) == []

    assert running_median([5]) == [5]

    assert running_median([5, 10]) == [5, 7.5]

    assert running_median([10, 5, 1]) == [10, 7.5, 5]

    assert running_median([1, 2, 3, 4, 5]) == [1, 1.5, 2, 2.5, 3]

    assert running_median([5, 5, 5]) == [5, 5, 5]

    assert running_median([-1, -2, -3]) == [-1, -1.5, -2]

    print("All tests passed")


if __name__ == "__main__":
    run_tests()
