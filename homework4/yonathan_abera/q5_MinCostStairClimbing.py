# Technique: Dynamic programming (tabulation)
# Time Complexity: O(n)
# Space Complexity: O(1)

def min_cost_stair_climbing(cost):
    n = len(cost)
    if n == 0:
        return 0
    if n == 1:
        return cost[0]
    prev2 = cost[0]
    prev1 = cost[1]
    for i in range(2, n):
        cur = cost[i] + min(prev1, prev2)
        prev2, prev1 = prev1, cur
    return min(prev1, prev2)

print(min_cost_stair_climbing([4, 1, 6, 3, 5, 8]))
print(min_cost_stair_climbing([11, 8, 3, 4, 9, 13, 10]))
print(min_cost_stair_climbing([10]))
print(min_cost_stair_climbing([10, 15]))
print(min_cost_stair_climbing([1, 100, 1, 1, 1, 100, 1, 1, 100, 1]))

# Time spent: 50
