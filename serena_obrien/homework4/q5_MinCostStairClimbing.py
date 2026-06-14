from math import factorial

# Time complexity: O(n)
# Space complexity: O(1)

# Technique: Dynamic programming: tabulation

# space optimized: O(1)
def MinCostStairClimbing(costs):
    n = len(costs)

    if n == 1:
        return costs[0]

    dp = [0] * n

    prev2 = costs[0]
    prev1 = costs[1]

    for i in range(2, n):
        dp[i] = costs[i] + min(prev2, prev1)
        prev2 = prev1
        prev1 = dp[i]

    return min(dp[n-1], dp[n-2])

# space not optimized: O(n)
# def MinCostStairClimbing(costs):
#     n = len(costs)

#     dp = [0] * n

#     dp[0] = costs[0]
#     dp[1] = costs[1]

#     for i in range(2, n):
#         dp[i] = costs[i] + min(dp[i-2], dp[i-1])

#     return min(dp[n-1], dp[n-2])

if __name__ == "__main__":
    inputs = [[4, 1, 6, 3, 5, 8], [11, 8, 3, 4, 9, 13, 10]]
    for input in inputs:
        print(MinCostStairClimbing(input))

# ~ time spent: ~30 minutes