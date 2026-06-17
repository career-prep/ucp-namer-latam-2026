/*Data Structure: array (rolling dp, two vars)
Algorithm: tabulation, dp[i] = cost[i] + min(dp[i-1], dp[i-2])
Technique: dynamic programming (tabulation)
Time Complexity: O(n)
Space Complexity: O(1)
Time Taken: 15 mins 33 seconds
*/

#include<iostream>
#include<vector>
#include <algorithm>

using namespace std;

/*
1. dp[i] = min toll to stand on stair i = cost[i] + min(dp[i-1], dp[i-2]).
2. base: dp[0]=cost[0], dp[1]=cost[1] (can start on either).
3. answer = min(dp[n-1], dp[n-2]) since the climb can end on either of the last two.
4. only need the last two dp values so roll them in two ints.
*/

int MinCostStairClimbing(vector<int> cost){
    int n = cost.size();
    if(n == 0) return 0;
    if(n == 1) return cost[0];

    int prev2 = cost[0]; //dp[i-2]
    int prev1 = cost[1]; //dp[i-1]
    for(int i = 2; i < n; i++){
        int curr = cost[i] + min(prev1, prev2);
        prev2 = prev1;
        prev1 = curr;
    }
    return min(prev1, prev2);
}

int main(){
    vector<vector<int>> tests = {
        {4, 1, 6, 3, 5, 8},
        {11, 8, 3, 4, 9, 13, 10}
    };
    vector<int> expected = {9, 25};

    for(size_t i = 0; i < tests.size(); i++){
        cout << "Actual result: " << MinCostStairClimbing(tests[i]);
        cout << "  Expected result: " << expected[i] << endl;
    }
}

/* psudocode/thoughts/logic
goal: min total toll to climb, paying only for stairs you step on, moving 1 or 2 at a time
restraints: must start on stair 0 or 1, last step lands on n-1 or n-2

strategy: dp where dp[i] is the cheapest way to be standing on stair i. to get to i you came from
i-1 or i-2, so dp[i] = cost[i] + min(dp[i-1], dp[i-2]). the "start on 0 or 1" rule is just the
two base cases, and the "end on n-1 or n-2" rule means the answer is the min of the last two dp
values, not just dp[n-1]. only ever need the previous two, so O(1) space with two rolling ints.

check on [4,1,6,3,5,8]: dp = 4,1,7,4,9,12 -> min(dp5,dp4)=min(12,9)=9. matches (stairs 1,3,4).
*/
