def change_ways(amount: int, coins: list[int]) -> int:
    dp = [0] * (amount + 1)
    dp[0] = 1
    
    for coin in coins:
        for i in range(coin, amount + 1):
            dp[i] += dp[i - coin]
            
    return dp[amount]


if __name__ == "__main__":
    coins = [2, 5, 10]
    assert change_ways(20, coins) == 6
    assert change_ways(15, coins) == 3
    assert change_ways(0, coins) == 1
    assert change_ways(3, coins) == 0

    assert change_ways(5, [5]) == 1
    assert change_ways(10, [1]) == 1
    assert change_ways(4, [2]) == 1
    assert change_ways(7, [2, 3]) == 1
    assert change_ways(1, [2, 5]) == 0
    assert change_ways(6, [1, 2, 5]) == 5

    print("All CoinChange tests passed!")
