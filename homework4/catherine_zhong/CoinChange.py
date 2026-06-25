#dynamic programming
#time compexlity: O(n*k)
#space complexity: O(n*k)

def CoinChange(coins, k):
    change = [[0]* (k+1) for _ in range(len(coins))]

    for i in range(len(coins)):
        change[i][0] = 1
    
    for i in range(len(coins)):
        for j in range(1, k+1):
            skip = change[i-1][j] if i > 0 else 0
            use = change[i][j-coins[i]] if j - coins[i] >= 0 else 0

            change[i][j] = skip + use

    return change[len(coins)-1][k]


#test cases
coins = [2, 5, 10]

sum = 20
print(CoinChange(coins, sum))

sum = 15
print(CoinChange(coins, sum))