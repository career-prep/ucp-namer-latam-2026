/*Data Structure: array (dp table)
Algorithm: tabulation, coins on the OUTER loop so we count combinations not permutations
Technique: dynamic programming (tabulation)
Time Complexity: O(#coins * k)
Space Complexity: O(k)
Time Taken: 21 mins 26 seconds
*/

#include<iostream>
#include<vector>

using namespace std;

/*
1. dp[s] = number of ways to make sum s. dp[0] = 1 (use nothing).
2. loop coins on the OUTSIDE, then sums coin..k on the inside.
3. dp[s] += dp[s - coin].
4. answer = dp[k].
*/

int CoinChange(vector<int> coins, int k){
    vector<long long> dp(k + 1, 0);
    dp[0] = 1;
    for(int coin : coins){
        for(int s = coin; s <= k; s++){
            dp[s] += dp[s - coin];
        }
    }
    return (int)dp[k];
}

int main(){
    vector<int> coins = {2, 5, 10};

    cout << "sum=20  Actual: " << CoinChange(coins, 20) << "  Expected: 6" << endl;
    cout << "sum=15  Actual: " << CoinChange(coins, 15) << "  Expected: 3" << endl;
}

/* psudocode/thoughts/logic
goal: number of ways to make sum k from the coin denominations (unlimited coins)
restraints: order doesnt matter — 2+5 and 5+2 are the SAME way, count once

strategy: dp[s] = ways to make s. seed dp[0]=1. the part that matters: coins go on the OUTER
loop. that way each coin is "considered" once and every combination is counted in a fixed coin
order, so we never double count permutations. if you flip the loops (sums outer, coins inner)
you count ordered sequences instead, which gives the wrong (bigger) number.
*/
