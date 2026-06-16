# Technique: Dynamic programming - tabulation
# time complexity: O(n)
# space complexity: O(n)

def min_cost_stair_climbing(costs):
    if not costs:
        return 0
    if len(costs) == 1:
        return costs[0]

    dp = [0] * len(costs)
    dp[0] = costs[0]
    dp[1] = costs[1]
    for i in range(2, len(costs)):
        dp[i] = costs[i] + min(dp[i - 1], dp[i - 2])
    return min(dp[-1], dp[-2])

#test cases
assert min_cost_stair_climbing([4, 1, 6, 3, 5, 8]) == 9
assert min_cost_stair_climbing([11, 8, 3, 4, 9, 13, 10]) == 25
assert min_cost_stair_climbing([2, 3]) == 2
assert min_cost_stair_climbing([]) == 0

# edge cases
assert min_cost_stair_climbing([7]) == 7
assert min_cost_stair_climbing([10, 15, 20]) == 15
assert min_cost_stair_climbing([1, 100, 1, 1, 1, 100, 1, 1, 100, 1]) == 6
assert min_cost_stair_climbing([0, 0, 0]) == 0

print("yay!!")

# Time spent: ~20 minutes
