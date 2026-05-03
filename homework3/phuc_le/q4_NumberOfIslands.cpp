#include <iostream>
#include <vector>
#include <string>
#include <stdexcept>

using namespace std;

class Solution
{
private:
    void dfs(vector<vector<int>> &grid, int r, int c)
    {
        int rows = grid.size();
        int cols = grid[0].size();

        if (r < 0 || c < 0 || r >= rows || c >= cols || grid[r][c] == 0)
        {
            return;
        }

        grid[r][c] = 0;      // Mark the cell as visited
        dfs(grid, r + 1, c); // down
        dfs(grid, r - 1, c); // up
        dfs(grid, r, c + 1); // right
        dfs(grid, r, c - 1); // left
    }

public:
    int NumberOfIslands(vector<vector<int>> &grid)
    {
        if (grid.empty())
        {
            return 0;
        }

        int rows = grid.size();
        int cols = grid[0].size();
        int islands = 0;

        for (int r = 0; r < rows; r++)
        {
            for (int c = 0; c < cols; c++)
            {
                if (grid[r][c] == 1)
                {
                    islands++;
                    dfs(grid, r, c);
                }
            }
        }

        return islands;
    }
};

// Helper function to run tests and format output
void runTest(int testNum, const string &description, const vector<vector<int>> &input, int expected)
{
    Solution sol;

    // Copy the grid because the NumberOfIslands function modifies it in-place
    vector<vector<int>> gridCopy = input;
    int result = sol.NumberOfIslands(gridCopy);

    cout << "Test " << testNum << " (" << description << "): ";
    if (result == expected)
    {
        cout << "PASS\n";
    }
    else
    {
        cout << "FAIL\n";
    }
    cout << "  Expected: " << expected << "\n";
    cout << "  Actual:   " << result << "\n";
    cout << "\n";
}

int main()
{
    cout << "--- Running NumberOfIslands Test Suite ---\n\n";

    // --- Baseline Tests ---
    runTest(1, "Empty Grid", {}, 0);

    runTest(2, "Empty Row", {{}}, 0);

    runTest(3, "All Water",
            {{0, 0},
             {0, 0}},
            0);

    runTest(4, "All Land",
            {{1, 1},
             {1, 1}},
            1);

    // --- Dimensional Boundaries ---
    runTest(5, "Single Land Cell", {{1}}, 1);

    runTest(6, "Single Water Cell", {{0}}, 0);

    runTest(7, "1D Single Row", {{1, 0, 1, 1, 0, 1}}, 3);

    runTest(8, "1D Single Column", {{1}, {0}, {1}, {1}, {0}, {1}}, 3);

    // --- Complex Geometries ---
    runTest(9, "Diagonal Islands",
            {{1, 0, 0},
             {0, 1, 0},
             {0, 0, 1}},
            3);

    runTest(10, "Snake Island",
            {{1, 1, 1},
             {0, 0, 1},
             {1, 1, 1},
             {1, 0, 0},
             {1, 1, 1}},
            1);

    runTest(11, "Donut with Lake and Inner Island",
            {{1, 1, 1, 1, 1},
             {1, 0, 0, 0, 1},
             {1, 0, 1, 0, 1},
             {1, 0, 0, 0, 1},
             {1, 1, 1, 1, 1}},
            2);

    runTest(12, "Inward Spiral",
            {{1, 1, 1, 1, 1},
             {0, 0, 0, 0, 1},
             {1, 1, 1, 0, 1},
             {1, 0, 0, 0, 1},
             {1, 1, 1, 1, 1}},
            1);

    // --- Density Variations ---
    runTest(13, "Checkerboard (High Density Disjoint)",
            {{1, 0, 1, 0, 1},
             {0, 1, 0, 1, 0},
             {1, 0, 1, 0, 1}},
            8);

    runTest(14, "Two Continents Split by River",
            {{1, 1, 0, 1, 1},
             {1, 1, 0, 1, 1},
             {0, 0, 0, 0, 0},
             {1, 1, 0, 1, 1},
             {1, 1, 0, 1, 1}},
            4);

    // --- Original Given Example ---
    runTest(15, "Standard LeetCode Example 1",
            {{1, 0, 1, 1, 1},
             {1, 1, 0, 1, 1},
             {0, 1, 0, 0, 0},
             {0, 0, 0, 1, 0},
             {0, 0, 0, 0, 0}},
            3);

    return 0;
}