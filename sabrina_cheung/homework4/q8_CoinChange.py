# Method: DP
# Space Complexity: O(k)
# Time Complexity: O(k * N)
# Total Time Taken: 20 mins
# For each type of coin we find the possible sums up to the input sum. Do this for each coin. Then return the number at k index


def CoinChange(coins, k):
    DP = [0] * (k + 1)

    DP[0] = 1

    for coin in coins:
        for i in range(coin, k + 1):
            DP[i] += DP[i - coin]
    return DP[k]

print(CoinChange([2, 5, 10], 20))
print(CoinChange([2, 5, 10], 15))
print(CoinChange([2, 5, 10], 0))
print(CoinChange([2, 5, 10], 1))