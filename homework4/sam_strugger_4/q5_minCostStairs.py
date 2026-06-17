# This is a tabulation approach
# Also, I have solved this problem before

# O(n) time complexity and O(n) space complexity

def minCostStairs(cost):
    min_costs = {0:0,1:0}

    if len(cost) < 2:
        return 0

    for i in range(len(cost)):
        if i <= 1:
            min_costs[i] = 0

        else:
            min_costs[i] = min(min_costs[i-1] + cost[i-1], min_costs[i-2] + cost[i-2])

    return min(min_costs[len(cost)-2] + cost[-2], min_costs[len(cost)-1] + cost[-1])

# This took me 5 minutes

# Test cases
test1 = minCostStairs([4,1,6,3,5,8])
print(test1)

test2 = minCostStairs([11,8,4,9,13,10])
print(test2)

test3 = minCostStairs([1])
print(test3)