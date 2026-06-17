# Runtime:
# Time: O(n * k)
# Space: O(k)
# Implementation time: 30 minutes


def coin_change(coins, target):
    #1. Declare variables
    dp = [0] * (target + 1)
    dp[0] = 1

    #2. Process each coin
    for coin in coins:

        #3. Update ways
        for amount in range(coin, target + 1):
            dp[amount] += dp[amount - coin]

    #4. Return result
    return dp[target]


def Test_CoinChange():
    #1. Declare coins
    coins = [2, 5, 10]

    #2. Declare test cases
    targets = [20, 15]

    #3. Run tests
    for target in targets:
        result = coin_change(coins, target)

        print("Coins:", coins)
        print("Sum:", target)
        print("Output:", result)
        print()


if __name__ == "__main__":
    Test_CoinChange()