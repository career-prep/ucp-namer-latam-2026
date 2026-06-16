/*
    Technique:
    - Dynamic Programming (Bottom-Up)

    - Let dp[i] be the minimum cost to reach stair i.
    - To reach stair i:
        - stair i-1
        - stair i-2
    => dp[i] = cost[i] + min(dp[i-1], dp[i-2])

    - Initialize:
        dp[0] = cost[0]
        dp[1] = cost[1]

    - Build the solution from left to right.
    - Top of the stairs:
        - the last stair (n-1)
        - the second-to-last stair (n-2)

    - Therefore, the answer is:

        min(dp[n-1], dp[n-2])

    Time Complexity: O(n) n = number of stairs
    Space Complexity: O(n)

    Time spent: 40 minutes
*/

#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

int minCostClimbingStairs(vector<int> &cost)
{
    int n = cost.size();

    if (n == 0)
        return 0;
    if (n == 1)
        return cost[0];

    vector<int> dp(n);

    dp[0] = cost[0];
    dp[1] = cost[1];

    for (int i = 2; i < n; i++)
    {
        dp[i] = cost[i] + min(dp[i - 1], dp[i - 2]);
    }

    return min(dp[n - 1], dp[n - 2]);
}

int main()
{
    vector<int> cost1 = {4, 1, 6, 3, 5, 8};
    vector<int> cost2 = {11, 8, 3, 4, 9, 13, 10};

    cout << "Example 1: "
         << minCostClimbingStairs(cost1)
         << endl;

    cout << "Example 2: "
         << minCostClimbingStairs(cost2)
         << endl;

    return 0;
}