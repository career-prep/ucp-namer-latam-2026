package homework1.nitaimahat;
import java.util.*;

public class q2_ReverseVowels{
    // my first thoought process is taht i will have two pointer one at the start and one at the end then i will increment left and right unles both are reverseVowelsusing
    // conditions and swap it each time both are vowels. To make swaping easier i will conver the string to a char array and then swap it using a temp variable 
    // this apporach will will be time o(n) where n will be the size of the string (length of string) an space will also be o(n) since we are creating 
    // array from input string which requires linear extra space
    public static String reverseVowels(String sentence){
         char[] characterArray = sentence.toCharArray();
        int left = 0;
        int right = characterArray.length-1;
       
        while(left<=right){
            if(isVowel(characterArray[left]) && isVowel(characterArray[right])){
                    char temp = characterArray[left];
                    characterArray[left] = characterArray[right];
                    characterArray[right] = temp;
                    left++;
                    right--;
            }else if(isVowel(characterArray[left])){
                right--;
            }else{
                left++;
            }
                
            }
           
        return new String(characterArray);

        }
        
    public static boolean isVowel(char letter){
        letter = Character.toLowerCase(letter);
        return letter == 'a' || letter == 'e' || letter == 'i' || letter == 'o' || letter == 'u';

    }
    public static void main(String[] args){
        String test1 = "Uber Career Prep";
        System.out.println(reverseVowels(test1));

         String test2 = "xyz";
        System.out.println(reverseVowels(test2));

         String test3 = "flamingo";
        System.out.println(reverseVowels(test3));
    }
    

    
    }
    //time spend on this 15 min

    

