//Time Complexity: O(n^2 * log n), where n is the number of cells
//Space Complexity: O(n^2)

//Technique: 2D Prefix Sum + Binary Search

#include "bits/stdc++.h"
using namespace std;

void solve_largestSquareOfOnes(vector<vector<int>> &grid){

    int n = grid.size();

    //Build the 2d prefix sum of the grid, to calculate the sum for a certain rectangle in constant time with precalculations.
    vector<vector<int>> prefix_sum(n, vector<int>(n));

    for(int i = 0; i < n; ++i){
        for(int j = 0; j < n; ++j){

            int result = grid[i][j];

            if(i) result += prefix_sum[i - 1][j];
            if(j) result += prefix_sum[i][j - 1];

            if(i && j) result -= prefix_sum[i - 1][j - 1];

            prefix_sum[i][j] = result;
        }
    }

    int answer = 0;

    //Iterate through all the possible top left corners of our answer.
    for(int i = 0; i < n; ++i){
        for(int j = 0; j < n; ++j){

            //The maximum side of the square depends on the positions of the top left corner.
            int max_len_side = min(n - i, n - j);

            int l = 0, r = max_len_side + 1;

            //Binary search the lenght of the side of the square.
            while(l + 1 < r){

                int mid = l + ((r - l) >> 1);

                int row_A = i + mid - 1;
                int row_a = i;

                int col_B = j + mid - 1;
                int col_b = j;

                int result = 0;

                //Calculate the sum using our prefix sum 2d array.

                result += prefix_sum[row_A][col_B];

                if(row_a) result -= prefix_sum[row_a - 1][col_B];
                if(col_b) result -= prefix_sum[row_A][col_b - 1];

                if(row_a && col_b) result += prefix_sum[row_a - 1][col_b - 1];

                //If the sum is equal to the area, we have a possible answer and look for a largest one.
                if(result == mid * mid) l = mid;
                else r = mid;
            }

            //Update our answer if possible.
            answer = max(answer, l);
        }
    }

    cout << answer << "\n";
}

int main(){

    /*
        vector<vector<int>> grid = {
            {0, 1, 0, 1},
            {0, 0, 1, 1},
            {0, 1, 1, 1}, 
            {0, 0, 1, 1}
        };
    */

    vector<vector<int>> grid = {
        {0, 1, 0, 1, 1},
        {0, 0, 1, 1, 1},
        {1, 1, 1, 1, 1}, 
        {1, 1, 1, 1, 1},
        {0, 1, 1, 0, 0}
    };

    solve_largestSquareOfOnes(grid);

    return 0;
}

//Time Spent: 17 minutes.