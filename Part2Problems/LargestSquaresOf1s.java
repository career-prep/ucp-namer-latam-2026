package Part2Problems;
//time comxplity o(m*n) row col
//sapce o(n) dp array
//time spend 23min
public class LargestSquaresOf1s {
    public static int largestSquaresOf1s(int[][] matrix){
        int row = matrix.length;
        int col = matrix[0].length;
        int maxSize = 0;
        int[][] dp = new int[row][col];
        for(int i=0;i<row;i++){
            for(int j=0;j<col;j++){
                if(matrix[i][j]==1){

                
                if(i ==0 || j ==0){
                    dp[i][j] = 1;
                }else{
                    dp[i][j] = 1 + Math.min(dp[i-1][j],Math.min(dp[i-1][j],dp[i-1][j-1]));
                }
                maxSize = Math.max(dp[i][j],maxSize);
            }
        }
        }
        return maxSize;
    }
      public static void main(String[] args) {
        int[][] matrix = {
            {0, 1, 0, 1},
            {0, 0, 1, 1},
            {0, 1, 1, 1},
            {0, 0, 1, 1}
        };

        System.out.println(largestSquaresOf1s(matrix));
}
}
