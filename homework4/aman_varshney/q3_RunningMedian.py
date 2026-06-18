# spent 25 minutes
# Maintain two heaps
# TC - O(nlogn)
# SC - O(n)

import heapq


def running_median(stream: list[int | float]) -> list[int | float]:
    """Return the median for a stream of numbers"""
    lower = []  # max-heap (for lower half of numbers)
    upper = []  # min-heap (for upper half of numbers)
    medians = []

    for num in stream:
        # Add the new number to lower half and move its max to upper
        heapq.heappush(lower, -num)
        heapq.heappush(upper, -heapq.heappop(lower))

        # Rebalance so lower half has the same number / one more element than upper half
        if len(upper) > len(lower):
            heapq.heappush(lower, -heapq.heappop(upper))

        # Record new median
        if len(lower) > len(upper):
            medians.append(-lower[0])
        else:
            medians.append((-lower[0] + upper[0]) / 2)

    return medians



def run_tests() -> None:
    print("Running tests")
    assert running_median([1, 11, 4, 15, 12]) == [1, 6, 4, 7.5, 11]
    print("All tests passed")


if __name__ == "__main__":
    run_tests()