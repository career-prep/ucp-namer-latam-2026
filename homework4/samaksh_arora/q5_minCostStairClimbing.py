#Samaksh Arora
#Question 5 - Min Cost Stair Climbing
#Dynamic programming (Tabulation)
#Time Complexity: O(n) where n is the number of stairs
#Space Complexity: O(1)
#Time Spent: 33 minutes



def minCostStairClimbing(costs):
    n = len(costs)
    if n == 0:
        return 0
    elif n == 1:
        return costs[0]

    prev2 = costs[0]
    prev1 = costs[1]

    for i in range(2, n):
        current = costs[i] + min(prev1, prev2)
        prev2 = prev1
        prev1 = current

    return min(prev1, prev2)

#Test Cases
assert minCostStairClimbing([4, 1, 6, 3, 5, 8]) == 9
assert minCostStairClimbing([11, 8, 3, 4, 9, 13, 10]) == 25

# Extra:
assert minCostStairClimbing([1, 2, 3, 4, 5]) == 6
assert minCostStairClimbing([10]) == 10
