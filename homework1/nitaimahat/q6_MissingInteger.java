package homework1.nitaimahat;
import java.util.*;
public class q6_MissingInteger {
    // thought: i was thinking of hvaiong two pointers one starts at 0 index and 
    // another starts +1 of the first pointer i will run a check to see if 
    // both integer only differs by 1 if not i will return left poiunter +1 since that wil be the missing MAX_VALUE
    //time o(n) and space o(1)
    public static int missInteger(int[] inputArray,int n){
        int left = 0;
        int right = 1;
        while(right <inputArray.length){
            if(inputArray[right] - inputArray[left]!=1){
                return inputArray[left]+1;
            }
            right++;
            left++;
        }
        
        return inputArray[left]+1;
    }

    public static void main(String[] args){
        int[] test1 = {1,2,3,4,6,7};
        int n = 7;
        System.out.println(missInteger(test1, n));

        int[] test2 = {1};
        int m = 2;
        System.out.println(missInteger(test2, m));

        int[] test3 = {1,2,3,4,5,6,7,8,10,11,12};
        int p = 12;
        System.out.println(missInteger(test3, p));
        
    }
    //time spent 10 min
}
