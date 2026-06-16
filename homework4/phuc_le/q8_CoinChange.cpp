/*
    Technique:
    - Dynamic Programming (Bottom-Up)

    - Let dp[i] be the number of ways to make a sum of i.

    - Base case: dp[0] = 1
    - For each coin:
        - Update all sums that can include this coin.
        - If we can make sum (i - coin), then by adding
          the current coin we can also make sum i.

    Recurrence:
        dp[i] += dp[i - coin]

    Why does this work?
    - dp[i - coin] stores the number of ways to make
      the smaller sum (i - coin).
    - Appending the current coin to each of those ways
      gives new ways to make sum i.
    - Iterating through coins first ensures combinations are counted only once.

    Time Complexity: O(n * sum): n = number of coin.
    Space Complexity: O(sum)

    Time spent: 40 minutes
*/

#include <iostream>
#include <vector>

using namespace std;

int coinChange(vector<int> &coins, int sum)
{
    vector<long long> dp(sum + 1, 0);
    dp[0] = 1;

    for (int coin : coins)
    {
        for (int i = coin; i <= sum; i++)
        {
            dp[i] += dp[i - coin];
        }
    }

    return dp[sum];
}

int main()
{
    vector<int> coins = {2, 5, 10};

    int sum1 = 20;
    int sum2 = 15;

    cout << "Coins: [2, 5, 10]\n\n";

    cout << "Sum: " << sum1 << "\n";
    cout << "Output: " << coinChange(coins, sum1) << "\n\n";

    cout << "Sum: " << sum2 << "\n";
    cout << "Output: " << coinChange(coins, sum2) << "\n";

    return 0;
}