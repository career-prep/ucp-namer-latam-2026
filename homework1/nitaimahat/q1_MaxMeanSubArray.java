package homework1.nitaimahat;
import java.util.*;
/**
 
 * 
 * Given an array of integers and an integer k, 
 * find the max mean of a subarray of size k
 */
// first thought: two pointers , one- at start & one at index k
    //                increment start and end pointer unditl end corss the length of the array
    //                have a sum variable to store sum of each window
    //                calcualting the mean then comapring it with a max 
    //                returning max at the end.

    //                since i will not be using any extra space or storage the space will be O(1)
    //                where as the time complexity will be o(n) where n will the the length of input array since i will have to loop the enitre array onces
    
    //                ** from rethinking my above apporch would be on worst case n^2  other wise(o(n*k) because i would need another loop to loop thourght start to end window, so
    //                waht im thinking of now is to firstly calcualte the mean of the first k integer in array
    //                then i will jsut simply remove the start index and add the end index and recalcualte and comper
                  // this will make my solution o(n) and space will remain o(1).
public class q1_MaxMeanSubArray {
    
            
    public static double maxMeanSubArray(int[] inputArray, int k){
        
        
         
        int sum = 0;
        for(int i=0;i<k;i++){
            sum += inputArray[i];
        }
        double maxMean = (double) sum/k;
        int left = 0;
        int right = k;
        while(right <inputArray.length){
            sum -= inputArray[left];
            left++;
            
            sum += inputArray[right];
            right++;
            maxMean = Math.max(maxMean,(double)sum/k);
          
            
        }
        return maxMean;
    }

    public static void main(String[] args){
        int[] test1 = {4,5,-3,2,6,1};
        int k = 2;
        System.out.println(maxMeanSubArray(test1,k));
         int[] test2= {4,5,-3,2,6,1};
        int l = 3;
        System.out.println(maxMeanSubArray(test2,l));
         int[] test3 = {1,1,1,1,-1,-1,2,-1,-1};
        int m = 3;
        System.out.println(maxMeanSubArray(test3,m));
         int[] test4 = {1,1,1,1,-1,-1,2,-1,-1,6};
        int n = 5;
        System.out.println(maxMeanSubArray(test4,n));
        
    }
    //time took 36min
    
}
