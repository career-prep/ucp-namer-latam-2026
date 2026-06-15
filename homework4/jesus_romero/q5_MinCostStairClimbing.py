# Runtime:
# Time: O(n)
# Space: O(1)
# Implementation time:  25 minutes


def min_cost_stair_climbing(costs):
    #1. Handle edge cases
    if len(costs) == 0:
        return 0

    if len(costs) == 1:
        return costs[0]

    #2. Declare variables
    first = costs[0]
    second = costs[1]

    #3. Iterate through stairs
    for i in range(2, len(costs)):
        current = costs[i] + min(first, second)
        first = second
        second = current

    #4. Return minimum cost
    return min(first, second)


def Test_MinCostStairClimbing():
    #1. Declare test cases
    test_cases = [
        [4, 1, 6, 3, 5, 8],
        [11, 8, 3, 4, 9, 13, 10]
    ]

    #2. Run tests
    for costs in test_cases:
        result = min_cost_stair_climbing(costs)

        print("Input:", costs)
        print("Output:", result)
        print()


if __name__ == "__main__":
    Test_MinCostStairClimbing()