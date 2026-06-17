//Time Complexity: O(n * k)
//Where n is the number of coins and k the target sum.

//Space Complexity: O(k)

//Technique: DP (Tabulation).

#include "bits/stdc++.h"
using namespace std;

void solve_coinChange(vector<int> coins, int k){

    vector<int> dp(k + 1);

    //Define dp[i] as the number of non-ordered ways to achieve sum i with the coins we have.
    //We have our base case dp[0]:
    dp[0] = 1;

    //Do the transition

    /*
        It is important to iterate through the coins first to calculate the answer correctly.
        If we do not do this, combinations like (1, 2) and (2, 1) would be counted as different.

    */

    for(int i = 0; i < coins.size(); ++i){
        for(int j = 1; j <= k; ++j){

            if(j - coins[i] >= 0){
                dp[j] = dp[j] + dp[j - coins[i]];
            }
        }
    }

    //dp[k] is our answer.
    cout << dp[k] << "\n";
}

int main(){

   vector<int> coins = {2, 5, 10};
   //int k = 20;
   int k = 15;

    solve_coinChange(coins, k);

    return 0;
}

//Time Spent: 12 minutes.