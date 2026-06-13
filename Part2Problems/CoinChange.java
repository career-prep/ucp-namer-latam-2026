package Part2Problems;

//time complxity = o(n*m) for both coins nd lopping thoruhg target;
//space complxity is = o(n) due to dp array


public class CoinChange {
    public static int coinChange(int[] coins , int target){
        int[] dp = new int[target+1];
        //[2,5,10]
        //[20]
        dp[0] = 1;
        for(int coin : coins){
            for(int i=coin; i<= target;i++){
                dp[i] += dp[i-coin];
            }
        }
        return dp[target]; 

    }
    public static void main(String[] args){
        int[] test1 = {2,5,10};
        int target = 20;
        int tar2 = 15;
        System.out.println(coinChange(test1, target));
        System.out.println(coinChange(test1, tar2));
    }
}
