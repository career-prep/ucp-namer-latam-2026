# Technique: Dynamic programming
# Time Complexity: O(n)
# Space Complexity: O(n)

def min_cost_stairs(cost):
    n = len(cost)

    dp = [0] * n

    dp[0] = cost[0]
    dp[1] = cost[1]

    for i in range(2, n):
        dp[i] = cost[i] + min(dp[i - 1], dp[i - 2])

    return min(dp[n - 1], dp[n - 2])


def main():
    cost1 = [4, 1, 6, 3, 5, 8]
    cost2 = [11, 8, 3, 4, 9, 13, 10]

    print(min_cost_stairs(cost1))  # 9
    print(min_cost_stairs(cost2))  # 25


if __name__ == "__main__":
    main()
    
#Time 30 min