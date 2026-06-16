/*Data Structure: 2D array (dp grid)
Algorithm: tabulation, dp[i][j] = 1 + min(up, left, up-left) when cell is 1
Technique: dynamic programming (tabulation)
Time Complexity: O(R*C)
Space Complexity: O(R*C)
Time Taken: 27 mins 40 seconds
*/

#include<iostream>
#include<vector>
#include <algorithm>

using namespace std;

/*
1. dp[i][j] = side length of the biggest all-1s square whose bottom-right corner is (i,j).
2. if cell is 0 -> dp[i][j] = 0.
3. if cell is 1 -> on the top row/left col its just 1, otherwise 1 + min(dp up, dp left, dp up-left).
4. track the max dp value, thats the answer (dimension).
*/

int LargestSquareOf1s(vector<vector<int>> matrix){
    int R = matrix.size();
    if(R == 0) return 0;
    int C = matrix[0].size();

    vector<vector<int>> dp(R, vector<int>(C, 0));
    int best = 0;

    for(int i = 0; i < R; i++){
        for(int j = 0; j < C; j++){
            if(matrix[i][j] == 1){
                if(i == 0 || j == 0) dp[i][j] = 1;
                else dp[i][j] = 1 + min({dp[i-1][j], dp[i][j-1], dp[i-1][j-1]});
                best = max(best, dp[i][j]);
            }
        }
    }
    return best;
}

int main(){
    vector<vector<int>> m1 = {
        {0,1,0,1},
        {0,0,1,1},
        {0,1,1,1},
        {0,0,1,1}
    };
    vector<vector<int>> m2 = {
        {0,1,0,1,1},
        {0,0,1,1,1},
        {1,1,1,1,1},
        {1,1,1,1,1},
        {0,1,1,0,0}
    };

    cout << "Actual result: " << LargestSquareOf1s(m1) << "  Expected result: 2" << endl;
    cout << "Actual result: " << LargestSquareOf1s(m2) << "  Expected result: 3" << endl;
}

/* psudocode/thoughts/logic
goal: side length of the largest square made of only 1s
restraints: square, not rectangle — all four sides equal

strategy: dp where dp[i][j] = biggest all-1s square ENDING (bottom-right) at (i,j). a square can
extend to (i,j) only if the three squares touching its top-left (up, left, up-left) can all
support it, so its limited by the smallest of those three, +1 for the current cell. zeros reset
to 0. answer is the largest dp value seen. the min-of-three is the whole trick — one short
neighbor caps how big the square here can be.
*/
