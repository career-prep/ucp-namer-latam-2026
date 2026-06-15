#Time: O(Coins * Amount)
#Space: O(Amount)

def coinChange(coins: list[int], amount: int) -> int:
        dp = [0] * (amount + 1)
        coins.sort()
 
        for i in range(1, amount+1):
            minn = float('inf')
            
            for coin in coins:
                diff = i - coin
                if diff < 0:
                    break
                minn = min(minn, dp[diff] + 1)
            
            dp[i] = minn
        
        if dp[amount] < float('inf'):
            return dp[amount]
        else:
            return -1


#Time-taken: 35 minutes


import unittest


class TestCoinChange(unittest.TestCase):

    def test_exact_amount(self):
        self.assertEqual(coinChange([1, 2, 5], 11), 3)

    def test_impossible_amount(self):
        self.assertEqual(coinChange([2], 3), -1)

    def test_zero_amount(self):
        self.assertEqual(coinChange([1, 2, 5], 0), 0)


if __name__ == "__main__":
    unittest.main()