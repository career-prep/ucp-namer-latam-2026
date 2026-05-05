package Part2Questions;
import java.util.*;
/**
 * Approach:
 * I treat the grid as a graph where each cell is a node.
 * When I find a '1', I use DFS to explore and mark all connected land cells as visited.
 * Each time I start a new DFS, it means I found a new island.
 *
 * DSA used: Graph + DFS
 *
 * Time Complexity: O(m * n) → visit each cell once
 * Space Complexity: O(m * n) → recursion stack in worst case
 * time spent 20min
 */
public class q4_NumberOfIslands {

    static int numOfIslands(int[][] islandMatrix){
        if(islandMatrix.length==0){
            return 0;//return 0 island
        }
        int countIsland = 0;
        for(int i=0;i<islandMatrix.length;i++){
            for(int j=0;j<islandMatrix[0].length;j++){
                if(islandMatrix[i][j]==1){
                    countAddress(islandMatrix,i,j);
                    countIsland++;
                }
            }
        }
        return countIsland;
    }
    private static void countAddress(int[][] islandMatrix, int row,int col){
        if(row < 0 || col <0 || row >= islandMatrix.length || col >= islandMatrix[0].length || islandMatrix[row][col]==0){
            return;
        }
        islandMatrix[row][col] = 0;

        countAddress(islandMatrix,row-1,col);
        countAddress(islandMatrix,row+1,col);
        countAddress(islandMatrix,row,col-1);
        countAddress(islandMatrix,row,col+1);
    }

    public static void main(String[] args){
        int[][] test1 ={
            {1,0,1,1,1},
            {1,1,0,1,1},
            {0,1,0,0,0},
            {0,0,0,1,0},
            {0,0,0,0,0}

        };
        int[][] test2 ={
            {1,0,0},
            {0,0,0}

        };
        System.out.println(numOfIslands(test2));
    }
    
}
