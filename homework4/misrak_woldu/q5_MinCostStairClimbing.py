# Technique: Dynamic Programming - Tabulation
# Data Structure: Array
# Time Complexity: O(n)
# Space Complexity: O(n)


def min_cost_stair_climbing(costs: list[int]) -> int:
    if not costs:
        return 0

    if len(costs) == 1:
        return costs[0]

    min_cost = [0] * len(costs)

    min_cost[0] = costs[0]
    min_cost[1] = costs[1]

    for stair_index in range(2, len(costs)):
        min_cost[stair_index] = costs[stair_index] + min(
            min_cost[stair_index - 1],
            min_cost[stair_index - 2],
        )

    return min(min_cost[-1], min_cost[-2])


def run_tests() -> None:
    assert min_cost_stair_climbing([4, 1, 6, 3, 5, 8]) == 9

    assert min_cost_stair_climbing([11, 8, 3, 4, 9, 13, 10]) == 25

    assert min_cost_stair_climbing([]) == 0

    assert min_cost_stair_climbing([5]) == 5

    assert min_cost_stair_climbing([5, 10]) == 5

    assert min_cost_stair_climbing([10, 5]) == 5

    assert min_cost_stair_climbing([1, 100, 1, 1, 1, 100, 1, 1, 100, 1]) == 6

    print("All tests passed")


if __name__ == "__main__":
    run_tests()
