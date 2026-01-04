package homework0.nitai_mahat;

import java.util.*;
/**
 * Time complexity = O(n) where n is the length of string
 * Space complexity = O(n) where n is the size of the hashset
 * 
 * 
 */
public class q2_FirstOccurrence {
    public static String firstOccurence(String word){
        StringBuilder finalString = new StringBuilder();
        Set<Character> uniqueSet = new HashSet<>();
    for(Character letter : word.toCharArray()){
        if(!uniqueSet.contains(letter)){
              finalString.append(letter);
        }
      
        uniqueSet.add(letter);
    }
    
   
    return finalString.toString();
    }
    //time spent: 8 min

    public static void main(String[] args){
        String test1 = "abracadabra";
        System.out.println(firstOccurence(test1));

        String test2 = "Uber CaPp";
        System.out.println(firstOccurence(test2));

        String test3 = "zzyzx";
        System.out.println(firstOccurence(test3));


    }
 
    
}
