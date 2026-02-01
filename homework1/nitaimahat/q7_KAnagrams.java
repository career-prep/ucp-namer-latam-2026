package homework1.nitaimahat;
import java.util.*;
public class q7_KAnagrams {
    //time o(n+m) space o(1)
    public static boolean kAnagrams(String s1,String s2,int k){
        if(s1.length()!=s2.length()){
            return false;
        }
        int[] arr = new int[26];

        for(char curr : s1.toCharArray()){
            if(Character.isLetter(curr)){
                arr[curr-'a']++;
            }
            
        }
        for(char curr1 : s2.toCharArray()){
            if(Character.isLetter(curr1)){
                arr[curr1-'a']--;
            }
        }
        int count = 0;
        for(int num: arr){
            if( num <0){
                count += -num;
            }
        }
        if(count <=k){
            return true;
        }
        return false;

    }
    //time spent 18min
    public static void main(String[] args){
        String test1 = "apple";
        String test = "peach";
        int k = 1;
        System.out.println(kAnagrams(test1, test, k));
        String test3 = "apple";
        String tes4 = "peach";
        int l = 2;
        System.out.println(kAnagrams(test3, tes4, l));
        
        String test5 = "cat";
        String tes6 = "dog";
        int m = 3;
        System.out.println(kAnagrams(test5, tes6, m));

         String test7 = "debit curd";
        String tes8 = "bad credit";
        int n = 1;
        System.out.println(kAnagrams(test7, tes8, n));

         String test9 = "baseball";
        String tes10 = "basketball";
        int o = 2;
        System.out.println(kAnagrams(test9, tes10, o));
    }
}
