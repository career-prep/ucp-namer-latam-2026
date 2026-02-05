package homework1.nitaimahat;
import java.util.*;
public class q4_BackspaceStringCompare {
    //time 0(n+m) , space O(n+m) (because of stringbuilder);
    public static boolean backspaceString(String s1, String s2){
        return checkBackspace(s1).equals(checkBackspace(s2));
    }
    private static String checkBackspace(String sentence){
        StringBuilder finalString = new StringBuilder();
        int right = sentence.length()-1;
        int hashcount = 0;
        while(right >=0){
            //u#Uber Career#r Prep";
            
            if(sentence.charAt(right)=='#'){
                hashcount++;    
            }else if(sentence.charAt(right)!='#' && hashcount==0){
                finalString.append(sentence.charAt(right));
            }else if(sentence.charAt(right)!='#'&& hashcount >0){
                hashcount--;
                
            }
            right--;
        }
        return finalString.toString();
    }

    public static void main(String[] args){
        String s1 = "abcde";
        String s2 = "abcde";
        System.out.println(backspaceString(s1, s2));
        String s3 = "Uber Career Prep";
        String s4 = "u#Uber Career#r Prep";
        System.out.println(backspaceString(s3, s4));

        String s5 = "abcdef###xyz";
        String s6 = "abcw#xyz";
        System.out.println(backspaceString(s5, s6));

        String s7 = "abcdef###xyz";
        String s8 = "abcdefxyz###";
        System.out.println(backspaceString(s7, s8));
    }
    //timeSpent 15 min
    
}
