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

struct TestCase
{
    string name;
    vector<vector<int>> input;
    int expected;
};

int main()
{
    vector<TestCase> testCases = {
        // --- Baseline Tests ---
        {"Empty Grid", {}, 0},
        {"Empty Row", {{}}, 0},
        {"All Water", {{0, 0}, {0, 0}}, 0},
        {"All Land", {{1, 1}, {1, 1}}, 1},

        // --- Dimensional Boundaries ---
        {"Single Land Cell", {{1}}, 1},
        {"Single Water Cell", {{0}}, 0},
        {"1D Single Row", {{1, 0, 1, 1, 0, 1}}, 3},
        {"1D Single Column", {{1}, {0}, {1}, {1}, {0}, {1}}, 3},

        // --- Complex Geometries ---
        {"Diagonal Islands", {{1, 0, 0}, {0, 1, 0}, {0, 0, 1}}, 3},
        {"Snake Island", {{1, 1, 1}, {0, 0, 1}, {1, 1, 1}, {1, 0, 0}, {1, 1, 1}}, 1},
        {"Donut with Lake and Inner Island", {{1, 1, 1, 1, 1}, {1, 0, 0, 0, 1}, {1, 0, 1, 0, 1}, {1, 0, 0, 0, 1}, {1, 1, 1, 1, 1}}, 2}, // Outer ring = 1, Inner center = 1
        {"Inward Spiral", {{1, 1, 1, 1, 1}, {0, 0, 0, 0, 1}, {1, 1, 1, 0, 1}, {1, 0, 0, 0, 1}, {1, 1, 1, 1, 1}}, 1},

        // --- Density Variations ---
        {"Checkerboard (High Density Disjoint)", {{1, 0, 1, 0, 1}, {0, 1, 0, 1, 0}, {1, 0, 1, 0, 1}}, 8},
        {"Two Continents Split by River", {{1, 1, 0, 1, 1}, {1, 1, 0, 1, 1}, {0, 0, 0, 0, 0}, {1, 1, 0, 1, 1}, {1, 1, 0, 1, 1}}, 4},

        // --- Original Given Example ---
        {"Standard LeetCode Example 1", {{1, 0, 1, 1, 1}, {1, 1, 0, 1, 1}, {0, 1, 0, 0, 0}, {0, 0, 0, 1, 0}, {0, 0, 0, 0, 0}}, 3}};

    Solution sol;
    int passed = 0;

    cout << "=== NUMBER OF ISLANDS TEST EXECUTION ===\n\n";

    for (const auto &tc : testCases)
    {
        vector<vector<int>> gridCopy = tc.input;
        int result = sol.NumberOfIslands(gridCopy);

        if (result == tc.expected)
        {
            passed++;
            cout << "✅ Passed: " << tc.name << "\n";
        }
        else
        {
            cout << "❌ Failed: " << tc.name << " | Expected " << tc.expected << ", got " << result << "\n";
        }
    }

    cout << "\n--- Final Results: " << passed << "/" << testCases.size() << " Tests Passed ---\n";

    return 0;
}