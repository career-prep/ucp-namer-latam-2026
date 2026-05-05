//Time Complexity: O(N * M).
//Space Complexity: O(N * M) (recursion).
//Technique: Dfs.

#include "bits/stdc++.h"
using namespace std;


//Arrays to visit adjacent cells efficiently.
int row[] = {1, 0, -1, 0};
int col[] = {0, 1, 0, -1};


//Function to check if the cell is outside the matrix.
bool outOfBounds(int i, int j, int n, int m){
    if(i < 0 || i >= n || j < 0 || j >= m) return true;
    return false;
}

//Use a dfs to visit all the cells that belong to the same connected component (island).
void dfs(int i, int j, vector<vector<char>> &grid, int n, int m){

    grid[i][j] = '0';

    //Handle the neighbors.
    for(int k = 0; k < 4; ++k){
        int newi = i + row[k];
        int newj = j + col[k];

        if(!outOfBounds(newi, newj, n, m) && grid[newi][newj] == '1'){
            dfs(newi, newj, grid, n, m);
        }
    }
}

int solveNumberOfIslands(vector<vector<char>> &grid, int n, int m){

    int islands = 0;

    for(int i = 0; i < n; ++i){
        for(int j = 0; j < m; ++j){

            //This means we just found a new island, so we visit all the cells
            //that belong to this island so we do not count twice.

            if(grid[i][j] == '1'){
                islands++;
                dfs(i, j, grid, n, m);
            }
        }
    }

    return islands;
}

int main() {

    int n; cin >> n;
    int m; cin >> m;

    vector<vector<char>> grid(n, vector<char>(m));

    for(int i = 0; i < n; ++i){
        for(int j = 0; j < m; ++j){
            cin >> grid[i][j];
        }
    }

    cout << solveNumberOfIslands(grid, n, m) << "\n";
}

//Time Spent: 15 minutes