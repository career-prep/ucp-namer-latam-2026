def min_cost_stair_climbing(costs):
    n = len(costs)
    dp = [0] * (n + 1)

    dp[0] = 0
    dp[1] = 0

    for i in range(2, n + 1):
        dp[i] = min(dp[i - 1] + costs[i - 1], dp[i - 2] + costs[i - 2])
    
    return dp[n]


if __name__ == "__main__":
    print(min_cost_stair_climbing([4, 1, 6, 3, 5, 8])) # 9
    print(min_cost_stair_climbing([11, 8, 3, 4, 9, 13, 10])) # 25
    print(min_cost_stair_climbing([1, 2])) # 1
    print(min_cost_stair_climbing([0, 0, 0])) # 0

# Time spent: 30 minutes
