# Technique: Dynamic Programming - Tabulation
# Data Structure: Array
# Time Complexity: O(c * k), where c is the number of coin denominations and k is the target sum
# Space Complexity: O(k)


def coin_change(coins: list[int], target_sum: int) -> int:
    if target_sum < 0:
        return 0

    if target_sum == 0:
        return 1

    if not coins:
        return 0

    unique_coins = sorted(set(coin for coin in coins if coin > 0))

    ways = [0] * (target_sum + 1)

    ways[0] = 1

    for coin in unique_coins:
        for current_sum in range(coin, target_sum + 1):
            ways[current_sum] += ways[current_sum - coin]

    return ways[target_sum]


def run_tests() -> None:
    assert coin_change([2, 5, 10], 20) == 6

    assert coin_change([2, 5, 10], 15) == 3

    assert coin_change([], 10) == 0

    assert coin_change([1, 2, 5], 0) == 1

    assert coin_change([1], 5) == 1

    assert coin_change([2], 3) == 0

    assert coin_change([1, 2, 5], 5) == 4

    assert coin_change([5, 2, 10], 20) == 6

    assert coin_change([2, 2, 5, 10], 20) == 6

    assert coin_change([0, 2, 5], 10) == 2

    assert coin_change([2, 5, 10], -1) == 0

    print("All tests passed")


if __name__ == "__main__":
    run_tests()
