package homework0.nitai_mahat;

import java.util.*;
/**
 * Time complexity = O(n) where n is the number of integer in  provided array
 * Space complexity = O(n) where n is the size of the hashset
 * 
 * 
 */
public class q1_UniqueSum {
    /**
     * return the sum of unique Integers in the array
     * @param numArray
     * @return
     */
    public static int uniqueSum(int[] numArray){
        Set<Integer> uniqueNumbers = new HashSet<>();
        for(int num : numArray){
            uniqueNumbers.add(num);
        }
        int sum =0;
        for(int number : uniqueNumbers){
            sum += number;
        }
        return sum;
    }
    public static void main(String[] args){
        int[] test1 = {1,10,8,3,2,5,7,2,-2,-1};
        System.out.println(uniqueSum(test1));

        int[] test2 = {4,3,3,5,7,0,2,3,8,6};
        System.out.println(uniqueSum(test2));


    }
    //time spent: 3 min
  
    
}
