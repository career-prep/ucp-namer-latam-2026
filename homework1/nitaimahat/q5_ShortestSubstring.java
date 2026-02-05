package homework1.nitaimahat;
import java.util.*;
public class q5_ShortestSubstring {
    // thought process: since i need to the shortest substring, im thinking of using array with
    // the leght of ascii letetrs which is 128 and thne i will increment the target string by 1 
    // i will have two pointers first second pointing at 0 index of the comparing string and then 
    // have a variable counter taht keeps tracks of number of character in target string in the comparing string
    // if the counter equals the size of the target string i will check for minwindow size}
    // and continue comapring and retun the minwindow size at the end
    // the time complexity will be o(n+m) since im using a slidding window pattern and each pointer moves at most n times 
    // and space will be o(n+m) since i will be creating character array from the input strings.
    public static int shortSubstring(String s1, String s2){
        int[] arr = new int[128];
        char[] firstArr = s1.toCharArray();
        char[] secondArr = s2.toCharArray();

        for(char curr : secondArr){
            arr[curr]++;
        }
        int first = 0;
        int second = 0;
        int counter = 0;
        int minLength = Integer.MAX_VALUE;

        while(second < firstArr.length){
            char currChar = firstArr[second];
            arr[currChar]--;
            if(arr[currChar] >=0){
                counter++;
            }
            //shringk window

            while(counter == secondArr.length){
                int currWindow = second - first +1;
                if(currWindow < minLength){
                    minLength = currWindow;
                }
                char firstCount = firstArr[first];
                arr[firstCount]++;
                if(arr[firstCount]>0){
                    counter--;
                }
                first++;
            }
            second++;
        }
        return minLength;

    }
    //time spent 32 min

    public static void main(String[] args){
        String s1 = "abracadabra";
        String s2 = "abc";
        System.out.println(shortSubstring(s1, s2));

         String s3 = "zxycbaabcdwxyzzxwdcbxyzabccbazyx";
        String s4 = "zzyzx";
        System.out.println(shortSubstring(s3, s4));

         String s5 = "dog";
        String s6 = "god";
        System.out.println(shortSubstring(s5, s6));


    }

}
