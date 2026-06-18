def MinCostStairClimbing(input):
    if len(input) == 1:
        return input[0]
    
    dp = [float("inf")] * (len(input) + 1)
    dp[0],dp[1] = 0,0
    for i in range(2, len(input) + 1):
        dp[i] = min(dp[i-1] + input[i-1], dp[i-2] + input[i-2])
    return dp[i]
    
print(MinCostStairClimbing([4, 1, 6, 3, 5, 8]))
print(MinCostStairClimbing([11, 8, 3, 4, 9, 13, 10]))