package homework1.nitaimahat;
import java.util.*;
public class q3_ZeroSumSubArrays {
    // my thought process is that i will have two pointers 
    // starting at the same index and i will increment the right
    // pointer and check if it equals 0 or the sum equals q3_ZeroSumSubArrays
    // based on the condition i will increment the zeroArray count.
    // keeping my time and space to 0(n) nad space to o(1)
    // on a seocnd thouhght since i need to loop twice and right goes thorugh every integer
    //my complexity (time) would be o(n^2).
    
    //from completing this i realized i dont need to check for zero since current sum will checl for it
    //*** completed using brute force apporach however i feel like using hasmap would help make it more efficent */
    // public static int zeroSumArray(int[] inputArray){
    //     //brute force way
    //    int subArrayCount = 0;
    //     for(int left=0;left<inputArray.length;left++){
    //         int right = left;
    //         int currentSum = 0;
    //         while(right < inputArray.length){
    //             currentSum += inputArray[right];
                
    //             if(currentSum ==0){
    //                 subArrayCount++;
    //             }
    //             right++;
    //         }
           
    //     }
    //     return subArrayCount;
    // }

    //4,5,2,-1,-3,-3,4,6,-7
    public static int zeroSumArray(int[] inputArray){
        int sum = 0;
        int count = 0;

        Map<Integer,Integer> seenMap = new HashMap<>(); // map = {0:1 ,1:1, 4:2, 9 :1 , 11:2 , 10:1, 7:1, 5:1}
        seenMap.put(0,1);
        for(int num : inputArray){ // num = -3
            sum += num; // sum = 4

            if(seenMap.containsKey(sum)){
                count += seenMap.get(sum); // count = 2
            }

            if(seenMap.containsKey(sum)){
                seenMap.put(sum,seenMap.get(sum)+1);
            }else{
                seenMap.put(sum,1);
            }
                 
            
        }
        return count;
        //total time spedn 35  min
      
    }
    public static void main(String[] args){
        int[] test1 = {4,5,2,-1,-3,-3,4,6,-7};
        System.out.println(zeroSumArray(test1));

        int[] test2 = {1,8,7,3,11,9};
        System.out.println(zeroSumArray(test2));

        int[] test3 = {8,-5,0,-2,3,-4};
        System.out.println(zeroSumArray(test3));
    }
    
}
