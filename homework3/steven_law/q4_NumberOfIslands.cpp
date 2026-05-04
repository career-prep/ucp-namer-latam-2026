/*Data Structure: Graph
Algorithm: DFS (generic traversal works, going with DFS)
Time Complexity: O(n*m)
Space Complexity: O(n*m)
Time Taken: 34 mins 28 seconds
*/

#include<iostream>
#include<vector>
#include<unordered_map>
#include <string>
#include <unordered_set>

using namespace std;

void dfs(vector<vector<int>>& grid, int r, int c){
    int rows = grid.size();
    int cols = grid[0].size();

    if(r < 0 || r >= rows || c < 0 || c >= cols) return;
    if(grid[r][c] != 1) return;

    grid[r][c] = -1; // mark visited in place so i dont need a separate visited set

    dfs(grid, r+1, c);
    dfs(grid, r-1, c);
    dfs(grid, r, c+1);
    dfs(grid, r, c-1);
}

int numberOfIslands(vector<vector<int>> grid){
    if(grid.empty()) return 0;

    int count = 0;
    int rows = grid.size();
    int cols = grid[0].size();

    for(int r = 0; r < rows; r++){
        for(int c = 0; c < cols; c++){
            if(grid[r][c] == 1){
                count++;
                dfs(grid, r, c);
            }
        }
    }
    return count;
}

int main(){
    vector<vector<int>> grid1 = {
        {1, 0, 1, 1, 1},
        {1, 1, 0, 1, 1},
        {0, 1, 0, 0, 0},
        {0, 0, 0, 1, 0},
        {0, 0, 0, 0, 0}
    };
    cout << "Test 1 Result: " << numberOfIslands(grid1) << " (Expected: 3)" << endl;

    vector<vector<int>> grid2 = {
        {1, 0, 0},
        {0, 0, 0}
    };
    cout << "Test 2 Result: " << numberOfIslands(grid2) << " (Expected: 1)" << endl;

    return 0;
}

/* psudocode/thoughts/logic
goal: count contiguous groups of 1s in a binary matrix
restraints: 1s connected horizontally or vertically count as one island, not diagonally

strategy:  dfs / flood fill... iterate every cell and when you hit a 1 fire off a dfs
from that cell that marks all connected 1s as visited. each fresh dfs = a new island so
just bump a counter

first attempt i forgot to mark cells as visited inside the dfs. so the dfs would go right,
the cell to the right would dfs back left, left would dfs right again - infinite recursion.
got a stack overflow on test 1. abandoned version below.

fix: mark visited. could use a separate 2d bool array but the input is mutable so im just
setting visited cells to -1. that way the base case `grid[r][c] != 1` skips both 0s and -1s.

bfs would also work, big O is the same.
*/

//////// first attempt, infinite recursion because i wasnt tracking visited
/*
void dfs_v1(vector<vector<int>>& grid, int r, int c){
    int rows = grid.size();
    int cols = grid[0].size();
    if(r < 0 || r >= rows || c < 0 || c >= cols) return;
    if(grid[r][c] != 1) return;

    dfs_v1(grid, r+1, c);
    dfs_v1(grid, r-1, c);
    dfs_v1(grid, r, c+1);
    dfs_v1(grid, r, c-1);
}
*/
