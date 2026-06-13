# Question 5: MinCostStairClimbing

# Technique: Dynamic programming (tabulation)
# dp[i] = minimum cost to step on stair i.
# dp[i] = cost[i] + min(dp[i-1], dp[i-2])
# Base cases: dp[0] = cost[0], dp[1] = cost[1].
# Answer: min(dp[n-1], dp[n-2]) since the last step can be either of the two.

# Time Complexity:  O(n)
# Space Complexity: O(n) — can reduce to O(1) with two variables but kept
#                   as array for clarity


def minCostStairClimbing(cost):
    n = len(cost)
    if n == 0:
        return 0
    if n == 1:
        return cost[0]
    dp = [0] * n
    dp[0] = cost[0]
    dp[1] = cost[1]
    for i in range(2, n):
        dp[i] = cost[i] + min(dp[i - 1], dp[i - 2])
    return min(dp[n - 1], dp[n - 2])
# Time Complexity = O(n), Space Complexity = O(n)


# --- Tests ---

print("Input [4,1,6,3,5,8]:", minCostStairClimbing([4, 1, 6, 3, 5, 8]))
# Expected: 9 (stairs 1,3,4 → 1+3+5)

print("Input [11,8,3,4,9,13,10]:", minCostStairClimbing([11, 8, 3, 4, 9, 13, 10]))
# Expected: 25 (stairs 1,3,5 → 8+4+13)

print("Input [1,100]:", minCostStairClimbing([1, 100]))
# Expected: 1

print("Input [10,15,20]:", minCostStairClimbing([10, 15, 20]))
# Expected: 15

print("Input [0]:", minCostStairClimbing([0]))
# Expected: 0

# Spent a total of 20 mins on this question
