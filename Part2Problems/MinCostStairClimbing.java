package Part2Problems;

public class MinCostStairClimbing {
    /**
     * [4,1,6,3,5,8]
     * 1,3,5
     * [11,8,3,4,9,13,10]
     * 
     * space = 0(n) 
     * time = o(n)
     * timespent : 20min
     * dsa: dp array and memoization
     */
    
    public static int minCostStair(int[] cost){
        if(cost==null || cost.length==0){
            return 0;
        }
        int[] dp =new int[cost.length];
        dp[0] = cost[0];
        dp[1] = cost[1];
        for(int i=2;i<dp.length;i++){
            dp[i]  = cost[i] + Math.min(dp[i-1],dp[i-2]);

        }
        return Math.min(dp[cost.length-1],dp[cost.length-2]);
    }
    public static void main(String[] args){
        int[] input = {4,1,6,3,5,8};
        int[] input1 = {11,8,3,4,9,13,10};
        System.out.println(minCostStair(input));
         System.out.println(minCostStair(input1));
    }
        

}
