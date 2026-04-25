package Part2Questions;
import java.util.*;
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
