# Technique: Dynamic Programming (Tabulation)
# Time Complexity: O(n)
# Space Complexity: O(1)

def min_cost_stairs(cost):
    if len(cost) == 1:
        return cost[0]
    prev2 = cost[0]
    prev1 = cost[1]
    for i in range(2, len(cost)):
        curr = cost[i] + min(prev1, prev2)
        prev2 = prev1
        prev1 = curr

    return min(prev1, prev2)

# Time Taken: 10mins 16secs

# Testcases:
cost_1 = [4, 1, 6, 3, 5, 8]
print(min_cost_stairs(cost_1))

cost_2 = [11, 8, 3, 4, 9, 13, 10]
print(min_cost_stairs(cost_2))

#My testcases:
cost_3 = [5, 2]
print(min_cost_stairs(cost_3))

cost_4 = [1, 100, 1]
print(min_cost_stairs(cost_4))
