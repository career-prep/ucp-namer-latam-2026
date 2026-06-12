package Part2Problems;
import java.util.*;
public class CatalanNumbers {
    
    //dsa used dp array memoization
    //time comp[lxity is o(n^2) i could not figure out a more efficient way then this
    //space is o(n);
    //time spent 38min;
    public static int[] catalanNumbers(int n){
        if(n==0){
            return new int[] {1};
        }
        int[] dp = new int[n+1];
        dp[0] = 1;
        dp[1] = 1;
        for(int i=2;i<dp.length;i++){
            for(int j=0;j<i;j++){
                dp[i] += dp[j] * dp[i-1-j];
            }
        }
        return dp;
    }
    public static void main(String[] args){
        int n = 5;
        int m=1;
        int[] res = catalanNumbers(n);
        int[] res1 = catalanNumbers(m);
        int[] res2 = catalanNumbers(0);
        for(int i=0;i<res.length;i++){
            System.out.print(" " + res[i]);
            
        }
        System.out.println();
        for(int i=0;i<res1.length;i++){
            System.out.print(" " + res1[i]);
        }
          System.out.println();
          if(res2.length==0){
            System.out.println("null");
          }else{
             for(int i=0;i<res2.length;i++){
            System.out.print(" " + res2[i]);
        }
          }
        
    }
}
