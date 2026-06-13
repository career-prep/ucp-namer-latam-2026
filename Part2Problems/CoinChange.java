package Part2Problems;

//Given a list of coin denomintions and a target um k , return the number of possible wys to make
//chnge for tht sum.
public class CoinChange {
    public int coinChange(int[] coins , int target){
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
    public void main(String[] args){
        int[] test1 = {2,5,10};
        int target = 20;
        System.out.println(coinChange(test1, target));
    }
}
