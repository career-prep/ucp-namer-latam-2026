#dynamic programming
#time complexity: O(n)
#space complexity: O(n)

def MinCostStairClimb(stairs):
    costs = [0] * len(stairs)

    if not stairs:
        return 0
    if len(stairs) == 1:
        return stairs[0]

    costs[0] = stairs[0]
    costs[1] = stairs[1]

    for i in range(2, len(stairs)):
        costs[i] = stairs[i] + min(costs[i-1],costs[i-2])

    return min(costs[len(stairs)-1], costs[len(stairs)-2])

#test cases
input= [4, 1, 6, 3, 5, 8]
print(MinCostStairClimb(input))

input2 = [11, 8, 3, 4, 9, 13, 10]
print(MinCostStairClimb(input2))
