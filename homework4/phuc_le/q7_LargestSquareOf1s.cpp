/*
    Technique:
    - Dynamic Programming (Bottom-Up)

    - Let dp[i][j] be the size of the largest square
      consisting entirely of 1's whose bottom-right
      corner is at cell (i, j).

    - If matrix[i][j] = 0:
        dp[i][j] = 0
      because a square of 1's cannot end at a cell
      containing 0.

    - If matrix[i][j] = 1:
        We need the top, left, and top-left cells
        to also form squares of 1's.

        Therefore:

        dp[i][j] = 1 + min({dp[i-1][j],
                            dp[i][j-1],
                            dp[i-1][j-1]
                            })

    Why the minimum?
    - The current square can only be extended by one if all three neighboring squares exist.
    - The smallest of the three determines the largest square that can be formed.

    - Ans = max val in DP table

    Time Complexity: O(n * m)
    Space Complexity: O(n * m)

    Time spent: 40 minutes
*/

#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

int largestSquareOf1s(vector<vector<int>> &matrix)
{
    int n = matrix.size();
    if (n == 0)
        return 0;

    int m = matrix[0].size();

    vector<vector<int>> dp(n, vector<int>(m, 0));

    int ans = 0;

    for (int i = 0; i < n; i++)
    {
        dp[i][0] = matrix[i][0];
        ans = max(ans, dp[i][0]);
    }

    for (int j = 0; j < m; j++)
    {
        dp[0][j] = matrix[0][j];
        ans = max(ans, dp[0][j]);
    }

    for (int i = 1; i < n; i++)
    {
        for (int j = 1; j < m; j++)
        {
            if (matrix[i][j] == 1)
            {
                dp[i][j] = 1 + min({dp[i - 1][j], dp[i][j - 1], dp[i - 1][j - 1]});
                ans = max(ans, dp[i][j]);
            }
        }
    }

    return ans;
}

int main()
{
    vector<vector<int>> matrix = {
        {0, 1, 0, 1},
        {0, 0, 1, 1},
        {0, 1, 1, 1},
        {0, 0, 1, 1}};

    cout << "Largest square size: "
         << largestSquareOf1s(matrix)
         << endl;

    return 0;
}