# Array/String Technique: Dynamic programming - Tabulation
# Time Complexity: O(N) 
# Space Complexity: O(1)

def minCostClimbingStairs(cost: list[int]) -> int:
    down_one = down_two = 0
    for i in range(2, len(cost) + 1):
        temp = down_one
        down_one = min(down_one + cost[i - 1], down_two + cost[i - 2])
        down_two = temp
    return down_one

if __name__ == "__main__":
    print("Min cost for [10, 15, 20]:", minCostClimbingStairs([10, 15, 20]))
    print("Min cost for [1, 100, 1, 1, 1, 100, 1, 1, 100, 1]:", minCostClimbingStairs([1, 100, 1, 1, 1, 100, 1, 1, 100, 1]))

# Time Spent: 15 minutes