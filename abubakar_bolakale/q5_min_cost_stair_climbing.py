def min_cost_climbing_stairs(cost: list[int]) -> int:
    n = len(cost)
    if n == 0:
        return 0
    if n == 1:
        return cost[0]
    
    first = cost[0]
    second = cost[1]
    
    for i in range(2, n):
        curr = cost[i] + min(first, second)
        first = second
        second = curr
        
    return min(first, second)


if __name__ == "__main__":
    assert min_cost_climbing_stairs([4, 1, 6, 3, 5, 8]) == 9
    assert min_cost_climbing_stairs([11, 8, 3, 4, 9, 13, 10]) == 25
    assert min_cost_climbing_stairs([]) == 0
    assert min_cost_climbing_stairs([10]) == 10
    assert min_cost_climbing_stairs([10, 15]) == 10

    assert min_cost_climbing_stairs([1, 1, 1, 1]) == 2
    assert min_cost_climbing_stairs([0, 0, 0, 0]) == 0
    assert min_cost_climbing_stairs([5, 1, 3, 2]) == 3
    assert min_cost_climbing_stairs([1, 100, 1, 100, 1]) == 3

    print("All MinCostStairClimbing tests passed!")
