package homework0.nitai_mahat;

import java.util.*;

/**
 * Time complexity = O(n) where n is the number of integer in provided array
 * Space complexity = O(n) where n is the size of the hashmap
 * 
 * 
 */
public class q0_ZeroSum {
    /**
     * returns the number of pairs of integers in the array that sum to 0 
     * where each index can be used once
     * @param numbers
     * @return
     */
    public static int sumToZero(int[] numbers){
        Map<Integer,Integer> seenMap = new HashMap<>();
        int pairs = 0;
        for(int num : numbers){
            int complement = -num;
            if(seenMap.containsKey(complement) && seenMap.get(complement)>0){
                pairs++;
                seenMap.put(complement,seenMap.get(complement)-1);
            }else{
                if(seenMap.containsKey(num)){
                    seenMap.put(num,seenMap.get(num)+1);

                }else{
                    seenMap.put(num,1);
                }
            }
           
        }
         return pairs;
            
    }
    /**
     * return the number of pairs that sum to 0
     * where elemt can be re used in differet pairs 
     * @param numbers
     * @return
     */
    public static int sumToZeroFollowUp(int[] numbers){
        int pairs = 0;
        Map<Integer,Integer> seenMap = new HashMap<>();
        for(int num : numbers){
            if(seenMap.containsKey(num)){
                seenMap.put(num,seenMap.get(num)+1);
            }else{
                seenMap.put(num,1);
            }
               
        }
        for(int num : seenMap.keySet()){
           
            if(num==0){
            int zeroCount = seenMap.get(0);
            pairs += (zeroCount * (zeroCount-1))/2;// using combinations because it gives unique ways to pick two different indicies
            }else if(num >0){
                 int complement = -num;
                  if(seenMap.containsKey(complement)){
                pairs += seenMap.get(num) * seenMap.get(complement);//gives unique index combinations
                 }
            }
           
        }
        
        return pairs;

       
    }
    // time spent : 36 min

    public static void main(String[] args){
        int[] test1 = {1,10,8,3,2,5,7,2,-2,-1};
        System.out.println(sumToZero(test1));
        int[] test2 = {1,10,8,-2,2,5,7,2,-2,-1};
        System.out.println(sumToZero(test2));
        int[] test3 = {4,3,3,5,7,0,2,3,8,6};
        System.out.println(sumToZero(test3));
        int[] test4 = {4,3,3,5,7,0,2,3,8,0};
        System.out.println(sumToZero(test4));


        int[] test11 = {1,10,8,3,2,5,7,2,-2,-1};
        System.out.println(sumToZeroFollowUp(test11));
        int[] test22 = {1,10,8,-2,2,5,7,2,-2,-1};
        System.out.println(sumToZeroFollowUp(test22));
        int[] test33 = {4,3,3,5,7,0,2,3,8,6};
        System.out.println(sumToZeroFollowUp(test33));
        int[] test44 = {4,3,3,5,7,0,2,3,8,0};
        System.out.println(sumToZeroFollowUp(test44));
    }
}

